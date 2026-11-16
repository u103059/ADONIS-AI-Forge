# Kommunikationsstrategie zur Veröffentlichung von ADONIS-AI-Forge

> Status: Entwurf · Alle Termine, Kanäle und Verantwortlichkeiten sind Vorschläge und vor Veröffentlichung abzustimmen.

## 1. Ausgangslage und Ziel

**ADONIS-AI-Forge** zeigt einen reproduzierbaren Workflow, mit dem sich mithilfe von GitHub Copilot und Custom Agents ADONIS-kompatible BPMN-2.0-Prozessmodelle, Prozesssteckbriefe, methodische Reviews und geführte Prozessaufnahmen erstellen lassen (Agenten: `ADONIS_BPMN_KO`, `ADONIS_BPMN_KOI`, `ADONIS_BPMN_I`, `Steckbrief`, `ADONIS_Review`, `Moritz`).

### Kommunikationsziele

| # | Ziel | Messgröße (Vorschlag) |
|---|---|---|
| 1 | Sichtbarkeit in der Verwaltungs- und Prozessmanagement-Community herstellen | Repo-Stars, Besucher:innen, Reichweite der Beiträge |
| 2 | Nachnutzung durch weitere Kommunen/Verwaltungen anstoßen | Forks, Clones, gemeldete Anwendungsfälle |
| 3 | Mitwirkung gewinnen (Beispiele, Feedback, Verbesserungen) | Issues, Pull Requests, Diskussionen |
| 4 | Den Ansatz als seriösen, nachvollziehbaren Beitrag zu KI in der Verwaltung positionieren | Einladungen zu Vorträgen/Austauschformaten, Erwähnungen |

## 2. Kernbotschaften

**Leitbotschaft:** *Prozessaufnahme und -modellierung in der Verwaltung schneller, standardisierter und nachnutzbar machen – mit generativer KI, offenen Standards (BPMN 2.0) und offenem Quellcode.*

Unterstützende Botschaften:

1. **Ressourcenschonung:** Weniger Aufwand bei der Prozessaufnahme, mehr Zeit für Analyse und Optimierung.
2. **Standardisierung:** Einheitliche Modelle und Steckbriefe mit KPIs, importierbar in ADONIS.
3. **Perspektivenvielfalt:** E2E-Modelle aus Sicht von Kunde, Organisation und IT (KOI).
4. **Qualitätssicherung:** Methodische Prüfung von Modellen, auch per ADONIS-REST-API.
5. **Interkommunale Nachnutzung:** Offen (MIT-Lizenz), anpassbar, ohne Lizenzbarrieren für den Ansatz selbst.
6. **Mensch im Loop:** KI unterstützt, Fachexpertise entscheidet. Ergebnisse sind zu prüfen.

### Wording-Leitplanken

- Klar zwischen **Werkzeug** (GitHub Copilot, VS Code) und **Ansatz** (Prompts, Agenten, Regeln) unterscheiden.
- Keine Versprechen wie „vollautomatisch“ oder „fehlerfrei“; stattdessen „unterstützt“, „beschleunigt“, „Entwurf zur fachlichen Prüfung“.
- ADONIS ist ein Produkt der BOC Group, GitHub Copilot ein Produkt von GitHub/Microsoft: Produktnamen nur beschreibend nutzen und einen **Disclaimer** ergänzen (inoffizielles Community-Projekt, keine Partnerschaft oder Zertifizierung, sofern nicht zutreffend).
- Eine GitHub-Copilot-Subscription ist für die Nutzung erforderlich bzw. empfohlen; das transparent kommunizieren (siehe [TECHNISCHE_DOKUMENTATION.md](TECHNISCHE_DOKUMENTATION.md)).

## 3. Zielgruppen

