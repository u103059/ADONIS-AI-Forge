# Prüfbericht: `[Name des Prozessmodells]`

> **Datei**: `[Dateiname.bpmn]`
> **ADONIS-Modell-ID / Version**: `[ID]` / `[Version]` (nur bei Abruf aus ADONIS)
> **Geprüft am**: `[TT.MM.JJJJ]`
> **Geprüft durch**: GovModeler_ADONIS_Review

---

## Zusammenfassung

| Kriterium | Ergebnis |
|---|---|
| **Gesamtbewertung** | `Bestanden` / `Bestanden mit Hinweisen` / `Nachbesserung erforderlich` |
| **Kritische Fehler** | `[Anzahl]` |
| **Warnungen** | `[Anzahl]` |
| **Hinweise** | `[Anzahl]` |

---

## 1. Pool-Struktur und Akteure

| Kriterium | Status | Befund |
|---|---|---|
| **Kunde-Pool** vorhanden (White- oder Black-Box) | `✅` / `❌` / `⚠️` | |
| **Organisation-Pool** vorhanden | `✅` / `❌` / `⚠️` | |
| **IT-Pool** (optional, bewertet falls vorhanden) | `✅` / `➖` / `⚠️` | |

**Bewertung**: `[Kurze Einschätzung zur Akteursmodellierung]`

---

## 2. Prozessumfang und Verständlichkeit

**Schrittanzahl pro Pool**:

| Pool | Anzahl Tasks | Anzahl Gateways | Anzahl Events |
|---|---|---|---|
| Kunde | | | |
| Organisation | | | |
| IT | | | |

**Verständlichkeit**: `[Bewertung der Lesbarkeit und Nachvollziehbarkeit des Modells]`

**Empfehlungen zur Kompaktheit**: `[Vorschläge zur Bündelung von Aktivitäten oder Nutzung von Subprozessen]`

---

## Detaillierte Befunde

> **Legende**: ✅ Ja – Kriterium erfüllt | ❌ Nein – Kriterium verletzt | ➖ Nicht relevant

### Allgemeine Struktur

| MP-Nr. | Prüfkriterium | ✅ Ja | ❌ Nein | ➖ Nicht relevant | Bemerkung |
|---|---|:---:|:---:|:---:|---|
| MP1 | Enthält der Prozess keine personenbezogenen Daten? | ☐ | ☐ | ☐ | |
| MP2 | Ist der Prozess in der richtigen Ablagestruktur? | ☐ | ☐ | ☐ | |
| MP3 | Enthält der Prozess keine vertraulichen oder höher eingestuften Inhalte? | ☐ | ☐ | ☐ | |
| MP4 | Modellierungsrichtung einheitlich? (von links nach rechts bei BPMN) | ☐ | ☐ | ☐ | |
| MP5 | Ist der Prozessname aussagekräftig, enthält keine Abkürzungen und Paragrafen? | ☐ | ☐ | ☐ | |
| MP6 | Modell enthält nur einen Prozess, kein Mischmodell. | ☐ | ☐ | ☐ | |
| MP7 | Pool-Benennung korrekt? (Ggf. Externe über Blackbox/Whitebox-Pool kenntlich gemacht?) | ☐ | ☐ | ☐ | |
| MP8 | Mindestens eine Schwimmbahn (Lane) vorhanden und korrekt benannt? | ☐ | ☐ | ☐ | |
| MP9 | Prozessanalyst/-modellierer eingetragen? | ☐ | ☐ | ☐ | |
| MP10 | 17-3.4 ADONIS-Team als methodischer Prüfer eingetragen? | ☐ | ☐ | ☐ | |
| MP11 | Prozessmanager eingetragen? | ☐ | ☐ | ☐ | |
| MP12 | Prozesseigner eingetragen? | ☐ | ☐ | ☐ | |
| MP13 | Grobe Prozessbeschreibung vorhanden? (Beschreibung, Zweck, Auslöser, Ergebnis) | ☐ | ☐ | ☐ | |
| MP14 | Gültigkeitsdauer des Prozesses max. 11 Monate beachtet? | ☐ | ☐ | ☐ | |
| MP15 | Teilprozesse referenziert, aber noch nicht modelliert? | ☐ | ☐ | ☐ | |

### Objektplatzierung & Sektoren

| MP-Nr. | Prüfkriterium | ✅ Ja | ❌ Nein | ➖ Nicht relevant | Bemerkung |
|---|---|:---:|:---:|:---:|---|
| MP16 | Lane vorhanden und Rolle zugewiesen? (Ressource) – Ausnahme: generische Rollen | ☐ | ☐ | ☐ | |
| MP17 | Rolle korrekt benannt? (Geschäftszeichen + Rolle) | ☐ | ☐ | ☐ | |
| MP18 | Pools korrekt angeordnet? (untereinander, nicht nebeneinander) | ☐ | ☐ | ☐ | |

### Sequenzflüsse & Kanten

| MP-Nr. | Prüfkriterium | ✅ Ja | ❌ Nein | ➖ Nicht relevant | Bemerkung |
|---|---|:---:|:---:|:---:|---|
| MP19 | Sequenzflüsse konsistent, ohne Überlappungen, mit korrekten Kantenansatzpunkten. | ☐ | ☐ | ☐ | |
| MP20 | Nachrichtenflüsse zwischen Pools vorhanden? | ☐ | ☐ | ☐ | |
| MP21 | Elemente in korrekten Sektoren platziert? | ☐ | ☐ | ☐ | |

