"""Ruft ADONIS-Modelle mit Freigabe-Workflow-Status 'In methodischer Pruefung' ab und legt sie in Import_ADONIS/ ab.

Aufruf:
    python fetch_models.py --discover   # Repositories und Beispiel-Attribute anzeigen
    python fetch_models.py --dry-run    # Nur Trefferliste anzeigen
    python fetch_models.py              # Modelle exportieren
"""

import argparse
import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

import requests
import truststore
from dotenv import load_dotenv

# Interne LHS-CA ist nur im Windows-Zertifikatsspeicher hinterlegt
truststore.inject_into_ssl()

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent.parent
OUTPUT_DIR = REPO_ROOT / "Import_ADONIS"

load_dotenv(SCRIPT_DIR / ".env")


def env(name: str, default: str | None = None, required: bool = False) -> str | None:
    value = os.getenv(name, default)
    if required and not value:
        sys.exit(f"Fehlende Umgebungsvariable: {name} (siehe .env.example)")
    return value


BASE_URL = env("ADONIS_BASE_URL", required=True).rstrip("/")
API_ROOT = env("ADONIS_API_ROOT", "/rest/2.0")
MODEL_CLASS = env("ADONIS_MODEL_CLASS", "MT_BUSINESS_PROCESS_DIAGRAM_BPMN_20")
STATUS_ATTR = env("ADONIS_STATUS_ATTR", "MFB_RWF_STATE")
STATUS_VALUE = env("ADONIS_STATUS_VALUE", "In methodischer Prüfung")
# Pfadvorlage relativ zu API_ROOT; Platzhalter {repo_id} und {model_id}
EXPORT_PATH = env("ADONIS_EXPORT_PATH", "/repos/{repo_id}/models/{model_id}/format?format=bpmn")


def ask_credentials() -> tuple[str, str]:
    import tkinter as tk
    from tkinter import simpledialog

    root = tk.Tk()
    root.withdraw()
    root.attributes("-topmost", True)
    user = env("ADONIS_USER") or simpledialog.askstring("ADONIS-Anmeldung", "Benutzername:", parent=root)
    password = simpledialog.askstring("ADONIS-Anmeldung", f"Passwort fuer {user}:", show="*", parent=root)
    root.destroy()
    if not user or not password:
        sys.exit("Anmeldung abgebrochen.")
    return user, password


def create_session() -> requests.Session:
    session = requests.Session()
    user, password = env("ADONIS_USER"), env("ADONIS_PASSWORD")
    session.auth = (user, password) if user and password else ask_credentials()
    session.headers.update({"Accept": "application/json"})
    session.verify = env("ADONIS_CA_BUNDLE") or True
    return session


def get(session: requests.Session, path: str, **kwargs) -> requests.Response:
    url = f"{BASE_URL}{API_ROOT}{path}"
    response = session.get(url, timeout=60, **kwargs)
    if response.status_code == 401:
        sys.exit("401 Unauthorized: Benutzer/Passwort pruefen bzw. Basic Auth in ADONIS aktivieren.")
    if response.status_code == 403:
        sys.exit(f"403 Forbidden: API-Nutzer hat keine Rechte fuer {path}.")
    if response.status_code == 404:
        raise FileNotFoundError(f"404 Not Found: {url} - Endpunkt in ADONIS_API_ROOT/ADONIS_EXPORT_PATH pruefen.")
    response.raise_for_status()
    return response


def resolve_repo_id(session: requests.Session) -> str:
    repo_id = env("ADONIS_REPO_ID")
    if repo_id:
        return repo_id
    repos = get(session, "/repos").json()
    items = repos.get("repos", repos) if isinstance(repos, dict) else repos
    if len(items) != 1:
        names = ", ".join(f"{r.get('name')} ({r.get('id')})" for r in items)
        sys.exit(f"Mehrere Repositories gefunden, ADONIS_REPO_ID setzen: {names}")
    return items[0]["id"]