| Zielgruppe | Interesse | Zentrale Botschaft | Bevorzugte Kanäle |
|---|---|---|---|
| **Prozessmanager:innen / Organisationsentwickler:innen** in Kommunen und Verwaltungen | Schnellere Prozessaufnahme, Standardisierung | Ressourcenschonung, Steckbriefe, Interviewagent `Moritz` | LinkedIn, Fachverbände, Newsletter, Webinar |
| **ADONIS-Anwender:innen / BPM-Community** | Import-Kompatibilität, Review-Qualität | ADONIS-kompatibles BPMN, Review per REST-API | LinkedIn, ADONIS-Community-Foren, BPM-Netzwerke |
| **Entwickler:innen / KI-Interessierte** | Technische Umsetzung, Custom Agents, Prompting | Reproduzierbarer Agenten-Workflow, offene Vorlage | GitHub, Blog, Fachforen, Meetups |
| **Entscheider:innen (CIO, Digitalisierung, Organisation)** | Nutzen, Risiko, Wirtschaftlichkeit | Aufwandsreduktion, Interkommunale Skalierbarkeit, Governance | Kurz-Whitepaper, Präsentationen, persönliche Ansprache |
| **Datenschutz / Informationssicherheit** | Umgang mit Daten und KI | Transparenz, keine Verarbeitung personenbezogener Daten nötig (siehe Abschnitt 8) | FAQ, Dokumentation |
| **Multiplikatoren** (Verbände, Kompetenzzentren, Förderprogramme, Presse) | Relevanz, Anschlussfähigkeit | Praxisnaher Beitrag zu KI in der Verwaltung | Direktansprache, Pressemitteilung |

## 4. Vorbereitung (vor dem Launch)

### 4.1 Repository „launch-ready“ machen

- [ ] **README** um Quickstart (3 Schritte bis zum ersten Modell), Screenshot/GIF und Beispielergebnis ergänzen
- [ ] **Disclaimer** (Produktnamen, KI-Ergebnisse müssen fachlich geprüft werden) in README aufnehmen
- [ ] **LICENSE**-Datei im Root vorhanden und konsistent zur README (MIT)
- [ ] **CONTRIBUTING.md**, **CODE_OF_CONDUCT.md** und **SECURITY.md** anlegen
- [ ] **Issue- und PR-Templates** (Bug, Feature, „Neues Praxisbeispiel“) unter `.github` ergänzen
- [ ] **GitHub Discussions** aktivieren (Fragen, Ideen, Erfahrungsberichte)
- [ ] **Topics** setzen, z. B. `bpmn`, `adonis`, `github-copilot`, `process-management`, `public-sector`, `govtech`, `generative-ai`
- [ ] **Social-Preview-Bild** (1280×640 px) hinterlegen
- [ ] **Release v1.0.0** mit Release Notes erstellen
- [ ] Prüfen, dass **keine vertraulichen Daten** (echte Prozessdaten, Zugangsdaten, API-Schlüssel, interne URLs) im Repo und in der Historie enthalten sind
- [ ] Beispielmodelle und Steckbriefe auf Freigabefähigkeit prüfen (Rechte, Anonymisierung)

### 4.2 Interne Abstimmung

- [ ] Freigabe durch Leitung / Rechtsabteilung / Datenschutz / Öffentlichkeitsarbeit (je nach Organisation)
- [ ] Sprechfähigkeit klären: Wer spricht öffentlich, wer beantwortet Anfragen?
- [ ] Abstimmung mit BOC Group bzw. Hinweis, falls ADONIS-Marke prominent genutzt wird
- [ ] Ggf. Abstimmung mit der Pressestelle und der Dienststellenleitung

### 4.3 Content-Paket erstellen

