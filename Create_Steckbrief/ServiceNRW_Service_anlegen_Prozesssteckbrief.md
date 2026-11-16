# Prozesssteckbrief: Service in ServiceNRW anlegen

## Zusammenfassung
Der Prozess **"Service in ServiceNRW anlegen"** beschreibt den End-to-End-Ablauf von der fachlichen Anforderung zur Anlage eines neuen digitalen Services bis zu dessen Bereitstellung für den Bürger im IT-System ServiceNRW. Der Prozess beginnt mit der Erfassung der Serviceinhalte durch die Behörde, führt über die technische Umsetzung im IT-System und endet mit dem Aufruf des veröffentlichten Services durch den Bürger. Ziel ist eine standardisierte, effiziente und transparente Bereitstellung von digitalen Verwaltungsleistungen.

## Stammdaten
| Attribut | Wert |
| :--- | :--- |
| **Prozessname** | Service in ServiceNRW anlegen |
| **Prozesskategorie** | IT-Servicemanagement |
| **Auslöser** | Anforderung zur Serviceanlage eingegangen |
| **Ergebnis** | Service in ServiceNRW bereitgestellt |
| **Hauptverantwortung** | Behörde (fachlich), IT (technisch) |
| **Beteiligte Rollen** | Behörde, IT, Bürger |

## Prozessziele
1. **Effizienz:** Beschleunigung der Servicebereitstellung durch einen standardisierten und teilautomatisierten Anlageprozess.
2. **Qualität:** Sicherstellung einer hohen Daten- und Servicequalität durch Validierungsmechanismen und klare Verantwortlichkeiten.
3. **Transparenz:** Schaffung einer nachvollziehbaren Prozesskette von der Anforderung bis zur Veröffentlichung des Services.
4. **Serviceorientierung:** Schnelle und bedarfsgerechte Bereitstellung neuer digitaler Services für den Bürger.

## Key Performance Indicators (KPIs)

Die folgenden Kennzahlen dienen der Messung der Prozessleistung und werden in Prozess-KPIs (Gesamtbetrachtung) und Aktivitäts-KPIs (Schrittbetrachtung) unterteilt.

### 1. Prozess-KPIs (Ebene Gesamtprozess)

Diese KPIs messen den Erfolg des gesamten End-to-End-Prozesses.

| KPI-ID | Kennzahl | Beschreibung | Zielwert | Messmethode |
| :--- | :--- | :--- | :--- | :--- |
| **P-KPI-01** | **Time-to-Market** | Gesamtzeit von der Anforderung (Start Behörde) bis zur Veröffentlichung des Services (Ende IT). | < 5 Arbeitstage | Timestamp(EndEvent_IT) - Timestamp(StartEvent_Behoerde) |
| **P-KPI-02** | **Prozessqualität** | Anteil der Serviceanlagen, die ohne fachliche oder technische Nachbesserungen (Schleifen) durchlaufen. | > 95% | (Anzahl Gesamt - Anzahl mit Korrekturen) / Anzahl Gesamt |
| **P-KPI-03** | **Automatisierungsgrad** | Anteil der Prozessschritte, die ohne manuelle Intervention (Service Tasks) ausgeführt werden. | > 60% | Anzahl(Service Tasks) / Anzahl(Gesamt-Tasks) |

### 2. Aktivitäts-KPIs (Ebene Prozessschritte)

Diese KPIs sind spezifischen Aktivitäten oder Phasen im BPMN-Modell zugeordnet, um Engpässe zu identifizieren.

| Zugeordnete Aktivität(en) | KPI-Name | Beschreibung & Relevanz | Zielwert |
| :--- | :--- | :--- | :--- |
| **Task_Serviceinhalt_erfassen** (Behörde) → **Task_Anlagedaten_uebermitteln** (Behörde) | **Fachliche Vorbereitungszeit** | Dauer der fachlichen Spezifikation und Freigabe. Ein Indikator für die interne Effizienz der Behörde. | < 2 Arbeitstage |
| **Task_Anlagedaten_uebermitteln** (Behörde) → **Task_Service_anlegen** (IT) | **Technische Umsetzungszeit** | Zeit, die das IT-System für die Validierung und Anlage des Services benötigt. Misst die Performance des IT-Systems. | < 1 Arbeitstag |
| **Task_Service_anlegen** (IT) → **Task_Anlage_rueckmelden** (IT) | **Konfigurations- & Feedbackzeit** | Dauer der Konfiguration und der systemseitigen Rückmeldung an die Behörde. | < 8 Stunden |
| **Task_Anlage_rueckmelden** (IT) → **Catch_Bestaetigung_erhalten** (Behörde) | **Bestätigungs-Latenz** | Zeit, bis die Behörde die erfolgreiche Anlage zur Kenntnis nimmt. Relevant für die Prozesssteuerung. | < 4 Stunden |
| **Task_Service_veroeffentlichen** (IT) → **StartEvent_Buerger** (Bürger) | **Veröffentlichungs-Dauer** | Zeit zwischen technischer Bereitstellung und tatsächlicher Sichtbarkeit für den Bürger. | < 1 Stunde |

## Eingesetzte IT-Systeme
- **ServiceNRW:** Zentrales IT-System zur Konfiguration, Verwaltung und Bereitstellung der digitalen Services.
- **Fachverfahren der Behörde (optional):** Quellsysteme für Serviceinhalte und -daten.
- **Digitaler Zugangskanal (Bürgerportal):** Plattform, auf der die Services für den Bürger veröffentlicht werden.

## Referenzdokumente
- BPMN-Modell: `ServiceNRW_Service_anlegen.bpmn`
- Formular: `ServiceNRW_Service_aufrufen.form`
- IT-Servicemanagement-Richtlinien

---