### Assoziationen & Datenzugriff

| MP-Nr. | Prüfkriterium | ✅ Ja | ❌ Nein | ➖ Nicht relevant | Bemerkung |
|---|---|:---:|:---:|:---:|---|
| MP22 | Assoziationen zeigen Verbindungen zu zusätzlichen Informationen wie Datenobjekten oder Notizen korrekt an. | ☐ | ☐ | ☐ | |
| MP23 | IT-Systeme angegeben und korrekt benannt? (ggf. neue Systeme korrekt benennen) | ☐ | ☐ | ☐ | |

### Größe & Detaillierung

| MP-Nr. | Prüfkriterium | ✅ Ja | ❌ Nein | ➖ Nicht relevant | Bemerkung |
|---|---|:---:|:---:|:---:|---|
| MP24 | Detailgrad einheitlich? (Modellierungstiefe, Anzahl der Prozessschritte? Ggfs. Subprozess) | ☐ | ☐ | ☐ | |
| MP25 | Keine ausladenden Mehrfachaktivitäten in einer Aufgabe? (ggf. aufteilen) | ☐ | ☐ | ☐ | |
| MP26 | Prozessoptik einheitlich? (Größe der Aufgaben, Pools, Lanes – Länge aller Pools und Lanes gleich) | ☐ | ☐ | ☐ | |
| MP27 | „Happy Path/happy-day-szenario" abgebildet? (Ausnahmen in der Aufgabenbeschreibung abgebildet) | ☐ | ☐ | ☐ | |

### Benennung & Text

| MP-Nr. | Prüfkriterium | ✅ Ja | ❌ Nein | ➖ Nicht relevant | Bemerkung |
|---|---|:---:|:---:|:---:|---|
| MP28 | Ereignisse konventionengetreu benannt? (z. B. „Antrag eingegangen" = Substantiv + Verb) | ☐ | ☐ | ☐ | |
| MP29 | Ereignisse korrekt verwendet? | ☐ | ☐ | ☐ | |
| MP30 | Aufgabenbezeichnung konventionengetreu? (Objekt + Verrichtung, kurz & prägnant) | ☐ | ☐ | ☐ | |
| MP31 | Abkürzungen in Aufgaben sind in der Beschreibung erläutert. | ☐ | ☐ | ☐ | |

### Verzweigungen & Gateways

| MP-Nr. | Prüfkriterium | ✅ Ja | ❌ Nein | ➖ Nicht relevant | Bemerkung |
|---|---|:---:|:---:|:---:|---|
| MP32 | Wird die Entscheidung, welcher Pfad genommen wird, in der Aktivität vor dem Gateway getroffen (und nicht im Gateway selbst)? | ☐ | ☐ | ☐ | |
| MP33 | Gateways korrekt geöffnet und wenn nötig, ggf. geschlossen? | ☐ | ☐ | ☐ | |
| MP34 | Exklusive Gateways korrekt benannt? (Als Frage formuliert) | ☐ | ☐ | ☐ | |
| MP35 | Parallele und ereignisbasierte Gateways sind nicht beschriftet? | ☐ | ☐ | ☐ | |
| MP36 | Max. 5 ausgehende Sequenzflüsse pro Gateway, Entscheidungspfade beschriftet? (Nur bei exklusiven Gateways) | ☐ | ☐ | ☐ | |
| MP37 | Verzweigungen: Keine Deadlocks, Livelocks oder Multi-Merges vorhanden? (Deadlock = Prozess steht still, weil Bedingungen nie eintreten; Livelock = Prozess dreht sich im Kreis ohne Austrittsbedingung; Multi-Merge = Prozess läuft mehrfach zusammen, obwohl nur einmal gedacht) | ☐ | ☐ | ☐ | |
| MP38 | Exklusive Gateways nicht verkettet? | ☐ | ☐ | ☐ | |

### Sonderfälle & Entweder-Oder-Rückkopplung

| MP-Nr. | Prüfkriterium | ✅ Ja | ❌ Nein | ➖ Nicht relevant | Bemerkung |
|---|---|:---:|:---:|:---:|---|
| MP39 | Wiederholungen und Fehlerbehandlung korrekt umgesetzt? Keine Endlosschleifen ohne Fortschritt. | ☐ | ☐ | ☐ | |

### BPMN-Regelkonformität

| MP-Nr. | Prüfkriterium | ✅ Ja | ❌ Nein | ➖ Nicht relevant | Bemerkung |
|---|---|:---:|:---:|:---:|---|
| MP40 | Verwendung zulässiger BPMN-Elemente (nach aktuellem Modellierungsleitfaden der LHS) | ☐ | ☐ | ☐ | |
| MP41 | Allgemeine Punkte zu DEMI, Wasserzeichen, Systeme/Produkte und Darstellung geprüft? | ☐ | ☐ | ☐ | |

---

## Empfehlungen

Priorisierte Liste der wichtigsten Änderungen für eine erfolgreiche Abnahme:

1. **[Wichtigste Empfehlung]** – `[Begründung]`
2. **[Zweitwichtigste Empfehlung]** – `[Begründung]`
3. `[Weitere Empfehlungen...]`

---

## Ergebnis

- [ ] **Abnahme erteilt** – Modell entspricht allen Anforderungen
- [ ] **Abnahme mit Auflagen** – Modell wird bedingt akzeptiert, Auflagen sind umzusetzen
- [ ] **Abnahme verweigert** – Kritische Fehler müssen vor Wiedervorlage behoben werden