| Baustein | Inhalt | Umfang |
|---|---|---|
| Elevator Pitch | Was, für wen, Nutzen | 2–3 Sätze |
| Projekt-One-Pager | Problem, Lösung, Nutzen, Nachnutzung, Kontakt | 1 Seite |
| Demo-Video | Interview mit `Moritz` → Steckbrief → BPMN-Modell → ADONIS-Import | 2–3 Minuten |
| Screenshots/GIFs | Agentenauswahl, BPMN-Ergebnis, ADONIS-Import, Review-Ergebnis | 4–6 Motive |
| Blogartikel / Fachbeitrag | Hintergrund, Vorgehen, Erkenntnisse, Grenzen | ca. 1.000–1.500 Wörter |
| FAQ | Voraussetzungen, Kosten, Datenschutz, Qualität, Lizenz | 10–15 Fragen |
| Social-Media-Texte | Launch-Post, Folgeposts, Hashtags | 5–8 Texte |
| Präsentationsfolien | Kurzvortrag für Netzwerke/Events | 8–12 Folien |

## 5. Phasenplan

Zeiten relativ zum Veröffentlichungstag **T0** (Termin festzulegen).

### Phase 1 – Vorbereitung (T-4 Wochen bis T-1 Woche)

- Repo-Checkliste (4.1) und interne Freigaben (4.2) abschließen
- Content-Paket (4.3) erstellen
- Kleinen Kreis von **Pilot-Reviewern** (3–5 Personen aus Kommunen/BPM-Community) um Feedback bitten und ggf. um ein Zitat/Statement
- Redaktionsplan und Verantwortlichkeiten festlegen

### Phase 2 – Soft Launch (T-1 Woche bis T0)

- Repo für den Pilotkreis freigeben, Feedback einarbeiten
- Ankündigungstexte final abstimmen
- Journalist:innen/Multiplikatoren mit Embargo-Hinweis vorab informieren (optional)

### Phase 3 – Launch (T0 bis T+1 Woche)

| Zeitpunkt | Maßnahme |
|---|---|
| T0 (Vormittag) | Repository auf **public** stellen, Release v1.0.0 veröffentlichen |
| T0 | Launch-Post auf LinkedIn mit Demo-Video/GIF und Link |
| T0 | Blogartikel/Fachbeitrag veröffentlichen |
| T0 | Direkte Information an Netzwerke, Verbände, Kolleg:innen, Pilotkreis |
| T+1 bis T+3 | Posts in Fachforen/Communities (z. B. ADONIS-/BPM-Community, GovTech- und Open-Source-Netzwerke) |
| T+2 | Folgepost: Anwendungsfall „Prozessaufnahme per Interview mit `Moritz`“ |
| T+5 | Folgepost: Anwendungsfall „Methodisches Review per ADONIS-REST-API“ |
| laufend | Fragen und Kommentare innerhalb von 1–2 Werktagen beantworten |

### Phase 4 – Verstetigung (T+1 Woche bis T+3 Monate)

- Wöchentliche Auswertung der Kennzahlen im ersten Monat, danach monatlich
- **Webinar/Online-Demo** (30–45 Min.) mit Live-Demo und Q&A anbieten
- Erfahrungsberichte und neue Praxisbeispiele aus der Community sichtbar machen (README, Discussions, Release Notes)
- Beiträge bei Fachveranstaltungen, Verbandsformaten und Meetups einreichen
- Regelmäßige Releases mit Changelog, jeweils kurz kommunizieren
- Nach 3 Monaten: Rückblick und Anpassung der Strategie

## 6. Kanäle und Formate

| Kanal | Zweck | Format | Frequenz |
|---|---|---|---|
| **GitHub** (Repo, Releases, Discussions) | Zentrale Anlaufstelle, Mitwirkung | README, Release Notes, Discussions | laufend |
| **LinkedIn** | Reichweite in Verwaltung und BPM-Community | Launch-Post, Kurzvideo, Praxisbeispiele | Launch + ca. 1 Post/Woche in den ersten 4 Wochen |
| **Blog / Fachbeitrag** (eigene Seite, Fachportale, Verbandsmedien) | Tiefe, Einordnung, Vertrauen | Artikel mit Screenshots | Launch + bei Meilensteinen |
| **Fach-Communities und Foren** | Dialog mit Anwender:innen | Vorstellung, Q&A | Launch + anlassbezogen |
| **Newsletter** von Verbänden/Netzwerken | Multiplikation | Kurzmeldung mit Link | einmalig, ggf. Folgebericht |
| **Webinar / Vorträge** | Vertiefung, Demo, Netzwerk | Live-Demo + Q&A | 1× nach Launch, danach anlassbezogen |
| **Pressemitteilung** (optional) | Breite Wahrnehmung | 1 Seite, Zitat, Kontakt | einmalig |
| **YouTube / Videoplattform** (optional) | Demo und Tutorials | Screencasts | nach Bedarf |

