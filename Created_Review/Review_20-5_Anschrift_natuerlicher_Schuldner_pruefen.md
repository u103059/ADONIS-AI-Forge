# Prüfbericht: `20-5 Anschrift natürlicher Schuldner prüfen`

> **Datei**: `20-5 Anschrift natürlicher Schuldner prüfen (de).bpmn`
> **Geprüft am**: `05.11.2026`
> **Geprüft durch**: GovModeler_ADONIS_Review

---

## Zusammenfassung

| Kriterium | Ergebnis |
|---|---|
| **Gesamtbewertung** | `Nachbesserung erforderlich` |
| **Kritische Fehler** | `1` |
| **Warnungen** | `9` |
| **Hinweise** | `8` |

**Kritischer Fehler**
1. Kein Kunde-Pool und keine Nachrichtenflüsse (Pflicht). Start- und Endereignisse leiten sich nicht vom Kunden ab; die Kommunikation mit Dritten (Eingang des Dokuments, Information der Stadtkasse) ist nicht dargestellt.

**Warnungen**
1. Gateway `neue Anschrift bekannt?` führt zwei Zweige zusammen und verzweigt gleichzeitig (gemischtes Gateway, `gatewayDirection` fehlt).
2. Elementdokumentation: 1 von 12 Tasks ohne Dokumentation, die übrigen 11 enthalten nur Stichworte bzw. Systemnamen.
3. Abkürzungen (KM-EwO, AZR, BZR, DRV, Dt RV, SAP, SB, AbtL, evtl., Ggf.) sind nicht erläutert.
4. Aufgabenbezeichnungen teilweise nicht konventionengetreu (Schreibweise, „Ggf.", Wortfolge, „Ermittlungsarten").
5. Endereignisse: 5 Stück mit teils identischem Namen, uneinheitliche Schreibweise (Singular/Plural), „(evtl. …)" im Ereignisnamen.
6. Gateway-Fragen `Treffen die Angaben zu?` (2×) sind unspezifisch und doppelt vergeben.
7. IT-Systeme: Meldeportal und SAP werden in den Beschreibungen genannt, aber nicht als IT-System an den Tasks referenziert.
8. Grobe Prozessbeschreibung (Beschreibung, Zweck, Auslöser, Ergebnis) nicht gepflegt.
9. Methodischer Prüfer (17-3.4 ADONIS-Team) im Export nicht nachweisbar.

