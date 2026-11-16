# Prozesssteckbrief: Miteinbürgerung genehmigen

## Zusammenfassung
Der Prozess **"Miteinbürgerung genehmigen"** dient der formalen Prüfung und rechtsverbindlichen Genehmigung eines Antrags auf Miteinbürgerung für eine mitantragstellende Person. Der Prozess beginnt mit dem Eingang des Antrags, führt über die digitale Erfassung und fachliche Prüfung der Voraussetzungen durch die Behörde und endet mit der Zustellung des Genehmigungsbescheids. Ziel ist eine effiziente, transparente und rechtssichere Bearbeitung unter Einbindung der beteiligten Stellen.

## Stammdaten
| Attribut | Wert |
| :--- | :--- |
| **Prozessname** | Miteinbürgerung genehmigen |
| **Prozesskategorie** | Personenstandswesen |
| **Auslöser** | Antrag auf Miteinbürgerung eingegangen |
| **Ergebnis** | Miteinbürgerung genehmigt |
| **Hauptverantwortung** | Einbürgerungsbehörde |
| **Beteiligte Rollen** | Bürger, IT, Einbürgerungsbehörde |

## Prozessziele
1. **Effizienz:** Minimierung der Gesamtdurchlaufzeit von der Antragstellung bis zur Bescheidzustellung durch klare Schnittstellen und digitale Unterstützung.
2. **Qualität:** Sicherstellung einer hohen Daten- und Entscheidungsqualität durch systemgestützte Prüfungen und definierte Bearbeitungsschritte.
3. **Rechtssicherheit:** Gewährleistung der Einhaltung aller gesetzlichen Vorgaben und Fristen im Einbürgerungsverfahren.
4. **Serviceorientierung:** Bereitstellung eines transparenten und nachvollziehbaren Verfahrens für den Bürger.

## Key Performance Indicators (KPIs)

Die folgenden Kennzahlen dienen der Messung der Prozessleistung und werden in Prozess-KPIs (Gesamtbetrachtung) und Aktivitäts-KPIs (Schrittbetrachtung) unterteilt.

### 1. Prozess-KPIs (Ebene Gesamtprozess)

Diese KPIs messen den Erfolg des gesamten End-to-End-Prozesses.

| KPI-ID | Kennzahl | Beschreibung | Zielwert | Messmethode |
| :--- | :--- | :--- | :--- | :--- |
| **P-KPI-01** | **Gesamtdurchlaufzeit** | Misst die Zeit vom Eingang des Antrags bis zur Zustellung des Bescheids an den Bürger. | < 45 Tage | Timestamp(EndEvent_Behoerde) - Timestamp(StartEvent_Behoerde) |
| **P-KPI-02** | **Erstmalige Erfolgsquote** | Anteil der Anträge, die ohne zusätzliche Rückfragen oder Nachforderungen direkt positiv beschieden werden. | > 90% | (Anzahl fehlerfreie Anträge / Gesamtanzahl Anträge) * 100 |
| **P-KPI-03** | **Automatisierungsgrad der Datenerfassung** | Anteil der Antragsdaten, die vollautomatisch vom IT-System ohne manuelle Korrektur erfasst werden. | > 98% | (Anzahl automatisch erfasster Felder / Gesamtanzahl Felder) * 100 |

### 2. Aktivitäts-KPIs (Ebene Prozessschritte)

Diese KPIs sind spezifischen Aktivitäten oder Phasen im BPMN-Modell zugeordnet, um Engpässe zu identifizieren.

| Zugeordnete Aktivität(en) | KPI-Name | Beschreibung & Relevanz | Zielwert |
| :--- | :--- | :--- | :--- |
| **Task_Antrag_entgegennehmen** (Behörde) → **Task_Antragsdaten_erfassen** (IT) | **Digitalisierungsdauer** | Zeit, die für die Überführung der Antragsdaten von der Behörde ins IT-System benötigt wird. Relevant für die Effizienz der Eingangsverarbeitung. | < 8 Stunden | Timestamp(StartEvent_IT) - Timestamp(StartEvent_Behoerde) |
| **Task_Antragsdaten_erfassen** (IT) → **Task_Entscheidungsgrundlage_bereitstellen** (IT) | **IT-Verarbeitungszeit** | Dauer der internen Datenverarbeitung und -aufbereitung im IT-System. Ein Indikator für die Systemperformance. | < 1 Stunde | Timestamp(EndEvent_IT) - Timestamp(StartEvent_IT) |
| **Event_IT_Daten_erhalten** (Behörde) → **Task_Voraussetzungen_pruefen** (Behörde) | **Liegezeit bis Fachprüfung** | Zeit zwischen der Bereitstellung der Daten durch die IT und dem Beginn der fachlichen Prüfung. Identifiziert potenzielle Wartezeiten. | < 24 Stunden | Timestamp(Start_Task_Voraussetzungen_pruefen) - Timestamp(Event_IT_Daten_erhalten) |
| **Task_Voraussetzungen_pruefen** (Behörde) → **Task_Genehmigung_erteilen** (Behörde) | **Dauer der Fachprüfung** | Reine Bearbeitungszeit für die inhaltliche Prüfung der Einbürgerungsvoraussetzungen. Misst die Effizienz der Sachbearbeitung. | < 5 Arbeitstage | Timestamp(Ende_Task_Voraussetzungen_pruefen) - Timestamp(Start_Task_Voraussetzungen_pruefen) |
| **Task_Genehmigung_erteilen** (Behörde) → **Task_Bescheid_uebermitteln** (Behörde) | **Zeit für Bescheiderstellung** | Dauer von der positiven Entscheidung bis zur finalen Erstellung des rechtsgültigen Bescheids. | < 2 Arbeitstage | Timestamp(Start_Task_Bescheid_uebermitteln) - Timestamp(Ende_Task_Genehmigung_erteilen) |

## Eingesetzte IT-Systeme
- **Fachverfahren Einbürgerung:** Zentrales System zur Verwaltung aller antrags- und personenbezogenen Daten des Einbürgerungsverfahrens.
- **Dokumenten-Management-System (DMS):** System zur Archivierung der Antragsunterlagen und des Genehmigungsbescheids.

## Referenzdokumente
- BPMN-Modell: `Miteinbuergerung_genehmigen.bpmn`
- Staatsangehörigkeitsgesetz (StAG)
- Allgemeine Verwaltungsvorschrift zum Staatsangehörigkeitsrecht (StAR-VwV)

---
