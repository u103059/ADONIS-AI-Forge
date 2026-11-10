# Technische Dokumentation - ADONIS-AI-Forge

## Übersicht
Diese Dokumentation beschreibt die technischen Grundlagen und Voraussetzungen zur Nutzung von ADONIS-AI-Forge für die KI-gestützte Erstellung ADONIS-kompatibler BPMN-Prozessmodelle, Prozesssteckbriefe, methodische Reviews und geführte Prozessaufnahmen.

## Systemvoraussetzungen

### Software-Anforderungen
- **Visual Studio Code** (aktuelle Version mit Unterstützung für Custom Agents / `.agent.md`)
- **GitHub Copilot Subscription** (optional)

### Betriebssystem
- Windows 10/11
- macOS 10.15 oder höher
- Linux (Ubuntu 20.04 oder höher empfohlen)

## Erforderliche VS Code Extensions

### 1. GitHub Copilot Chat (erforderlich)
**Extension ID:** `GitHub.copilot-chat`

**Zweck:** KI-gestützte BPMN-Generierung und interaktive Kommunikation mit den Agenten (enthält die frühere Extension `GitHub.copilot`)


### 2. Camunda Modeler by Miragon (erforderlich)
**Extension ID:** `miragon-gmbh.vs-code-bpmn-modeler`

**Zweck:** Visuelle Darstellung, Simulierung und Bearbeitung von BPMN-Diagrammen


### 3. GitHub Pull Requests (empfohlen)
**Extension ID:** `github.vscode-pull-request-github`

**Zweck:** Pull Requests und Issues direkt in VS Code prüfen und verwalten


### 4. GitHub Repositories (empfohlen)
**Extension ID:** `github.remotehub`

**Zweck:** Remote-GitHub-Repositories direkt in VS Code durchsuchen, bearbeiten und committen, ohne lokalen Clone

### 5. VS Code Speech (optional)
**Extension ID:** `ms-vscode.vscode-speech`

**Zweck:** Spracheingabe (Speech-to-Text) in VS Code und Copilot Chat

### 6. German language support for VS Code Speech (optional)
**Extension ID:** `ms-vscode.vscode-speech-language-pack-de-de`

**Zweck:** Deutsche Sprachunterstützung für VS Code Speech


## Verfügbare Agenten

| Agent | Zweck |
|---|---|
| `ADONIS_BPMN_KO` | Prozessmodell mit den Pools Kunde und Organisation (ADONIS-Import-kompatibel) |
| `ADONIS_BPMN_KOI` | Prozessmodell mit den Pools Kunde, IT und Organisation (ADONIS-Import-kompatibel) |
| `ADONIS_BPMN_I` | IT-Datenverarbeitung über mehrere IT-System-Pools mit Nachrichtenflüssen (ADONIS-Import-kompatibel) |
| `Steckbrief` | Prozesssteckbrief mit Prozess- und Aktivitäts-KPIs auf Basis des Templates |
| `ADONIS_Review` | Methodische Prüfung von ADONIS-Prozessmodellen (BPMN 2.0, ADONIS-Kompatibilität, GPM-Standards) |
| `Moritz` | Geführtes Interview zur Ist-Prozessaufnahme mit Steckbrief und BPMN-Ist-Modell |

## BPMN-Generierung mit Copilot Chat
1. Öffnen Sie Copilot Chat (`Ctrl+Alt+I` / `Cmd+Alt+I`)
2. KI-Modell auswählen
3. Passenden BPMN-Agenten auswählen (siehe [Verfügbare Agenten](#verfügbare-agenten))
4. Prozess benennen oder einsprechen

## Prozesssteckbrief-Generierung mit Copilot Chat
1. Agent "Steckbrief" auswählen
2. Erstellung über Prompt anstoßen, z. B. "Erstelle Steckbrief"

## Geführte Prozessaufnahme mit Moritz
1. Agent "Moritz" auswählen
2. Namen des aufzunehmenden Prozesses eingeben, z. B. "Starte Prozessaufnahme Wohngeld beantragen"
3. Die Interviewfragen beantworten (optional per Spracheingabe)
4. Ergebnis: Prozesssteckbrief und ADONIS-kompatibles BPMN-Ist-Prozessmodell (ein Pool Organisation mit Lanes)

## ADONIS-Modelle per API abrufen und prüfen
Voraussetzungen: Python 3.10+, lokaler Clone im Stadtnetz, REST-API und Basic Auth für den API-Nutzer in ADONIS aktiviert.

1. `cd tools/adonis_fetch` und `pip install --proxy http://webgateway.lhs.stuttgart.de:9090 -r requirements.txt`
2. `.env.example` nach `.env` kopieren und `ADONIS_BASE_URL` sowie ggf. `ADONIS_USER` eintragen. `ADONIS_PASSWORD` leer lassen: Das Skript fragt das Passwort per Dialog ab und speichert es im Windows-Schlüsselbund.
3. `python fetch_models.py --discover` - Repository-ID und Attributname des Freigabe-Workflow-Status ermitteln, ggf. in `.env` anpassen
4. `python fetch_models.py --dry-run` - Trefferliste prüfen
5. `python fetch_models.py` - Modelle nach `Import_ADONIS/` exportieren
6. Agent "ADONIS_Review" auswählen und z. B. "Prüfe alle Modelle in Import_ADONIS" eingeben

Hinweise:
- `python fetch_models.py --logout` löscht die gespeicherten Zugangsdaten.
- Das Zertifikat der internen LHS-CA wird automatisch aus dem Windows-Zertifikatsspeicher verwendet.
- Ausgabe je Modell als `.bpmn`; bietet ADONIS keinen BPMN-Export per REST an, wird stattdessen eine `.json`-Datei mit Objektdetails und Imagemap abgelegt. Zusätzlich entsteht `Import_ADONIS/manifest.json`.
- `Import_ADONIS/` und `.env` sind per `.gitignore` von der Versionierung ausgeschlossen.

## Troubleshooting

### Problem: Copilot bricht ab und generiert kein BPMN (Timeout)
**Lösung:** 
- Über Prompt klarstellen, dass ein vereinfachtes Prozessmodell erstellt werden soll
- anderes KI-Modell auswählen
- es an einem anderen Tag wieder versuchen
  
## Support und Kontakt

Bei Fragen oder Problemen:
- Projektverantwortliche kontaktieren

---

**Stand:** November 2026  
**Version:** 1.4


