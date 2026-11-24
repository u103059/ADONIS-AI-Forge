# Prozesssteckbrief: Incident Management

## Zusammenfassung
Der Prozess **"Incident Management"** bildet die Behandlung einer gemeldeten Störung im Regelbetrieb von der Meldung durch den Kunden bis zur bestätigten Wiederherstellung des Services ab. Er beginnt mit der Störungsmeldung des Kunden und der Prüfung durch den Service Desk, führt über die automatisierte Erfassung, Kategorisierung und Priorisierung im Ticketsystem der IT zur Analyse und Behebung durch die Organisation und endet mit dem Abschluss des Incidents sowie der Bestätigung der Lösung durch den Kunden. Ziel ist eine schnelle, transparente und nachvollziehbare Wiederherstellung gestörter Services unter Einbindung von Kunde, Service Desk und IT.

## Stammdaten
| Attribut | Wert |
| :--- | :--- |
| **Prozessname** | Incident Management |
| **Prozesskategorie** | IT-Servicemanagement / Störungsmanagement |
| **Auslöser** | Störung festgestellt |
| **Ergebnis** | Störung behoben / Incident abgeschlossen |
| **Hauptverantwortung** | Service Desk |
| **Beteiligte Rollen** | Kunde, IT (IT-Betrieb), Organisation (Service Desk) |

## Prozessziele
1. **Effizienz:** Minimierung der Ausfallzeiten durch automatisierte Erfassung, Kategorisierung, Priorisierung und Zuweisung im Ticketsystem.
2. **Qualität:** Sicherstellung nachhaltiger Lösungen durch strukturierte Ursachenanalyse und die Nutzung der Wissensdatenbank.
3. **Transparenz:** Nachvollziehbarkeit jedes Incidents durch lückenlose Dokumentation und Protokollierung von Bearbeitungszeiten.
4. **Serviceorientierung:** Zeitnahe Rückmeldung an den Kunden und Einbindung bei der Bestätigung der Lösung.
5. **Verlässlichkeit:** Einhaltung der vereinbarten Reaktions- und Lösungsfristen (SLA) in Abhängigkeit von der Priorität.

## Key Performance Indicators (KPIs)

Die folgenden Kennzahlen dienen der Messung der Prozessleistung und werden in Prozess-KPIs (Gesamtbetrachtung) und Aktivitäts-KPIs (Schrittbetrachtung) unterteilt.

### 1. Prozess-KPIs (Ebene Gesamtprozess)

Diese KPIs messen den Erfolg des gesamten End-to-End-Prozesses.

| KPI-ID | Kennzahl | Beschreibung | Zielwert | Messmethode |
| :--- | :--- | :--- | :--- | :--- |
| **P-KPI-01** | **Time-to-Resolution (Durchlaufzeit)** | Gesamtdauer von der Störungsmeldung bis zur Lösungsmitteilung an den Kunden. | Priorität hoch: < 4 Stunden; Priorität normal: < 3 Werktage | Timestamp(Lösung mitgeteilt) - Timestamp(Störungsmeldung eingegangen) |
| **P-KPI-02** | **SLA-Einhaltungsquote** | Anteil der Incidents, die innerhalb der vereinbarten Reaktions- und Lösungsfristen bearbeitet werden. | > 95% | Anzahl(Incidents mit eingehaltenem SLA) / Gesamtanzahl(Incidents) |
| **P-KPI-03** | **Erstlösungsquote** | Anteil der Incidents, die ohne Rückfrage an den Kunden oder Wiedereröffnung gelöst werden. | > 85% | Anzahl(Incidents ohne Rückfrage/Wiedereröffnung) / Gesamtanzahl(Incidents) |
| **P-KPI-04** | **Dunkelverarbeitungsquote (Teilprozess IT)** | Anteil der Incidents, die Erfassung, Kategorisierung, Priorisierung und Zuweisung ohne manuellen Eingriff durchlaufen. | > 90% | Anzahl(automatisch zugewiesene Incidents) / Gesamtanzahl(Incidents) |
| **P-KPI-05** | **Kundenbestätigungsquote** | Anteil der Incidents, bei denen der Kunde die Wiederherstellung bestätigt. | > 90% | Anzahl(bestätigte Lösungen) / Gesamtanzahl(mitgeteilte Lösungen) |