def build_query(with_status: bool = True) -> str:
    override = env("ADONIS_SEARCH_QUERY")
    if override:
        return override
    filters: list[dict] = [{"className": MODEL_CLASS}]
    if with_status:
        filters.append({"attrName": STATUS_ATTR, "op": "OP_EQ", "value": STATUS_VALUE})
    return json.dumps({"filters": filters, "attributes": ["NAME", STATUS_ATTR]}, ensure_ascii=False)


def search_models(session: requests.Session, repo_id: str, with_status: bool = True) -> list[dict]:
    result = get(session, f"/repos/{repo_id}/search", params={"query": build_query(with_status)}).json()
    return result.get("items", []) if isinstance(result, dict) else result


def safe_filename(name: str) -> str:
    cleaned = re.sub(r"[^\w\-. ]", "_", name, flags=re.UNICODE).strip()
    return re.sub(r"\s+", "_", cleaned)[:120] or "Modell"


def discover(session: requests.Session) -> None:
    print("Repositories:")
    print(json.dumps(get(session, "/repos").json(), indent=2, ensure_ascii=False))
    repo_id = resolve_repo_id(session)
    models = search_models(session, repo_id, with_status=False)
    print(f"\n{len(models)} Modelle der Klasse {MODEL_CLASS} gefunden.")
    if models:
        model_id = models[0]["id"]
        print("Beispielmodell (Attributnamen fuer ADONIS_STATUS_ATTR suchen):")
        print(json.dumps(get(session, f"/repos/{repo_id}/models/{model_id}").json(), indent=2, ensure_ascii=False))


def fetch_link(session: requests.Session, obj: dict) -> dict:
    href = next((l["href"] for l in obj.get("rest_links", []) if l.get("rel") == "self"), None)
    if not href or not href.startswith(BASE_URL):
        return obj
    response = session.get(href, timeout=60)
    return response.json().get("item", obj) if response.ok else obj


def export_model(session: requests.Session, repo_id: str, model: dict) -> Path:
    model_id = model["id"]
    filename = safe_filename(f"{model.get('name', 'Modell')}_{model_id}")
    try:
        response = get(session, EXPORT_PATH.format(repo_id=repo_id, model_id=model_id),
                       headers={"Accept": "application/xml"})
        target = OUTPUT_DIR / f"{filename}.bpmn"
        target.write_bytes(response.content)
    except FileNotFoundError:
        # Fallback, falls die Instanz keinen BPMN-Export per REST anbietet
        data = get(session, f"/repos/{repo_id}/models/{model_id}").json()
        item = data.get("item", data)
        item["objectDetails"] = [fetch_link(session, obj) for obj in item.get("objects", [])]
        item["imagemap"] = get(session, f"/repos/{repo_id}/models/{model_id}/imagemap").json().get("item")
        target = OUTPUT_DIR / f"{filename}.json"
        target.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
    return target


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--discover", action="store_true", help="Repositories und Attribute anzeigen")
    parser.add_argument("--dry-run", action="store_true", help="Nur Treffer anzeigen, nichts speichern")
    args = parser.parse_args()

    session = create_session()
    if args.discover:
        discover(session)
        return

    repo_id = resolve_repo_id(session)
    models = search_models(session, repo_id)
    print(f"{len(models)} Modelle mit Status '{STATUS_VALUE}' gefunden.")
    for model in models:
        print(f"  - {model.get('name')} ({model.get('id')})")
    if args.dry_run or not models:
        return

    OUTPUT_DIR.mkdir(exist_ok=True)
    manifest = []
    for model in models:
        target = export_model(session, repo_id, model)
        manifest.append({
            "id": model.get("id"),
            "name": model.get("name"),
            "version": model.get("version"),
            "status": STATUS_VALUE,
            "datei": target.name,
            "abgerufen": datetime.now(timezone.utc).isoformat(),
        })
        print(f"Gespeichert: {target.relative_to(REPO_ROOT)}")

    (OUTPUT_DIR / "manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")


if __name__ == "__main__":
    main()