## 7. Beispieltexte

### Elevator Pitch

> ADONIS-AI-Forge ist ein offenes Repository, das zeigt, wie sich mit GitHub Copilot und Custom Agents ADONIS-kompatible BPMN-Prozessmodelle, Prozesssteckbriefe und methodische Reviews erstellen lassen – für Verwaltungen, die Prozesse schneller und standardisierter aufnehmen wollen. Nachnutzung ausdrücklich erwünscht.

### LinkedIn-Launch-Post (Entwurf)

> 🚀 **ADONIS-AI-Forge ist jetzt öffentlich!**
>
> Prozessaufnahme ist zeitaufwendig – besonders in der Verwaltung. Wir zeigen, wie generative KI dabei unterstützen kann:
>
> ✅ ADONIS-kompatible BPMN-2.0-Modelle aus Kunden-, Organisations- und IT-Perspektive
> ✅ Geführte Prozessaufnahme per Interview (Agent „Moritz“)
> ✅ Standardisierte Prozesssteckbriefe mit KPIs
> ✅ Methodische Modellprüfung, auch über die ADONIS-REST-API
>
> Alles offen unter MIT-Lizenz und für die interkommunale Nachnutzung gedacht. Die KI liefert Entwürfe – die fachliche Prüfung bleibt beim Menschen.
>
> 👉 [Link zum Repository]
>
> Feedback, Praxisbeispiele und Beiträge sind willkommen!
>
> #BPMN #ADONIS #GitHubCopilot #GovTech #Verwaltungsdigitalisierung #Prozessmanagement #KI

### Kurzmeldung für Newsletter/Verbände (Entwurf)

> **Offener Ansatz für KI-gestützte Prozessmodellierung in der Verwaltung**
> Das Open-Source-Projekt ADONIS-AI-Forge stellt Prompts, Agenten und Regeln bereit, mit denen sich BPMN-Prozessmodelle für ADONIS sowie Prozesssteckbriefe mithilfe von GitHub Copilot erstellen und prüfen lassen. Das Projekt richtet sich an Kommunen und Verwaltungen und lädt zur Nachnutzung und Mitwirkung ein. Mehr unter: [Link]

### Struktur des Blogartikels

1. Ausgangsproblem: Prozessaufnahme kostet Zeit und Ressourcen
2. Idee: Domänenspezifische Agenten statt generischer Prompts
3. Der Workflow in Bildern (Interview → Steckbrief → BPMN → Review → ADONIS-Import)
4. Erkenntnisse und Grenzen (Qualität, Prüfbedarf, Modellabhängigkeit)
5. So starten Sie / so können Sie mitmachen

## 8. Umgang mit Risiken und kritischen Fragen

