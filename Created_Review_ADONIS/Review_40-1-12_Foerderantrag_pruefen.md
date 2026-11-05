# Prüfbericht: `40-1-12 Aktiv Förderantrag prüfen`

> **Datei**: `40-1-12 Aktiv Förderantrag prüfen (de).bpmn`
> **Geprüft am**: `05.11.2026`
> **Geprüft durch**: GovModeler_ADONIS_Review

---

## Zusammenfassung

| Kriterium | Ergebnis |
|---|---|
| **Gesamtbewertung** | `Nachbesserung erforderlich` |
| **Kritische Fehler** | `3` |
| **Warnungen** | `9` |
| **Hinweise** | `4` |

**Kritische Fehler**
1. Kein Kunde-Pool, keine Nachrichtenflüsse (Pflicht).
2. Genehmigungspfad endet an einem parallelen Gateway ohne ausgehenden Fluss; es gibt kein Endereignis für den Happy Path (Deadlock/Sackgasse).
3. Das ereignisbasierte Gateway nach dem „Teilprozess" hat 4 ausgehende Sequenzflüsse, von denen 2 Paare dieselben Ziele doppelt anbinden.

---

## 1. Pool-Struktur und Akteure

| Kriterium | Status | Befund |
|---|---|---|
| **Kunde-Pool** vorhanden (White- oder Black-Box) | ❌ | Es existiert nur ein Participant (`40-1 beispiele`). Kein Kunde-Pool, keine Nachrichtenflüsse. Das Startereignis „Antrag eingegangen" liegt in der Organisation, nicht beim Kunden. |
| **Organisation-Pool** vorhanden | ⚠️ | Pool mit 2 Lanes vorhanden, aber Pool-Name `40-1 beispiele` ist nicht aussagekräftig und Lane 2 heißt `2-2`. |
| **IT-Pool** (optional, bewertet falls vorhanden) | ➖ | Nicht vorhanden. Hinweis: „in Datenbahn erheben" und das Erstellen von Bescheid/Ablehnungsschreiben (Poststelle) deuten auf Systemunterstützung hin. Ein IT-Pool oder die Referenzierung der Systeme an den Tasks wäre sinnvoll. |

**Bewertung**: Die KOI-Struktur ist nicht erfüllt. Der Kunde als Auslöser und Empfänger (Nachforderung, Bescheid, Ablehnung) fehlt vollständig. Die Organisation ist in zwei Lanes aufgeteilt, die Lane-Bezeichnungen sind jedoch nicht tragfähig.

---

## 2. Prozessumfang und Verständlichkeit

**Schrittanzahl pro Pool**:

| Pool | Anzahl Tasks | Anzahl Gateways | Anzahl Events |
|---|---|---|---|
| Kunde | 0 (Pool fehlt) | 0 | 0 |
| Organisation – Lane `40-1.1 SB Organisation` | 4 | 2 | 5 (1 Start, 1 Ende, 3 Zwischenereignisse) |
| Organisation – Lane `2-2` | 3 + 1 Teilprozess | 2 | 3 (Zwischenereignisse) |
| **Organisation gesamt** | **7 + 1 Teilprozess** | **4** | **8** |
| IT | 0 (nicht vorhanden) | 0 | 0 |

**Verständlichkeit**: Der Umfang ist überschaubar, die Lesbarkeit ist jedoch eingeschränkt: Der Fluss springt mehrfach zwischen den Lanes, ein Sequenzfluss läuft ca. 800 px entgegen der Modellierungsrichtung zurück (`Auftrag eingegangen` → `Ablehnung Antrag, erstellen und verschicken`), das Endereignis liegt links von dem Ereignis, das ihm vorgeschaltet ist. Doppelte Flüsse liegen deckungsgleich übereinander. Der Genehmigungspfad (eigentlicher Happy Path) bricht ab.

