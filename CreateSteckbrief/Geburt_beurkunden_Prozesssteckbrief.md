# Prozesssteckbrief: Geburt beurkunden

## Zusammenfassung
Der Prozess **"Geburt beurkunden"** bildet den Ablauf ab der Anzeige einer Geburt durch den Bürger oder das Krankenhaus bis zur Ausstellung der Geburtsurkunde ab. Er beginnt mit der Erfassung der Geburtsdaten und das Hochladen von Nachweisen durch den Bürger, führt über die automatische Vorprüfung und Weiterleitung durch die IT-Infrastruktur zur fachlichen Prüfung und Beurkundung durch das Standesamt. Der Prozess endet mit der Zustellung der digitalen oder physischen Geburtsurkunde an den Bürger sowie dem Eintrag in das Personenstandsregister. Ziel ist eine effiziente, medienbruchfreie und rechtssichere Abwicklung von Geburtsanzeigen unter Einbindung von Bürgern, IT-Systemen und dem Standesamt.

## Stammdaten
| Attribut | Wert |
| :--- | :--- |
| **Prozessname** | Geburt beurkunden |
| **Prozesskategorie** | Personenstandswesen |
| **Auslöser** | Geburt angezeigt / Anzeige eingegangen |
| **Ergebnis** | Geburt beurkundet / Urkunde zugestellt |
| **Hauptverantwortung** | Standesamt |
| **Beteiligte Rollen** | Bürger, IT, Standesamt |

## Prozessziele
1. **Effizienz:** Minimierung der Durchlaufzeiten durch automatisierte Vorprüfung und direkten Datenaustausch zwischen Bürger und Behörde.
2. **Qualität:** Sicherstellung korrekter Registereinträge durch Vier-Augen-Prinzip und fachliche Prüfung im Standesamt.
3. **Serviceorientierung:** Reduzierung von Behördengängen für Eltern durch digitale Antragstellung und Nachreichung von Unterlagen.
4. **Rechtssicherheit:** Einhaltung der personenstandsrechtlichen Vorschriften (PStG) bei der Beurkundung.

## Key Performance Indicators (KPIs)

Die folgenden Kennzahlen dienen der Messung der Prozessleistung und werden in Prozess-KPIs (Gesamtbetrachtung) und Aktivitäts-KPIs (Schrittbetrachtung) unterteilt.

### 1. Prozess-KPIs (Ebene Gesamtprozess)

Diese KPIs messen den Erfolg des gesamten End-to-End-Prozesses.

| KPI-ID | Kennzahl | Beschreibung | Zielwert | Messmethode |
| :--- | :--- | :--- | :--- | :--- |
| **P-KPI-01** | **Time-to-Certificate (Durchlaufzeit)** | Gesamtzeitdauer von der Anzeige der Geburt bis zur Bereitstellung der Urkunde. | < 7 Werktage | Timestamp(Urkunde bereitgestellt) - Timestamp(Anzeige eingegangen) |
| **P-KPI-02** | **Dunkelverarbeitungsquote (Teilprozess)** | Anteil der Schritte, die ohne manuellen Eingriff durch die IT verarbeitet werden (bis zur Übergabe an Standesamt). | > 90% | Anzahl(Auto-Weiterleitung an Behörde) / Gesamtanzahl(Anzeigen) |
| **P-KPI-03** | **Erstlösungsquote** | Anteil der Anträge, die ohne manuelle Nachforderung von Unterlagen beurkundet werden können. | > 80% | Anzahl(Anträge ohne Rückfrage) / Gesamtanzahl(Anträge) |

### 2. Aktivitäts-KPIs (Ebene Prozessschritte)

Diese KPIs sind spezifischen Aktivitäten oder Phasen im BPMN-Modell zugeordnet, um Engpässe zu identifizieren.

| Zugeordnete Aktivität(en) | KPI-Name | Beschreibung & Relevanz | Zielwert |
| :--- | :--- | :--- | :--- |
| **Anzeige absenden** (Bürger) → **Daten entgegennehmen** (IT) | **Submission Latency** | Zeitdauer zwischen Absenden und technischem Empfang (Systemverfügbarkeit). Relevanz: Sicherstellung der 24/7 Verfügbarkeit. | < 5 Minuten |
| **StartEvent Behoerde** (Standesamt) → **Beurkundung vornehmen** (Standesamt) | **Liegezeit Eingangskorb** | Wartezeit des Vorgangs im Posteingang des Standesamtes bis zur ersten Bearbeitung. Relevanz: Identifikation von Personalengpässen. | < 2 Werktage |
| **Beurkundung vornehmen** (Standesamt) → **Rückmeldung senden** (Standesamt) | **Bearbeitungszeit Sachbearbeiter** | Reine Bearbeitungsdauer für die fachliche Prüfung und Beurkundung. Relevanz: Ressourcenplanung. | < 30 Minuten |
| **Nachweise hochladen** (Bürger) → **Vollständigkeit prüfen** (IT) | **Nachreichungsdauer** | Zeitspanne, die der Bürger benötigt, um fehlende Dokumente bereitzustellen. Relevanz: Einfluss auf Gesamtdurchlaufzeit. | < 3 Tage |
| **Rückmeldung senden** (Standesamt) → **Urkunde freigeben** (Standesamt) | **Freigabedauer** | Zeit zwischen Abschluss der Beurkundung und finaler Freigabe der Urkunde. Relevanz: Prozessabschlussgeschwindigkeit. | < 4 Stunden |

## Eingesetzte IT-Systeme
- **Online-Portal (Frontend):** Plattform für die Erfassung der Anzeige und den Upload von Nachweisen durch den Bürger.
- **Vorgangsbearbeitungssystem (Mid-Office):** IT-Komponente zur Entgegennahme, Vorprüfung und Weiterleitung der Daten (Orchestrierung).
- **Fachverfahren Personenstandswesen (z.B. AutiSta):** System im Standesamt zur rechtssicheren Beurkundung und Registerführung.

## Referenzdokumente
- BPMN-Modell: [CreateBPMN/Geburt_beurkunden.bpmn](../CreateBPMN/Geburt_beurkunden.bpmn)
- Personenstandsgesetz (PStG)
- Verordnung zur Ausführung des Personenstandsgesetzes (PStV)