| Thema | Risiko | Vorbereitete Antwort / Maßnahme |
|---|---|---|
| **Qualität der KI-Ergebnisse** | Erwartung „fertiger“ Modelle | Ergebnisse sind Entwürfe; `ADONIS_Review` und fachliche Prüfung sind Teil des Ansatzes |
| **Datenschutz** | Eingabe sensibler oder personenbezogener Daten in KI-Dienste | Hinweis in Doku/FAQ: keine personenbezogenen oder vertraulichen Daten eingeben; Prozesse abstrakt beschreiben; Datenschutzvorgaben der eigenen Organisation und Copilot-Einstellungen beachten |
| **Kosten / Lizenz** | Unklarheit zu Copilot-Subscription und ADONIS-Lizenz | In FAQ klar benennen: Repo ist MIT-lizenziert, Copilot und ADONIS sind separate Produkte mit eigenen Bedingungen |
| **Marken- und Herstellerbezug** | Eindruck offizieller Unterstützung durch BOC/GitHub/Microsoft | Disclaimer, neutrale Produktnennung, ggf. Vorab-Information an Hersteller |
| **Hohe Erwartungen / Supportanfragen** | Überlastung bei Rückfragen | Support-Erwartung in README/CONTRIBUTING festhalten (Best Effort), FAQ und Discussions nutzen |
| **Kritik an KI in der Verwaltung** | Skepsis (Qualität, Transparenz, Arbeitsplätze) | Sachlich antworten, „Mensch im Loop“ betonen, Methodik offenlegen, Entlastung statt Ersatz |
| **Sicherheitslücken / Fehlkonfiguration** | Offenlegung sensibler Daten im Repo | Vorab-Scan auf Secrets, SECURITY.md mit Meldeweg |

### Reaktionsregeln

- Antwort auf Fragen und Kritik innerhalb von **1–2 Werktagen**, sachlich und mit Verweis auf Dokumentation
- Fehler offen einräumen und im Changelog dokumentieren
- Eskalation bei Presseanfragen, Rechts- oder Datenschutzfragen an die vorab benannten Verantwortlichen
- Verhaltensregeln (Code of Conduct) konsequent anwenden

## 9. Rollen und Verantwortlichkeiten (auszufüllen)

| Rolle | Aufgabe | Verantwortlich |
|---|---|---|
| Projektleitung | Gesamtverantwortung, Freigaben | _tbd_ |
| Repo-Maintainer | Repo, Releases, Issues/PRs, Discussions | _tbd_ |
| Kommunikation | Texte, Kanäle, Redaktionsplan, Pressekontakt | _tbd_ |
| Fachliche Expertise | Inhaltliche Beantwortung, Webinar, Vorträge | _tbd_ |
| Datenschutz / Recht | Freigabe, Disclaimer, Marken | _tbd_ |

## 10. Erfolgsmessung

| Kennzahl | Quelle | Zielwert nach 3 Monaten (Vorschlag) |
|---|---|---|
| Stars / Watchers | GitHub | _festzulegen_ |
| Forks / Clones | GitHub Insights | _festzulegen_ |
| Besucher:innen und Referrer | GitHub Traffic | _festzulegen_ |
| Issues, Discussions, PRs von Externen | GitHub | _festzulegen_ |
| Reichweite / Interaktionen der Beiträge | LinkedIn Analytics | _festzulegen_ |
| Webinar-Teilnehmende | Veranstaltungstool | _festzulegen_ |
| Gemeldete Nachnutzungen / Praxisbeispiele | Discussions, Direktfeedback | _festzulegen_ |
| Erwähnungen in Medien, Vorträge, Einladungen | Monitoring | _festzulegen_ |

Auswertung: wöchentlich im ersten Monat, danach monatlich; Rückblick mit Anpassung der Maßnahmen nach 3 Monaten.

## 11. Zeit- und Aufgabenübersicht (Checkliste)

- [ ] Launch-Termin T0 festlegen
- [ ] Verantwortlichkeiten (Abschnitt 9) klären
- [ ] Repo-Checkliste (4.1) abarbeiten
- [ ] Freigaben (4.2) einholen
- [ ] Content-Paket (4.3) erstellen
- [ ] Pilotkreis einbinden und Feedback einarbeiten
- [ ] Repo veröffentlichen, Release v1.0.0 erstellen
- [ ] Launch-Beiträge veröffentlichen und Multiplikatoren informieren
- [ ] Webinar planen und durchführen
- [ ] Kennzahlen auswerten und Strategie nach 3 Monaten überprüfen
