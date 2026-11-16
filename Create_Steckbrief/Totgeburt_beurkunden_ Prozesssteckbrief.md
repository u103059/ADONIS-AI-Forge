# Prozesssteckbrief: Totgeburt beurkunden

## Zusammenfassung
Der Prozess **"Totgeburt beurkunden"** regelt die amtliche Erfassung und Beurkundung einer Totgeburt im Personenstandsregister. Er beginnt mit der Anzeige durch die sorgeberechtigten Personen oder die betreuende Einrichtung, führt über die Prüfung der personenstandsrechtlichen Voraussetzungen und erforderlichen Nachweise durch das Standesamt bis zur Eintragung im Register. Der Prozess endet mit der Ausstellung der Bescheinigung über die Totgeburt oder einer Geburtsurkunde mit entsprechendem Vermerk für die Eltern. Ziel ist eine würdevolle, rechtssichere und zeitnahe Beurkundung unter Wahrung aller gesetzlichen Fristen.

## Stammdaten
| Attribut | Wert |
| :--- | :--- |
| **Prozessname** | Totgeburt beurkunden |
| **Prozesskategorie** | Personenstandswesen / Bürgerdienste |
| **Auslöser** | Totgeburt eingetreten / Anzeige eingegangen |
| **Ergebnis** | Totgeburt beurkundet und Urkunde ausgestellt |
| **Hauptverantwortung** | Standesamt |
| **Beteiligte Rollen** | Bürger (Anzeigepflichtige), Standesbeamter, IT-System (Fachverfahren) |

## Prozessziele
1. **Rechtssicherheit:** Gewährleistung einer korrekten personenstandsrechtlichen Erfassung gemäß PStG und PStV.
2. **Effizienz:** Minimierung der Durchlaufzeit zwischen Anzeige und Urkundenausstellung, um den Eltern zeitnah Dokumente für Bestattung und weitere Behördengänge bereitzustellen.
3. **Datenqualität:** Sicherstellung korrekter Registerdaten durch automatisierte Plausibilitätsprüfungen und validierte Eingaben.
4. **Serviceorientierung:** Einfache und würdevolle Antragstellung für betroffene Eltern durch digitale Vorab-Erfassung und transparente Kommunikation.

## Key Performance Indicators (KPIs)

Die folgenden Kennzahlen dienen der Messung der Prozessleistung und werden in Prozess-KPIs (Gesamtbetrachtung) und Aktivitäts-KPIs (Schrittbetrachtung) unterteilt.

### 1. Prozess-KPIs (Ebene Gesamtprozess)

Diese KPIs messen den Erfolg des gesamten End-to-End-Prozesses.

| KPI-ID | Kennzahl | Beschreibung | Zielwert | Messmethode |
| :--- | :--- | :--- | :--- | :--- |
| **P-KPI-01** | **Durchlaufzeit (E2E)** | Gesamtdauer von Eingang der Anzeige bis zur Bereitstellung der Urkunde. | < 3 Arbeitstage | Timestamp(Urkunde erstellt) - Timestamp(Anzeige eingegangen) |
| **P-KPI-02** | **First-Pass-Yield** | Anteil der Anzeigen, die ohne manuelle Nachforderungen oder Korrekturen beurkundet werden können. | > 85% | Anzahl(Vorgänge ohne Rückschleifen) / Gesamtanzahl |
| **P-KPI-03** | **Service-Level (SLA)** | Einhaltung der gesetzlichen und internen Fristen zur Beurkundung. | > 98% | Anzahl(SLA eingehalten) / Gesamtanzahl |
| **P-KPI-04** | **Automatisierungsgrad** | Anteil der Vorgangsdaten, die vom Bürger/Klinik direkt digital übernommen werden können. | > 60% | Anzahl(Feldinhalte übernommen) / Gesamtanzahl(Feldinhalte) |

### 2. Aktivitäts-KPIs (Ebene Prozessschritte)

Diese KPIs sind spezifischen Aktivitäten oder Phasen im BPMN-Modell zugeordnet, um Engpässe zu identifizieren.

| Zugeordnete Aktivität(en) | KPI-Name | Beschreibung & Relevanz | Zielwert |
| :--- | :--- | :--- | :--- |
| **Anzeige eingegangen** (Standesamt) → **Zuständigkeit feststellen** (Standesamt) | **Liegezeit Eingang** | Zeitdauer bis zur ersten Sichtung des Falls. Relevant für schnelle Reaktionszeiten. | < 4 Stunden |
| **Zuständigkeit feststellen** → **Unterlagen prüfen** (Standesamt) | **Prüfdauer** | Dauer der fachlichen Bewertung der eingereichten Nachweise. Indikator für Komplexität oder Schulungsbedarf. | < 1 Arbeitstag |
| **Registereintrag veranlassen** (Standesamt) → **Prüfergebnis erhalten** (Standesamt/IT) | **Systemantwortzeit** | Wartezeit auf Rückmeldung des Fachverfahrens/Registers. Kritisch für flüssiges Arbeiten. | < 1 Minute |
| **Prüfergebnis erhalten** → **Beurkundung vornehmen** (Standesamt) | **Bearbeitungszeit Finalisierung** | Dauer für die rechtliche Freigabe und Signatur des Eintrags nach technischer Prüfung. | < 2 Stunden |
| **Beurkundung vornehmen** → **Urkunde ausstellen** (Standesamt) | **Erstellungsdauer Dokumente** | Zeit zur Generierung und Bereitstellung der physischen/digitalen Urkunden. | < 30 Minuten |

## Eingesetzte IT-Systeme
- **Fachverfahren Personenstandswesen (z.B. AutiSta):** Kernsystem zur Führung der Personenstandsregister und Beurkundung.
- **Formularserver / Online-Portal:** Schnittstelle für Bürger zur digitalen Anzeige und Dokumentenübermittlung.
- **XPersonenstand-Schnittstelle:** Standardisierter Datenaustausch mit anderen Behörden und Registern.
- **DMS (Dokumentenmanagementsystem):** Zur revisionssicheren Ablage der Sammelakten und Nachweise.

## Referenzdokumente
- BPMN-Modell: `Totgeburt_beurkunden.bpmn`
- Personenstandsgesetz (PStG)
- Personenstandsverordnung (PStV)
- Dienstanweisung für die Standesbeamten und ihre Aufsichtsbehörden (DA)