### 2. Aktivitäts-KPIs (Ebene Prozessschritte)

Diese KPIs sind spezifischen Aktivitäten oder Phasen im BPMN-Modell zugeordnet, um Engpässe zu identifizieren.

| Zugeordnete Aktivität(en) | KPI-Name | Beschreibung & Relevanz | Zielwert |
| :--- | :--- | :--- | :--- |
| **Störung melden** (Kunde) → **Meldung prüfen** (Organisation) | **Liegezeit Eingang** | Wartezeit der Störungsmeldung im Service Desk bis zum Beginn der Prüfung. Relevanz: Frühindikator für Personalengpässe und Grundlage der Reaktionszeit. | < 15 Minuten |
| **Meldung prüfen** (Organisation) | **Prüfdauer Meldung** | Bearbeitungszeit für die Prüfung von Vollständigkeit, Plausibilität und Zuständigkeit. Relevanz: Vermeidung von Verzögerungen vor der Erfassung. | < 10 Minuten |
| **Meldung prüfen** (Organisation) → **Incident priorisieren und zuweisen** (IT) | **Time-to-Assignment** | Zeitdauer von der geprüften Meldung bis zur Zuweisung an die Bearbeitergruppe mit gesetzten SLA-Fristen. Relevanz: Verfügbarkeit und Performance der automatisierten Verarbeitung. | < 5 Minuten |
| **Incident erfassen und kategorisieren** (IT) | **Kategorisierungsgenauigkeit** | Anteil der Incidents, deren automatische Kategorisierung im Verlauf nicht korrigiert werden muss. Relevanz: Voraussetzung für korrekte Zuweisung und Priorisierung. | > 90% |
| **Incident priorisieren und zuweisen** (IT) → **Störung analysieren und beheben** (Organisation) | **Time-to-First-Response** | Zeit von der Zuweisung bis zum Beginn der Analyse durch die Fachkraft. Relevanz: Einhaltung der Reaktionszeit je Priorität. | Priorität hoch: < 30 Minuten; Priorität normal: < 4 Stunden |
| **Störung analysieren und beheben** (Organisation) | **Bearbeitungszeit Analyse und Behebung** | Reine Bearbeitungsdauer für Ursachenanalyse, Umsetzung und Test der Lösung. Relevanz: Hauptanteil der Durchlaufzeit, Ressourcenplanung. | Priorität hoch: < 3 Stunden; Priorität normal: < 2 Werktage |
| **Störung analysieren und beheben** (Organisation) → **Lösung dokumentieren** (Organisation) | **Dokumentationsquote** | Anteil der Incidents mit vollständiger Lösungsdokumentation (Ursache, Maßnahmen, Lösung) bei Abschluss. Relevanz: Nachvollziehbarkeit und Wiederverwendbarkeit des Wissens. | 100% |
| **Incident abschließen** (IT) → **Lösung mitteilen** (Organisation) → **Lösung bestätigen** (Kunde) | **Time-to-Confirmation** | Zeit vom Abschluss des Incidents bis zur Bestätigung durch den Kunden. Relevanz: Einfluss auf die Gesamtdurchlaufzeit und Indikator für Kundenzufriedenheit. | < 1 Werktag |

## Eingesetzte IT-Systeme
- **Online-Formular (Störungsmeldung):** Erfassung der Störung mit Symptom, Zeitpunkt, betroffenem Service und Kontaktdaten durch den Kunden.
- **Ticketsystem:** Automatisierte Anlage, Kategorisierung, Priorisierung, Zuweisung und Archivierung von Incidents sowie Überwachung der SLA-Fristen und Protokollierung der Bearbeitungszeiten.
- **Wissensdatenbank:** Unterstützung der Diagnose und Dokumentation bekannter Fehler und Lösungen.

## Referenzdokumente
- BPMN-Modell: `ADONIS_KOI_Incident_Management.bpmn`
- Interne Prioritätsmatrix (Auswirkung/Dringlichkeit) und Service Level Agreements (SLA)
