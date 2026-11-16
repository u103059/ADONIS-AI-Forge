# Prozesssteckbrief: Antrag auf Betreuungsgeld bearbeiten

## Zusammenfassung
Der Prozess **"Antrag auf Betreuungsgeld bearbeiten"** regelt das Verfahren zur Gewährung von Betreuungsgeld an Sorgeberechtigte. Er beginnt mit der Antragstellung durch den Kunden, führt über die formelle und materielle Prüfung durch die zuständige Organisation (Zuständigkeit, Vollständigkeit, Anspruchsvoraussetzungen, Berechnung) und endet mit der Erstellung und dem Versand des Bewilligungsbescheids. Ziel ist eine effiziente, rechtssichere und bürgerfreundliche Bearbeitung der Anträge zur zeitnahen finanziellen Unterstützung der Familien.

## Stammdaten
| Attribut | Wert |
| :--- | :--- |
| **Prozessname** | Antrag auf Betreuungsgeld bearbeiten |
| **Prozesskategorie** | Bürger-Service / Sozialleistung |
| **Auslöser** | Bedarf nach Betreuungsgeld festgestellt / Antrag eingegangen |
| **Ergebnis** | Betreuungsgeld bewilligt / Bescheid zugestellt |
| **Hauptverantwortung** | Fachbereich Soziales / Jugendamt |
| **Beteiligte Rollen** | Kunde (Antragsteller), Organisation (Sachbearbeitung) |

## Prozessziele
1. **Rechtssicherheit:** Gewährleistung der korrekten Anwendung der gesetzlichen Vorschriften und Anspruchsvoraussetzungen zum Betreuungsgeld.
2. **Effizienz:** Zügige Bearbeitung der Anträge zur Vermeidung von Wartezeiten und zur schnellen finanziellen Entlastung der Familien.
3. **Qualität:** Minimierung von Fehlern bei der Datenerfassung, Anspruchsprüfung und Berechnung der Leistungshöhe.
4. **Serviceorientierung:** Einfache Antragstellung, verständliche Prozesse und transparente Kommunikation mit dem Antragsteller.

## Key Performance Indicators (KPIs)

Die folgenden Kennzahlen dienen der Messung der Prozessleistung und werden in Prozess-KPIs (Gesamtbetrachtung) und Aktivitäts-KPIs (Schrittbetrachtung) unterteilt.

### 1. Prozess-KPIs (Ebene Gesamtprozess)

Diese KPIs messen den Erfolg des gesamten End-to-End-Prozesses.

| KPI-ID | Kennzahl | Beschreibung | Zielwert | Messmethode |
| :--- | :--- | :--- | :--- | :--- |
| **P-KPI-01** | **Durchlaufzeit (End-to-End)** | Gesamtdauer vom Antragseingang bei der Organisation bis zum Versand des Bescheids. | < 20 Arbeitstage | Timestamp(Versand) - Timestamp(Eingang) |
| **P-KPI-02** | **First-Pass-Yield (FPY)** | Anteil der Anträge, die ohne Rückfragen oder Nachforderungen ("gerade durch") bearbeitet werden können. | > 85% | Anzahl(Anträge ohne Rückfragen) / Gesamtanzahl(Anträge) |
| **P-KPI-03** | **Termintreue** | Einhaltung der gesetzlich oder intern vorgegebenen Bearbeitungsfristen. | > 95% | Anzahl(Fristgerechte Bearbeitungen) / Gesamtanzahl(Bearbeitungen) |
| **P-KPI-04** | **Bewilligungsquote** | Anteil der positiv beschiedenen Anträge im Verhältnis zu allen geprüften Anträgen. | Beobachtungswert | Anzahl(Bewilligungen) / Gesamtanzahl(Entscheidungen) |

### 2. Aktivitäts-KPIs (Ebene Prozessschritte)

Diese KPIs sind spezifischen Aktivitäten oder Phasen im BPMN-Modell zugeordnet, um Engpässe zu identifizieren.

| Zugeordnete Aktivität(en) | KPI-Name | Beschreibung & Relevanz | Zielwert |
| :--- | :--- | :--- | :--- |
| **Eingang erfassen** (Organisation) → **Zuständigkeit prüfen** | **Erfassungsdauer** | Zeitspanne zwischen technischem Antragseingang und systemseitiger Erfassung/Weiterleitung zur Prüfung. Relevant für schnelle Initialbearbeitung. | < 1 Arbeitstag |
| **Zuständigkeit prüfen** → **Vollständigkeit prüfen** | **Vorprüfungszeit** | Dauer der formalen Prüfung auf Zuständigkeit und Vollständigkeit der Unterlagen. Engpassindikator für initiale Filterung. | < 2 Arbeitstage |
| **Vollständigkeit prüfen** → **Anspruchsvoraussetzungen prüfen** | **Wartezeit auf Sachbearbeitung** | Liegezeit zwischen formaler Vorprüfung und Beginn der inhaltlichen Prüfung. Indikator für Auslastung der Sachbearbeitung. | < 3 Arbeitstage |
| **Anspruchsvoraussetzungen prüfen** (Organisation) | **Prüfungsdauer (Sachlich)** | Reine Bearbeitungszeit für die komplexe inhaltliche Prüfung der Anspruchsvoraussetzungen. Kernaktivität des Prozesses. | < 3 Arbeitstage |
| **Höhe berechnen** → **Bescheid erstellen** | **Berechnungs- & Erstellungszeit** | Zeitbedarf für die technische Berechnung der Leistungshöhe und die Generierung des Bescheids. | < 1 Arbeitstag |
| **Bescheid erstellen** → **Bescheid versenden** | **Versanddauer** | Zeitspanne zwischen Erstellung des Dokuments und physischem/digitalem Versand an den Kunden. | < 1 Arbeitstag |

## Eingesetzte IT-Systeme
- **Fachverfahren Sozialwesen (z.B. Lämmerkom/OpenSoz):** Zentrales System zur Fallbearbeitung, Anspruchsprüfung und Bescheiderstellung.
- **Berechnungsmodul:** Spezielle Komponente oder externe Software zur exakten Ermittlung der Anspruchshöhe gemäß gesetzlichen Vorgaben.
- **DMS (Dokumentenmanagementsystem):** Zur elektronischen Aktenführung und Archivierung der Antragsunterlagen und Bescheide.
- **Output-Management-System:** Für den automatisierten Druck und Versand der Bescheide.

## Referenzdokumente
- BPMN-Modell: `Betreuungsgeld_beantragen.bpmn`
- Bundeselterngeld- und Elternzeitgesetz (BEEG) (Analoge Anwendung oder landesspezifische Regelungen für Betreuungsgeld)
- Interne Arbeitsanweisungen zur Prüfung von Sozialleistungen
- Datenschutzrichtlinien (DSGVO) bei der Verarbeitung von Sozialdaten

