# 💡 Generative KI für Prozessmodelle in der öffentlichen Verwaltung

## Projektziel

Dieses Repository dokumentiert einen innovativen Ansatz zur Erstellung von **ADONIS-kompatiblen BPMN-Prozessmodellen** mithilfe von **GitHub Copilot** und generativer KI. Ziel ist es, einen **reproduzierbaren Workflow** zu entwickeln, mit dem Kommunen, Verwaltungen und Organisationen schnell und standardisiert Prozessbeschreibungen und -modelle generieren können – auf Basis von **BPMN 2.0** und importierbar in **ADONIS**.


## Hintergrund

Die öffentliche Verwaltung steht vor der Herausforderung, komplexe und heterogene Prozesse strategisch zu erfassen und kontinuierlich zu digitalisieren. Klassische Prozessaufnahmen sind zeit- und ressourcenintensiv. Hier setzt das Projekt an: Durch die Kombination aus domänenspezifischen Prompts, GitHub Copilot und BPMN-Standards wird eine KI-gestützte Modellierung ermöglicht, die bestehende Verwaltungsprozesse effizient und konsistent abbildet.

## Was dieses Projekt bietet

* 🧠 **Prompting-Strategien** zur Erzeugung qualitativ hochwertiger Prozessbeschreibungen
* 🔄 **Transformationsregeln** von Fließtext zu BPMN-Modellen
* :eyeglasses: **Erstellung von e2e-Prozessmodellen** durch Einbeziehung der Perspektiven **Kunde, Organisation und IT (KOI)**
* :microphone: **Geführte Prozessaufnahme** per Interview (Agent `Moritz`) mit Steckbrief und Ist-Prozessmodell
* :mag: **Erstellung von standardisierten Prozesssteckbriefen** mit KPIs für Gesamtprozess und Aktivitäten im BPMN-Modell
* :white_check_mark: **Methodische Prüfung** von ADONIS-Prozessmodellen, inkl. Abruf über die ADONIS-REST-API

## Technologische Basis

* **GitHub Copilot** mit Custom Agents zur KI-unterstützten Erstellung von BPMN-XML
* **BPMN 2.0** als Modellierungsstandard
* **ADONIS** als Zielsystem für Import und Review der Prozessmodelle
* **Camunda Modeler (Miragon)** zur Darstellung und Bearbeitung der BPMN-Prozessmodelle in VS Code

Details zu Voraussetzungen, Agenten und Abläufen: [TECHNISCHE_DOKUMENTATION.md](docs/TECHNISCHE_DOKUMENTATION.md)

## Warum das wichtig ist

* ⏱️ **Ressourcenschonung**: Reduktion von Aufwand und Kosten in der Prozessaufnahme
* 📊 **Strukturiertes Vorgehen**: Förderung von Standardisierung und Wiederverwendung
* 🌐 **Interkommunale Skalierbarkeit**: Ansatz ist nachnutzbar

## Mitmachen

Du bist Prozessmanager:in, Entwickler:in oder interessierst dich für die Anwendung von KI in der öffentlichen Verwaltung? Beiträge, Feedback und neue Beispiele sind jederzeit willkommen!

## Lizenz

Dieses Projekt steht unter der MIT-Lizenz.