**Hinweise**
1. Personenbezug im Änderungsverlauf (`MFB_RWF_HISTORY`).
2. Gültigkeitsdauer (Gültig von/bis) nicht gepflegt.
3. Ereignisse sind 56×56 px statt 36×36 px (Guidelines).
4. Kantenansatz an Gateways: Sequenzflüsse beginnen 37–50 px unterhalb der Gateway-Form (vermutlich Darstellung „Name unten"); am Gateway `neue Anschrift bekannt?` laufen Ein- und Ausgang nur 19 px parallel nebeneinander.
5. Fachliche Überschneidung zwischen `Deutsche Adresse prüfen` (Meldeportal) und `Anschrift über das Meldeportal prüfen`.
6. Doppelt modellierte, identische Schritte (`Wegzugsangaben prüfen`, `Weitere Ermittlungsarten prüfen`, `Ggf. Daten in avviso ergänzen`) sind konsolidierbar.
7. Lane-Name (`20-5 Sachbearbeiter Innendienst`) und Rollen-Name (`20-5 SB Innendienst`) weichen voneinander ab.
8. IT-Pool optional: signifikante IT-Unterstützung vorhanden (siehe Kategorie 1).

---

## 1. Pool-Struktur und Akteure

| Kriterium | Status | Befund |
|---|---|---|
| **Kunde-Pool** vorhanden (White- oder Black-Box) | ❌ | Die Collaboration enthält nur einen Participant (`20 Stadtkämmerei`). Kein Kunde-Pool, keine `messageFlow`-Elemente. Das Startereignis `Dokument mit falscher Anschrift ist eingegangen` liegt in der Organisation. |
| **Organisation-Pool** vorhanden | ✅ | Pool `20 Stadtkämmerei` (Geschäftszeichen + Organisation) mit einer Lane `20-5 Sachbearbeiter Innendienst`, Ressource `20-5 SB Innendienst`. |
| **IT-Pool** (optional, bewertet falls vorhanden) | ➖ | Nicht vorhanden, nicht zwingend. Die Systeme KM-EwO, avviso, DRV und E-Mail (Notes) sind bereits an den Tasks referenziert. Hinweis: Bei den Systemwechseln (Papierdokument → KM-EwO/Meldeportal/avviso → E-Mail) wäre ein IT-Pool oder die vollständige Referenzierung (Meldeportal, SAP) sinnvoll. |

**Bewertung**: Die Organisation ist sauber als Pool mit Lane und Rolle abgebildet. Die Kundenperspektive fehlt vollständig. Der Prozess wird durch ein eingehendes Dokument ausgelöst; wer das Dokument sendet (anfragende Stelle bzw. Absender), ist nicht dargestellt. Ebenso fehlt der Empfänger der Information am Prozessende (Stadtkasse/Geschäftspartner-Stammdaten per E-Mail). Wer im konkreten Fall der „Kunde" ist (interne anfragende Stelle oder externer Absender), ist mit dem Fachbereich zu klären.

---

## 2. Prozessumfang und Verständlichkeit

**Schrittanzahl pro Pool**:

| Pool | Anzahl Tasks | Anzahl Gateways | Anzahl Events |
|---|---|---|---|
| Kunde | 0 (Pool fehlt) | 0 | 0 |
| Organisation (`20 Stadtkämmerei`, 1 Lane) | 12 | 5 (alle exklusiv) | 6 (1 Start, 5 Ende) |
| IT | 0 (nicht vorhanden) | 0 | 0 |

Gesamt: 23 Flow-Nodes, 23 Sequenzflüsse, alle der Lane zugeordnet.

**Verständlichkeit**: Der Prozess ist übersichtlich in drei Zeilen angeordnet (Stuttgart / Deutschland / Ausland bzw. Weitere Ermittlung) und verläuft von links nach rechts. Alle Pfade enden in einem Endereignis, es gibt keine Sackgassen oder Schleifen. Die Lesbarkeit leidet an: (a) fünf Endereignissen mit nahezu gleichen Namen, (b) zwei Gateways mit identischer Frage `Treffen die Angaben zu?`, (c) dem gemischten Gateway `neue Anschrift bekannt?`, in dem zwei Zweige zusammenlaufen und neu verzweigen, (d) Stichwort-Dokumentation ohne erläuterte Abkürzungen.

**Empfehlungen zur Kompaktheit** (ohne Reduzierung der Schritte):
- Die identischen Schritte `Ggf. Daten in avviso ergänzen` (2×) und `Weitere Ermittlungsarten prüfen` (2×) können über ein vorgeschaltetes zusammenführendes exklusives Gateway je einmal modelliert werden; gleiches gilt für die gleichlautenden Endereignisse. Dies ist ein Gestaltungsvorschlag, keine Pflicht.
- `Weitere Ermittlungsarten prüfen` bündelt AZR, BZR und DRV in einem Task. Die Bündelung ist vertretbar; die Einzelquellen in der Elementdokumentation erläutern.
- Die Entscheidung `Wohnt Schuldner in Stuttgart?` / `Wohnt der Schuldner in Deutschland?` kann bei Bedarf als Subprozess „Wohnort des Schuldners ermitteln" gebündelt werden, falls die Prüfschritte weiter detailliert werden.

---

## Detaillierte Befunde

> **Legende**: ✅ Ja – Kriterium erfüllt | ❌ Nein – Kriterium verletzt | ➖ Nicht relevant

### Allgemeine Struktur

| MP-Nr. | Prüfkriterium | ✅ Ja | ❌ Nein | ➖ Nicht relevant | Bemerkung |
|---|---|:---:|:---:|:---:|---|
| MP1 | Enthält der Prozess keine personenbezogenen Daten? | ☐ | ☒ | ☐ | Der Änderungsverlauf (`MFB_RWF_HISTORY`) enthält Name und Benutzerkennung der bearbeitenden Person (2 Einträge). Systemmetadaten, aber personenbezogen; vor Abnahme/Veröffentlichung klären. In der Dokumentation stehen nur Funktionspostfächer der Poststelle (kein Personenbezug). |
| MP2 | Ist der Prozess in der richtigen Ablagestruktur? | ☐ | ☐ | ☒ | Aus der Datei nicht prüfbar. |
| MP3 | Enthält der Prozess keine vertraulichen oder höher eingestuften Inhalte? | ☒ | ☐ | ☐ | Keine entsprechenden Inhalte erkennbar. |
| MP4 | Modellierungsrichtung einheitlich? (von links nach rechts bei BPMN) | ☒ | ☐ | ☐ | Alle Sequenzflüsse laufen von links nach rechts bzw. nach unten/oben zu einem rechts liegenden Ziel; keine Rückwärtsflüsse. |
| MP5 | Ist der Prozessname aussagekräftig, enthält keine Abkürzungen und Paragrafen? | ☒ | ☐ | ☐ | „Anschrift natürlicher Schuldner prüfen" ist aussagekräftig; „20-5" ist das Geschäftszeichen. |
| MP6 | Modell enthält nur einen Prozess, kein Mischmodell. | ☒ | ☐ | ☐ | Ein `process`-Element. |
| MP7 | Pool-Benennung korrekt? (Ggf. Externe über Blackbox/Whitebox-Pool kenntlich gemacht?) | ☐ | ☒ | ☐ | Pool `20 Stadtkämmerei` ist korrekt benannt. Externe Beteiligte (Absender des Dokuments, Stadtkasse/Geschäftspartner, Poststelle) sind nicht kenntlich gemacht. |
| MP8 | Mindestens eine Schwimmbahn (Lane) vorhanden und korrekt benannt? | ☒ | ☐ | ☐ | Lane `20-5 Sachbearbeiter Innendienst`. |
| MP9 | Prozessanalyst/-modellierer eingetragen? | ☒ | ☐ | ☐ | `RC_ANALYST`: `20 Prozessanalyse/-modellierung`. |
| MP10 | 17-3.4 ADONIS-Team als methodischer Prüfer eingetragen? | ☐ | ☒ | ☐ | Im Export nicht nachweisbar (Status steht auf `In methodischer Prüfung`). |
| MP11 | Prozessmanager eingetragen? | ☒ | ☐ | ☐ | `RC_MANAGER`: `20-5 AbtL` (Abkürzung „AbtL" ausschreiben bzw. erläutern). |
| MP12 | Prozesseigner eingetragen? | ☒ | ☐ | ☐ | `RC_OWNER`: `20-5 AbtL`. |
| MP13 | Grobe Prozessbeschreibung vorhanden? (Beschreibung, Zweck, Auslöser, Ergebnis) | ☐ | ☒ | ☐ | Keine Beschreibung in den Modellattributen. Inhaltlich ableitbar: Auslöser = Dokument mit falscher Anschrift eingegangen; Ergebnis = Anschrift und Daten geprüft, ggf. neue Anschrift erfasst und Stadtkasse informiert. |
| MP14 | Gültigkeitsdauer des Prozesses max. 11 Monate beachtet? | ☐ | ☒ | ☐ | `Gültig von` / `Gültig bis` nicht gepflegt. Version 1.01, Status `In methodischer Prüfung`. Bei Freigabe max. 11 Monate setzen. |
| MP15 | Teilprozesse referenziert, aber noch nicht modelliert? | ☐ | ☐ | ☒ | Keine Teilprozesse vorhanden. |

### Objektplatzierung & Sektoren

| MP-Nr. | Prüfkriterium | ✅ Ja | ❌ Nein | ➖ Nicht relevant | Bemerkung |
|---|---|:---:|:---:|:---:|---|
| MP16 | Lane vorhanden und Rolle zugewiesen? (Ressource) – Ausnahme: generische Rollen | ☒ | ☐ | ☐ | Lane mit `RC_RESOURCE` auf `20-5 SB Innendienst`; alle 12 Tasks haben `RESPONSIBLE_FOR_EXECUTION` auf dieselbe Rolle. |
| MP17 | Rolle korrekt benannt? (Geschäftszeichen + Rolle) | ☒ | ☐ | ☐ | Geschäftszeichen + Rolle vorhanden. Hinweis: Rolle enthält „SB", die Lane `Sachbearbeiter`; Schreibweise angleichen. |
| MP18 | Pools korrekt angeordnet? (untereinander, nicht nebeneinander) | ☐ | ☐ | ☒ | Nur ein Pool. Nach Ergänzung des Kunde-Pools über dem Organisation-Pool anordnen. |

### Sequenzflüsse & Kanten

| MP-Nr. | Prüfkriterium | ✅ Ja | ❌ Nein | ➖ Nicht relevant | Bemerkung |
|---|---|:---:|:---:|:---:|---|
| MP19 | Sequenzflüsse konsistent, ohne Überlappungen, mit korrekten Kantenansatzpunkten. | ☒ | ☐ | ☐ | Keine Überlappungen. Hinweis: Flüsse am Gateway-Unterrand beginnen 37–50 px unterhalb der Form (Darstellung „Name unten", beim Import in ADONIS prüfen). Am Gateway `neue Anschrift bekannt?` verlaufen Eingang (x=1401) und Ausgang `Nein` (x=1420) nur 19 px nebeneinander, beide am Unterrand. |
| MP20 | Nachrichtenflüsse zwischen Pools vorhanden? | ☐ | ☒ | ☐ | Keine `messageFlow`-Elemente. Erforderlich: Dokumenteingang (Kunde → Organisation) und ggf. Information der Stadtkasse (Organisation → Stadtkasse). |
| MP21 | Elemente in korrekten Sektoren platziert? | ☒ | ☐ | ☐ | Alle 23 Elemente liegen in der einzigen Lane. `Bei SAP- Geschäftspartnern Stadtkasse informieren` ist eine Kommunikation an eine externe Stelle (siehe MP20). |

### Assoziationen & Datenzugriff

| MP-Nr. | Prüfkriterium | ✅ Ja | ❌ Nein | ➖ Nicht relevant | Bemerkung |
|---|---|:---:|:---:|:---:|---|
| MP22 | Assoziationen zeigen Verbindungen zu zusätzlichen Informationen wie Datenobjekten oder Notizen korrekt an. | ☐ | ☐ | ☒ | Keine Assoziationen/Datenobjekte vorhanden. |
| MP23 | IT-Systeme angegeben und korrekt benannt? (ggf. neue Systeme korrekt benennen) | ☐ | ☒ | ☐ | Referenziert: `KM-EwO` (Tasks `Eintrag in KM- Ewo prüfen`, `Wegzugsangaben prüfen`), `20 Avviso`, `20 DRV`, `E-Mail (Notes)`. Nicht referenziert: Meldeportal (3 Tasks: `Deutsche Adresse prüfen`, `Anschrift über das Meldeportal prüfen`, `Wegzugsangaben prüfen`) und SAP (`Bei SAP- Geschäftspartnern Stadtkasse informieren`). `Postvermerk auf Dokument prüfen` ohne System (Papier/Dokument ggf. korrekt). `Deutsche Adresse prüfen` ist mit avviso referenziert (BZR). |

### Größe & Detaillierung

| MP-Nr. | Prüfkriterium | ✅ Ja | ❌ Nein | ➖ Nicht relevant | Bemerkung |
|---|---|:---:|:---:|:---:|---|
| MP24 | Detailgrad einheitlich? (Modellierungstiefe, Anzahl der Prozessschritte? Ggfs. Subprozess) | ☒ | ☐ | ☐ | Einheitliche Tiefe (12 Tasks, alle fachlich). Hinweis: Überschneidung `Deutsche Adresse prüfen` (Meldeportal, BZR) und `Anschrift über das Meldeportal prüfen` (Meldeportal) fachlich klären; identische Schritte doppelt modelliert (siehe Kompaktheit). |
| MP25 | Keine ausladenden Mehrfachaktivitäten in einer Aufgabe? (ggf. aufteilen) | ☒ | ☐ | ☐ | Hinweis: `Weitere Ermittlungsarten prüfen` bündelt AZR, BZR und DRV; `Deutsche Adresse prüfen` Meldeportal und BZR. Als Bündelung vertretbar, Einzelquellen in der Dokumentation beschreiben. |
| MP26 | Prozessoptik einheitlich? (Größe der Aufgaben, Pools, Lanes – Länge aller Pools und Lanes gleich) | ☒ | ☐ | ☐ | Tasks 151×76, Gateways 56×56, Pool 2041 px = Lane 40 + 2001 px, Höhe je 719 px. Ereignisse 56×56 statt 36×36 (Hinweis). Wasserzeichen: Lane `true`, Pool `false` (uneinheitlich, siehe MP41). |
| MP27 | „Happy Path/happy-day-szenario" abgebildet? (Ausnahmen in der Aufgabenbeschreibung abgebildet) | ☒ | ☐ | ☐ | Happy Path erkennbar: Postvermerk prüfen → Wohnort Stuttgart → KM-EwO-Eintrag prüfen → Angaben treffen zu → Daten ergänzen → Ende. Ausnahmen (Wegzug, andere Wohnorte, Ermittlung) sind zusätzlich vollständig abgebildet. |

### Benennung & Text

| MP-Nr. | Prüfkriterium | ✅ Ja | ❌ Nein | ➖ Nicht relevant | Bemerkung |
|---|---|:---:|:---:|:---:|---|
| MP28 | Ereignisse konventionengetreu benannt? (z. B. „Antrag eingegangen" = Substantiv + Verb) | ☐ | ☒ | ☐ | Start `Dokument mit falscher Anschrift ist eingegangen` konform. Enden: `Anschriften und Daten sind geprüft` (2×, plural), `Anschrift und Daten sind geprüft` (Singular, uneinheitlich), `Anschriften und Daten sind geprüft (evtl. keine aktuelle Anschrift bekannt)` (2×; „evtl." und Klammerzusatz, mehrdeutiges Ergebnis). Der Endzustand nach „neue Anschrift erfasst und Stadtkasse informiert" heißt wie der Endzustand ohne Änderung. |
| MP29 | Ereignisse korrekt verwendet? | ☐ | ☒ | ☐ | Startereignis ist ein Eingang eines Dokuments (Nachricht), aber ohne Ereignistyp und ohne Nachrichtenfluss vom Kunden. Endereignisse ohne Ergebnistyp sind zulässig. |
| MP30 | Aufgabenbezeichnung konventionengetreu? (Objekt + Verrichtung, kurz & prägnant) | ☐ | ☒ | ☐ | Siehe Tabelle „Task-Benennung" unten. |
| MP31 | Abkürzungen in Aufgaben sind in der Beschreibung erläutert. | ☐ | ☒ | ☐ | Nicht erläutert: `KM-EwO`/`KM- Ewo`, `SAP`, `AZR`, `BZR`, `DRV`, `Dt RV`, `SB` (Rolle), `AbtL`, `evtl.`, `Ggf.`, `Z.B.`. |

**Task-Benennung**

| Aktuell | Befund | Vorschlag |
|---|---|---|
| `Postvermerk auf Dokument prüfen` | konform | – |
| `Eintrag in KM- Ewo prüfen` | Leerzeichen im Systemnamen, Schreibweise weicht von `KM-EwO` ab | `Eintrag in KM-EwO prüfen` |
| `Wegzugsangaben prüfen` (2×) | konform; Namensgleichheit, Unterscheidung nur über Beschreibung (KM-EwO bzw. Meldeportal) | beibehalten oder System in der Beschreibung ergänzen |
| `Deutsche Adresse prüfen` | konform; fachlich zu `Anschrift über das Meldeportal prüfen` abgrenzen | – |
| `Anschrift über das Meldeportal prüfen` | konform | – |
| `Weitere Ermittlungsarten prüfen` (2×) | „Ermittlungsarten" ist kein Objekt | z. B. `Anschrift über weitere Quellen ermitteln` (Begriff mit Fachbereich klären) |
| `Ggf. Daten in avviso ergänzen` (2×) | Abkürzung „Ggf.", Bedingung im Namen, System im Namen | `Daten in avviso ergänzen` (Bedingung in der Beschreibung) |
| `Neue Anschrift in avviso erfassen` | konform | – |
| `Bei SAP- Geschäftspartnern Stadtkasse informieren` | Wortfolge, Leerzeichen, Abkürzung | `Stadtkasse über neue Anschrift informieren` |

### Verzweigungen & Gateways

| MP-Nr. | Prüfkriterium | ✅ Ja | ❌ Nein | ➖ Nicht relevant | Bemerkung |
|---|---|:---:|:---:|:---:|---|
| MP32 | Wird die Entscheidung, welcher Pfad genommen wird, in der Aktivität vor dem Gateway getroffen (und nicht im Gateway selbst)? | ☒ | ☐ | ☐ | Jedem Gateway geht ein Prüf-Task voraus. |
| MP33 | Gateways korrekt geöffnet und wenn nötig, ggf. geschlossen? | ☐ | ☒ | ☐ | `neue Anschrift bekannt?` hat 2 Eingänge (`Wegzugsangaben prüfen` aus KM-EwO und aus Meldeportal) und 2 Ausgänge; kein `gatewayDirection`-Attribut. Empfehlung: Zusammenführung und Entscheidung trennen oder Zweige vor dem Gateway über ein zusammenführendes Gateway verbinden. |
| MP34 | Exklusive Gateways korrekt benannt? (Als Frage formuliert) | ☒ | ☐ | ☐ | Alle 5 als Frage formuliert. Hinweis: `Treffen die Angaben zu?` (2×) präzisieren, z. B. „Stimmt die Anschrift?". |
| MP35 | Parallele und ereignisbasierte Gateways sind nicht beschriftet? | ☐ | ☐ | ☒ | Keine parallelen oder ereignisbasierten Gateways. |
| MP36 | Max. 5 ausgehende Sequenzflüsse pro Gateway, Entscheidungspfade beschriftet? (Nur bei exklusiven Gateways) | ☒ | ☐ | ☐ | Je 2 ausgehende Flüsse, alle mit `Ja`/`Nein` beschriftet. |
| MP37 | Verzweigungen: Keine Deadlocks, Livelocks oder Multi-Merges vorhanden? | ☒ | ☐ | ☐ | Alle Pfade enden in einem Endereignis, keine Schleifen. Das gemischte Gateway ist ein exklusiver Merge, kein Multi-Merge. |
| MP38 | Exklusive Gateways nicht verkettet? | ☒ | ☐ | ☐ | Zwischen allen Gateways liegt ein Task. |

### Sonderfälle & Entweder-Oder-Rückkopplung

| MP-Nr. | Prüfkriterium | ✅ Ja | ❌ Nein | ➖ Nicht relevant | Bemerkung |
|---|---|:---:|:---:|:---:|---|
| MP39 | Wiederholungen und Fehlerbehandlung korrekt umgesetzt? Keine Endlosschleifen ohne Fortschritt. | ☐ | ☐ | ☒ | Keine Wiederholungen/Schleifen. |

### BPMN-Regelkonformität

| MP-Nr. | Prüfkriterium | ✅ Ja | ❌ Nein | ➖ Nicht relevant | Bemerkung |
|---|---|:---:|:---:|:---:|---|
| MP40 | Verwendung zulässiger BPMN-Elemente (nach aktuellem Modellierungsleitfaden der LHS) | ☒ | ☐ | ☐ | Es werden nur Task, exklusives Gateway, Start- und Endereignis, Sequenzfluss, Pool und Lane verwendet. Fehlende Pools/Nachrichtenflüsse siehe Kategorie 1. |
| MP41 | Allgemeine Punkte zu DEMI, Wasserzeichen, Systeme/Produkte und Darstellung geprüft? | ☐ | ☐ | ☒ | DEMI nicht aus der Datei prüfbar. Wasserzeichen: Lane `A_DISPLAY_WATERMARK = true`, Pool `false`, vor Abnahme vereinheitlichen. Produkte nicht referenziert. Systeme siehe MP23. |

---

## Elementdokumentation (Documentation - Element documentation)

Prüfgrundlage: `.github/instructions/BPMN_Documentation.instructions.md`

| Task | Dokumentation (Auszug) | Befund |
|---|---|---|
| `Postvermerk auf Dokument prüfen` | `-Anschrift`, `-Name des natürlichen Schuldners` | Stichworte ohne Satz, führende/nachgestellte Leerzeichen; Zweck, Bearbeitung und Ergebnis fehlen. |
| `Eintrag in KM- Ewo prüfen` | – | **fehlt** |
| `Wegzugsangaben prüfen` (KM-EwO) | `im KM-Ewo` | nur Systemhinweis, keine Beschreibung. |
| `Deutsche Adresse prüfen` | `Meldeportal, Bundeszentralregister über avviso` | nur Systemnennung. |
| `Anschrift über das Meldeportal prüfen` | `Meldeportal` | wiederholt nur das System. |
| `Wegzugsangaben prüfen` (Meldeportal) | `Meldeportal` | wiederholt nur das System. |
| `Weitere Ermittlungsarten prüfen` (2×) | `(AZR über avviso, BZR über avviso, DRV (Programm der Dt RV …` | Abkürzungen nicht erläutert, Klammer nicht geschlossen, endet mit „…". |
| `Ggf. Daten in avviso ergänzen` (2×) | `Z.B. Geburtsdatum, Geburtsort` | Beispiel ohne Beschreibung der Bearbeitung. |
| `Neue Anschrift in avviso erfassen` | `Avviso` | wiederholt nur das System. |
| `Bei SAP- Geschäftspartnern Stadtkasse informieren` | E-Mail über Lotus an zwei Funktionspostfächer | Inhaltlich am nächsten an einer Beschreibung; Anlass und Inhalt der Information ergänzen. |

Alle vorhandenen Einträge liegen als `<documentation id="documentation_…">` mit CDATA und ohne `textFormat` vor, in der korrekten Position vor `extensionElements`. Es sind 11 von 12 Tasks mit Dokumentation versehen, keine davon erfüllt die Vorgabe (Zweck, Bearbeitung, Ergebnis). Die Zuordnung des `documentation`-Elements zum ADONIS-Feld ist ohne Import-/Exportprüfung unbestätigt; das Format deutet auf einen ADONIS-Export hin.

---

## Empfehlungen

Priorisierte Liste der wichtigsten Änderungen für eine erfolgreiche Abnahme:

1. **Kunde-Pool ergänzen** (mindestens Black-Box, besser White-Box) und Nachrichtenflüsse modellieren: Dokumenteingang (Kunde → Organisation, Startereignis als Nachrichtenstart) sowie ggf. die Information der Stadtkasse. Kunde und Ergebnis-Empfänger mit dem Fachbereich klären; Start- und Endereignisse vom Kunden ableiten.
2. **Gateway `neue Anschrift bekannt?` bereinigen**: Zusammenführung der beiden `Wegzugsangaben prüfen`-Zweige und Entscheidung trennen bzw. `gatewayDirection` setzen; Ein- und Ausgänge an unterschiedlichen Kanten anbinden.
3. **Elementdokumentation überarbeiten**: Für `Eintrag in KM- Ewo prüfen` ergänzen, alle übrigen Einträge in vollständige Beschreibungen (Zweck, Bearbeitung, Ergebnis, Eingaben/Systeme) überführen, `textFormat="text/plain"` setzen. Abkürzungen (KM-EwO, AZR, BZR, DRV, Dt RV, SAP) in der Beschreibung ausschreiben.
4. **Endereignisse vereinheitlichen**: Singular/Plural angleichen, „evtl." und Klammerzusatz entfernen, Ergebnisse eindeutig benennen (z. B. Daten bestätigt / neue Anschrift erfasst und Stadtkasse informiert / keine aktuelle Anschrift ermittelt); gleichlautende Enden ggf. zusammenführen.
5. **Aufgabenbezeichnungen korrigieren** gemäß Tabelle „Task-Benennung" (Schreibweise KM-EwO, „Ggf." entfernen, `Weitere Ermittlungsarten prüfen`, Stadtkasse-Task).
6. **Gateway-Fragen präzisieren**: `Treffen die Angaben zu?` in zwei unterscheidbare Fragen umformulieren.
7. **IT-Systeme referenzieren**: Meldeportal und SAP an den betroffenen Tasks als IT-System ergänzen; optional IT-Pool prüfen.
8. **Modellmetadaten pflegen**: Prozessbeschreibung (Beschreibung, Zweck, Auslöser, Ergebnis), methodischen Prüfer (17-3.4 ADONIS-Team), Gültigkeitsdauer (max. 11 Monate); Personenbezug im Änderungsverlauf klären; „AbtL" und „SB" ausschreiben bzw. erläutern.
9. **Fachliche Abgrenzung klären**: `Deutsche Adresse prüfen` vs. `Anschrift über das Meldeportal prüfen`; identische, doppelt modellierte Schritte nach Abstimmung zusammenführen.
10. **Darstellung angleichen**: Ereignisgrößen 36×36, Wasserzeichen (Pool/Lane), Kantenansatz an Gateways nach dem Import in ADONIS prüfen.

---

## Ergebnis

- [ ] **Abnahme erteilt** – Modell entspricht allen Anforderungen
- [ ] **Abnahme mit Auflagen** – Modell wird bedingt akzeptiert, Auflagen sind umzusetzen
- [x] **Abnahme verweigert** – Kritische Fehler müssen vor Wiedervorlage behoben werden (fehlender Kunde-Pool und Nachrichtenflüsse)

Für die Remodellierung bitte den entsprechenden Remodellierungsagenten auswählen.