**Empfehlungen zur Kompaktheit** (ohne Reduzierung der Schritte):
- Die Übergabe `An SB weiterleiten` → `Antrag eingegangen` (Lane-Wechsel) als Nachricht/Übergabe klar kennzeichnen oder die Lane-Aufteilung überdenken, statt Transportschritt + Eingangsereignis zu modellieren.
- Die Nachforderungsschleife (Unterlagen nachfordern, Warten auf Unterlagen/2 Wochen, erneute Prüfung) bleibt im Hauptfluss; der „Teilprozess" sollte benannt und tatsächlich als Teilprozess referenziert werden.
- `Ablehnung Antrag, erstellen und verschicken` ggf. in „Ablehnungsbescheid erstellen" und „Ablehnungsbescheid versenden" aufteilen oder als einen klar benannten Task führen.

---

## Detaillierte Befunde

> **Legende**: ✅ Ja – Kriterium erfüllt | ❌ Nein – Kriterium verletzt | ➖ Nicht relevant

### Allgemeine Struktur

| MP-Nr. | Prüfkriterium | ✅ Ja | ❌ Nein | ➖ Nicht relevant | Bemerkung |
|---|---|:---:|:---:|:---:|---|
| MP1 | Enthält der Prozess keine personenbezogenen Daten? | ☐ | ☒ | ☐ | Der Änderungsverlauf (`MFB_RWF_HISTORY`) enthält Name und Benutzerkennung der Ersteller-Person. Systemmetadaten, aber personenbezogen; vor Abnahme prüfen. |
| MP2 | Ist der Prozess in der richtigen Ablagestruktur? | ☐ | ☐ | ☒ | Aus der Datei nicht prüfbar. |
| MP3 | Enthält der Prozess keine vertraulichen oder höher eingestuften Inhalte? | ☒ | ☐ | ☐ | Keine entsprechenden Inhalte erkennbar. |
| MP4 | Modellierungsrichtung einheitlich? (von links nach rechts bei BPMN) | ☐ | ☒ | ☐ | `Auftrag eingegangen` (x≈1846) → `Ablehnung Antrag…` (x≈1062) läuft nach links zurück; `Auftrag eingegangen` liegt rechts vom Endereignis `Antrag abgelehnt` (x≈1259). |
| MP5 | Ist der Prozessname aussagekräftig, enthält keine Abkürzungen und Paragrafen? | ☒ | ☐ | ☐ | Modellname „Förderantrag prüfen" ist passend. Das Präfix „Aktiv" im Modellnamen ist ein Statuszusatz und nicht Teil des Prozessnamens (Hinweis). |
| MP6 | Modell enthält nur einen Prozess, kein Mischmodell. | ☒ | ☐ | ☐ | Ein `process`-Element. |
| MP7 | Pool-Benennung korrekt? (Ggf. Externe über Blackbox/Whitebox-Pool kenntlich gemacht?) | ☐ | ☒ | ☐ | Pool `40-1 beispiele` (klein geschrieben, „beispiele", nur Geschäftszeichen). Externe (Kunde, Poststelle) nicht dargestellt. |
| MP8 | Mindestens eine Schwimmbahn (Lane) vorhanden und korrekt benannt? | ☐ | ☒ | ☐ | Zwei Lanes vorhanden; `2-2` ist keine zulässige Benennung. `40-1.1 SB Organisation` enthält die Abkürzung „SB". |
| MP9 | Prozessanalyst/-modellierer eingetragen? | ☐ | ☒ | ☐ | Im Export nicht nachweisbar. |
| MP10 | 17-3.4 ADONIS-Team als methodischer Prüfer eingetragen? | ☐ | ☒ | ☐ | Im Export nicht nachweisbar. |
| MP11 | Prozessmanager eingetragen? | ☐ | ☒ | ☐ | Im Export nicht nachweisbar. |
| MP12 | Prozesseigner eingetragen? | ☐ | ☒ | ☐ | Im Export nicht nachweisbar. |
| MP13 | Grobe Prozessbeschreibung vorhanden? (Beschreibung, Zweck, Auslöser, Ergebnis) | ☐ | ☒ | ☐ | Keine Beschreibung in den Modellattributen. |
| MP14 | Gültigkeitsdauer des Prozesses max. 11 Monate beachtet? | ☐ | ☒ | ☐ | „Gültig von/bis" nicht gepflegt. Status „In Bearbeitung", Version 0.01. |
| MP15 | Teilprozesse referenziert, aber noch nicht modelliert? | ☒ | ☐ | ☐ | Leerer Teilprozess vorhanden, aber nur generisch benannt („Teilprozess"). Eine Referenz auf einen konkreten Teilprozess ist nicht erkennbar. |

### Objektplatzierung & Sektoren

| MP-Nr. | Prüfkriterium | ✅ Ja | ❌ Nein | ➖ Nicht relevant | Bemerkung |
|---|---|:---:|:---:|:---:|---|
| MP16 | Lane vorhanden und Rolle zugewiesen? (Ressource) – Ausnahme: generische Rollen | ☐ | ☒ | ☐ | Lane 2 ohne erkennbare Rolle; keine Ressourcenzuordnung im Export. |
| MP17 | Rolle korrekt benannt? (Geschäftszeichen + Rolle) | ☐ | ☒ | ☐ | `40-1.1 SB Organisation` ungefähr konform (Abkürzung „SB"); `2-2` nicht konform. |
| MP18 | Pools korrekt angeordnet? (untereinander, nicht nebeneinander) | ☐ | ☐ | ☒ | Nur ein Pool vorhanden (siehe Kategorie 1). |

### Sequenzflüsse & Kanten

| MP-Nr. | Prüfkriterium | ✅ Ja | ❌ Nein | ➖ Nicht relevant | Bemerkung |
|---|---|:---:|:---:|:---:|---|
| MP19 | Sequenzflüsse konsistent, ohne Überlappungen, mit korrekten Kantenansatzpunkten. | ☐ | ☒ | ☐ | `_db38fb23…` und `_e005cd99…` haben identische Waypoints (vollständige Überlappung). `_8305513e…` und `_cb5daba9…` führen parallel zum selben Ziel. Langer Rücksprung-Fluss quer durch Lane 1. |
| MP20 | Nachrichtenflüsse zwischen Pools vorhanden? | ☐ | ☒ | ☐ | Keine `messageFlow`-Elemente. Erforderlich: Antrag (Kunde → Org), Nachforderung, Unterlagen, Bescheid/Ablehnung (Org → Kunde). |
| MP21 | Elemente in korrekten Sektoren platziert? | ☐ | ☒ | ☐ | Zuordnung nicht nachvollziehbar, da Lane 2 unbenannt. Die Poststelle wird in Tasknamen genannt, ist aber weder Lane noch Pool. Die Task `Antrag zur Erstellung des Ablehnungsschreibens…` (Lane 2) führt per Sequenzfluss in Lane 1 zurück. |

### Assoziationen & Datenzugriff

| MP-Nr. | Prüfkriterium | ✅ Ja | ❌ Nein | ➖ Nicht relevant | Bemerkung |
|---|---|:---:|:---:|:---:|---|
| MP22 | Assoziationen zeigen Verbindungen zu zusätzlichen Informationen wie Datenobjekten oder Notizen korrekt an. | ☐ | ☐ | ☒ | Keine Assoziationen/Datenobjekte vorhanden. |
| MP23 | IT-Systeme angegeben und korrekt benannt? (ggf. neue Systeme korrekt benennen) | ☐ | ☒ | ☐ | Keine Systeme referenziert, obwohl `in Datenbahn erheben` auf ein System hindeutet. |

### Größe & Detaillierung

| MP-Nr. | Prüfkriterium | ✅ Ja | ❌ Nein | ➖ Nicht relevant | Bemerkung |
|---|---|:---:|:---:|:---:|---|
| MP24 | Detailgrad einheitlich? (Modellierungstiefe, Anzahl der Prozessschritte? Ggfs. Subprozess) | ☐ | ☒ | ☐ | Reine Transportschritte (`An SB weiterleiten`) neben fachlichen Schritten; leerer, generisch benannter Teilprozess. |
| MP25 | Keine ausladenden Mehrfachaktivitäten in einer Aufgabe? (ggf. aufteilen) | ☐ | ☒ | ☐ | `Ablehnung Antrag, erstellen und verschicken` bündelt Erstellen und Versenden. |
| MP26 | Prozessoptik einheitlich? (Größe der Aufgaben, Pools, Lanes – Länge aller Pools und Lanes gleich) | ☒ | ☐ | ☐ | Tasks 151×76, Lanes 2189 px, Pool 2229 px einheitlich. Lane-Höhen unterschiedlich (417/379), Ereignisse 56×56 statt 36×36 laut Guidelines (Hinweis). |
| MP27 | „Happy Path/happy-day-szenario" abgebildet? (Ausnahmen in der Aufgabenbeschreibung abgebildet) | ☐ | ☒ | ☐ | Der Genehmigungspfad (`Förderung genehmigt` → Bescheid erstellen) endet an einem Gateway ohne Ausgang. Einziges Endereignis ist `Antrag abgelehnt`. |

### Benennung & Text

| MP-Nr. | Prüfkriterium | ✅ Ja | ❌ Nein | ➖ Nicht relevant | Bemerkung |
|---|---|:---:|:---:|:---:|---|
| MP28 | Ereignisse konventionengetreu benannt? (z. B. „Antrag eingegangen" = Substantiv + Verb) | ☒ | ☐ | ☐ | Alle Ereignisnamen konform. Hinweis: `Antrag eingegangen` wird für Start und für die interne Übergabe doppelt verwendet; `Auftrag eingegangen` ist uneinheitlich dazu. |
| MP29 | Ereignisse korrekt verwendet? | ☐ | ☒ | ☐ | Alle 6 Zwischen-Fangereignisse ohne Ereignisdefinition (Timer `2 Wochen verstrichen`, Nachricht `Unterlagen eingegangen` etc.). `Förderung genehmigt/abgelehnt` als ereignisbasierte Alternative nach dem Teilprozess: Das Ergebnis ist eine Entscheidung und kein externes Ereignis. Interne Übergaben zwischen Lanes als Zwischenereignisse (`Antrag eingegangen`, `Auftrag eingegangen`) modelliert. |
| MP30 | Aufgabenbezeichnung konventionengetreu? (Objekt + Verrichtung, kurz & prägnant) | ☐ | ☒ | ☐ | Siehe Tabelle „Task-Benennung" unten. |
| MP31 | Abkürzungen in Aufgaben sind in der Beschreibung erläutert. | ☐ | ☒ | ☐ | „SB" in `An SB weiterleiten` und im Lane-Namen nicht erläutert. |

**Task-Benennung**

| Aktuell | Befund | Vorschlag |
|---|---|---|
| `Antrag auf Vollständigkeit prüfen` | konform | – |
| `Unterlagen nachfordern` | konform | – |
| `An SB weiterleiten` | Objekt fehlt, Abkürzung | `Antrag an Sachbearbeitung weiterleiten` |
| `in Datenbahn erheben` | Kleinschreibung, Objekt fehlt, „Datenbahn" unklar | `Antragsdaten erheben` (Begriff mit Fachbereich klären) |
| `Teilprozess` (Subprozess) | generischer Name | Fachlichen Namen vergeben, z. B. `Förderantrag fachlich prüfen` |
| `Anttag zur Erstellung des Bescheides` | Tippfehler, zu lang | `Bescheid erstellen lassen` |
| `Antrag zur Erstellung des Ablehnungsschreibens an Poststelle` | zu lang | `Ablehnungsschreiben beauftragen` |
| `Ablehnung Antrag, erstellen und verschicken` | Wortfolge, Mehrfachaktivität | `Ablehnungsbescheid erstellen und versenden` |

### Verzweigungen & Gateways

| MP-Nr. | Prüfkriterium | ✅ Ja | ❌ Nein | ➖ Nicht relevant | Bemerkung |
|---|---|:---:|:---:|:---:|---|
| MP32 | Wird die Entscheidung, welcher Pfad genommen wird, in der Aktivität vor dem Gateway getroffen (und nicht im Gateway selbst)? | ☒ | ☐ | ☐ | `Antrag auf Vollständigkeit prüfen` → `Antrag vollständig?`. |
| MP33 | Gateways korrekt geöffnet und wenn nötig, ggf. geschlossen? | ☐ | ☒ | ☐ | Paralleles Gateway `Nicht-exklusives Gateway` (Richtung „Diverging") hat nur einen eingehenden und keinen ausgehenden Fluss. `Ablehnung…` hat zwei Eingänge ohne zusammenführendes Gateway (implizites Merge). |
| MP34 | Exklusive Gateways korrekt benannt? (Als Frage formuliert) | ☒ | ☐ | ☐ | `Antrag vollständig?`. |
| MP35 | Parallele und ereignisbasierte Gateways sind nicht beschriftet? | ☐ | ☒ | ☐ | Namen `Nicht-exklusives Gateway` und 2× `Exklusives Gateway` (bei ereignisbasierten Gateways inhaltlich falsch). Die Flüsse aus dem ereignisbasierten Gateway sind mit „Ja"/„Nein" beschriftet. |
| MP36 | Max. 5 ausgehende Sequenzflüsse pro Gateway, Entscheidungspfade beschriftet? (Nur bei exklusiven Gateways) | ☒ | ☐ | ☐ | `Antrag vollständig?` hat 2 beschriftete Pfade (Ja/Nein). |
| MP37 | Verzweigungen: Keine Deadlocks, Livelocks oder Multi-Merges vorhanden? | ☐ | ☒ | ☐ | Sackgasse am parallelen Gateway. Das ereignisbasierte Gateway nach dem Teilprozess hat doppelte Flüsse zu `Förderung abgelehnt` und `Förderung genehmigt`, die Ereignisse erhalten damit jeweils zwei Token (Multi-Merge-Risiko). |
| MP38 | Exklusive Gateways nicht verkettet? | ☒ | ☐ | ☐ | Keine Verkettung. |

### Sonderfälle & Entweder-Oder-Rückkopplung

| MP-Nr. | Prüfkriterium | ✅ Ja | ❌ Nein | ➖ Nicht relevant | Bemerkung |
|---|---|:---:|:---:|:---:|---|
| MP39 | Wiederholungen und Fehlerbehandlung korrekt umgesetzt? Keine Endlosschleifen ohne Fortschritt. | ☒ | ☐ | ☐ | Nachforderungsschleife hat einen Ausstieg über `2 Wochen verstrichen`. Der Rücksprung zu `Antrag auf Vollständigkeit prüfen` ist nachvollziehbar. |

### BPMN-Regelkonformität

| MP-Nr. | Prüfkriterium | ✅ Ja | ❌ Nein | ➖ Nicht relevant | Bemerkung |
|---|---|:---:|:---:|:---:|---|
| MP40 | Verwendung zulässiger BPMN-Elemente (nach aktuellem Modellierungsleitfaden der LHS) | ☐ | ☒ | ☐ | Fehlender Kunde-Pool/Nachrichtenflüsse, Fangereignisse ohne Typ, doppelte Sequenzflüsse, Gateway ohne Ausgang. |
| MP41 | Allgemeine Punkte zu DEMI, Wasserzeichen, Systeme/Produkte und Darstellung geprüft? | ☐ | ☐ | ☒ | Aus der Datei nicht belastbar prüfbar (Wasserzeichen deaktiviert, keine Systeme/Produkte referenziert). |

---

## Elementdokumentation (Documentation - Element documentation)

Prüfgrundlage: `.github/instructions/BPMN_Documentation.instructions.md`

| Task | Dokumentation | Befund |
|---|---|---|
| `Antrag auf Vollständigkeit prüfen` | vorhanden | Inhalt „Eingangsstempel / Arbeitsgebiet" sind Stichworte, keine Beschreibung von Zweck, Bearbeitung und Ergebnis; ohne `textFormat`. Position im XML korrekt (vor `extensionElements`). |
| `Unterlagen nachfordern` | fehlt | |
| `An SB weiterleiten` | fehlt | |
| `in Datenbahn erheben` | fehlt | |
| `Teilprozess` | fehlt | |
| `Anttag zur Erstellung des Bescheides` | fehlt | |
| `Antrag zur Erstellung des Ablehnungsschreibens an Poststelle` | fehlt | |
| `Ablehnung Antrag, erstellen und verschicken` | fehlt | |

Die Zuordnung des `documentation`-Elements zum ADONIS-Feld ist laut Instruktion ohne Import-/Exportprüfung unbestätigt. In dieser Datei ist das Element als `<documentation id="documentation_…">` mit CDATA vorhanden, was auf einen ADONIS-Export hindeutet.

---

## Empfehlungen

Priorisierte Liste der wichtigsten Änderungen für eine erfolgreiche Abnahme:

1. **Kunde-Pool ergänzen** (mindestens als Black-Box-Pool, besser White-Box mit Start-/Endereignis) und Nachrichtenflüsse für Antrag, Nachforderung, Unterlagen sowie Bescheid/Ablehnung modellieren. Das Startereignis leitet sich aus dem Kunden ab (KOI-/e2e-Prinzip).
2. **Genehmigungspfad schließen**: Paralleles Gateway nach `Anttag zur Erstellung des Bescheides` entfernen oder sinnvoll fortsetzen, Bescheid an den Kunden versenden und ein Endereignis (z. B. „Förderantrag bewilligt") ergänzen.
3. **Doppelte Sequenzflüsse entfernen** (`_e005cd99…` oder `_db38fb23…`; `_8305513e…` oder `_cb5daba9…`), damit jedes Ereignis nur einmal angebunden ist.
4. **Entscheidung nach dem Teilprozess überarbeiten**: Statt ereignisbasiertem Gateway mit „Förderung genehmigt/abgelehnt" ein exklusives Gateway als Frage („Förderung genehmigt?") mit Ja/Nein-Pfaden verwenden. Die Entscheidung wird im Teilprozess getroffen.
5. **Ereignisse typisieren**: `2 Wochen verstrichen` als Timer, `Unterlagen eingegangen` als Nachricht. Ja/Nein-Beschriftungen an den Flüssen aus dem ereignisbasierten Gateway entfernen. Gateway-Namen („Exklusives Gateway", „Nicht-exklusives Gateway") entfernen.
6. **Pool und Lanes korrekt benennen**: Pool (z. B. Organisation/Fachbereich), Lane `2-2` durch Geschäftszeichen + Rolle ersetzen, „SB" ausschreiben. Prüfen, ob die Poststelle als eigene Lane/Rolle dargestellt werden sollte.
7. **Aufgabenbezeichnungen korrigieren** (Tippfehler „Anttag", Objekt + Verrichtung, Kürzung) gemäß obiger Tabelle. `Teilprozess` fachlich benennen und referenzieren.
8. **Elementdokumentation ergänzen** für alle 7 Tasks und den Teilprozess (Zweck, Bearbeitung, Ergebnis); vorhandene Stichworte am Prüftask in einen vollständigen Text überführen.
9. **Layout bereinigen**: Rückwärtsflüsse vermeiden (`Auftrag eingegangen` links vom Ergebnis platzieren oder per Nachrichtenfluss lösen), Elemente von links nach rechts anordnen, Lane-Höhen angleichen.
10. **Modellmetadaten pflegen**: Prozessanalyst/-modellierer, ADONIS-Team als methodischer Prüfer, Prozessmanager, Prozesseigner, Prozessbeschreibung (Beschreibung, Zweck, Auslöser, Ergebnis), Gültigkeitsdauer (max. 11 Monate). Personenbezug im Änderungsverlauf klären.
11. **IT-Unterstützung prüfen** (optional): Systeme für `in Datenbahn erheben` und die Bescheiderstellung an den Tasks referenzieren oder einen IT-Pool ergänzen.

---

## Ergebnis

- [ ] **Abnahme erteilt** – Modell entspricht allen Anforderungen
- [ ] **Abnahme mit Auflagen** – Modell wird bedingt akzeptiert, Auflagen sind umzusetzen
- [x] **Abnahme verweigert** – Kritische Fehler müssen vor Wiedervorlage behoben werden

> Für die Remodellierung bitte den entsprechenden Remodellierungsagenten auswählen.
