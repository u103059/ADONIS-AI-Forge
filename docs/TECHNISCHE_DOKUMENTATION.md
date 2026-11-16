# Technische Dokumentation - ADONIS-AI-Forge

## Übersicht
Diese Dokumentation beschreibt die technischen Grundlagen und Voraussetzungen zur Nutzung von ADONIS-AI-Forge für die KI-gestützte Erstellung ADONIS-kompatibler BPMN-Prozessmodelle, Prozesssteckbriefe, methodische Reviews und geführte Prozessaufnahmen.

## Systemvoraussetzungen

### Software-Anforderungen
- **Visual Studio Code** (aktuelle Version mit Unterstützung für Custom Agents / `.agent.md`)
- **GitHub Copilot Subscription** (optional)

### Betriebssystem
- Windows 10/11
- macOS 10.15 oder höher
- Linux (Ubuntu 20.04 oder höher empfohlen)

## Erforderliche VS Code Extensions

### 1. GitHub Copilot Chat (erforderlich)
**Extension ID:** `GitHub.copilot-chat`

**Zweck:** KI-gestützte BPMN-Generierung und interaktive Kommunikation mit den Agenten (enthält die frühere Extension `GitHub.copilot`)


### 2. Camunda Modeler by Miragon (erforderlich)
**Extension ID:** `miragon-gmbh.vs-code-bpmn-modeler`

**Zweck:** Visuelle Darstellung, Simulierung und Bearbeitung von BPMN-Diagrammen


### 3. GitHub Pull Requests (empfohlen)
**Extension ID:** `github.vscode-pull-request-github`

**Zweck:** Pull Requests und Issues direkt in VS Code prüfen und verwalten


### 4. GitHub Repositories (empfohlen)
**Extension ID:** `github.remotehub`

**Zweck:** Remote-GitHub-Repositories direkt in VS Code durchsuchen, bearbeiten und committen, ohne lokalen Clone

> **Achtung:** Für die Nutzung der Agenten wird ein **lokaler Clone** benötigt. Der Copilot-Harness läuft im Agent Host neben dem lokalen Workspace und findet die Agenten unter `.github/agents` in einem über „GitHub Repositories“ geöffneten (virtuellen) Workspace nicht – sie erscheinen dann nicht in der Agent-Auswahl.

### 5. VS Code Speech (optional)
**Extension ID:** `ms-vscode.vscode-speech`

**Zweck:** Spracheingabe (Speech-to-Text) in VS Code und Copilot Chat

### 6. German language support for VS Code Speech (optional)
**Extension ID:** `ms-vscode.vscode-speech-language-pack-de-de`

**Zweck:** Deutsche Sprachunterstützung für VS Code Speech


## Verfügbare Agenten

| Agent | Zweck |
|---|---|
| `ADONIS_BPMN_KO` | Prozessmodell mit den Pools Kunde und Organisation (ADONIS-Import-kompatibel) |
| `ADONIS_BPMN_KOI` | Prozessmodell mit den Pools Kunde, IT und Organisation (ADONIS-Import-kompatibel) |
| `ADONIS_BPMN_I` | IT-Datenverarbeitung über mehrere IT-System-Pools mit Nachrichtenflüssen (ADONIS-Import-kompatibel) |
| `Steckbrief` | Prozesssteckbrief mit Prozess- und Aktivitäts-KPIs auf Basis des Templates |
| `ADONIS_Review` | Methodische Prüfung von ADONIS-Prozessmodellen (BPMN 2.0, ADONIS-Kompatibilität, GPM-Standards) |
| `Moritz` | Geführtes Interview zur Ist-Prozessaufnahme mit Steckbrief und BPMN-Ist-Modell |

> **Hinweis:** Die Agenten sind für den **Copilot**-Harness konfiguriert (Session Target „Copilot“ im Chat). In den `tools`-Listen der `.agent.md`-Dateien nur die Copilot-Aliasse (`read`, `edit`, `search`, `execute`, `web`, `todo`, `agent`) verwenden – Local-spezifische Tool-Namen wie `edit/createFile` oder `execute/runInTerminal` und Felder wie `argument-hint` bzw. `handoffs` führen dazu, dass die Agenten nicht im Agent-Dropdown erscheinen.

## BPMN-Generierung mit Copilot Chat
1. Öffnen Sie Copilot Chat (`Ctrl+Alt+I` / `Cmd+Alt+I`)
2. KI-Modell auswählen
3. Passenden BPMN-Agenten auswählen (siehe [Verfügbare Agenten](#verfügbare-agenten))
4. Prozess benennen oder einsprechen

## Prozesssteckbrief-Generierung mit Copilot Chat
1. Agent "Steckbrief" auswählen
2. Erstellung über Prompt anstoßen, z. B. "Erstelle Steckbrief"

## Geführte Prozessaufnahme mit Moritz
1. Agent "Moritz" auswählen
2. Namen des aufzunehmenden Prozesses eingeben, z. B. "Starte Prozessaufnahme Wohngeld beantragen"
3. Die Interviewfragen beantworten (optional per Spracheingabe)
4. Ergebnis: Prozesssteckbrief und ADONIS-kompatibles BPMN-Ist-Prozessmodell (ein Pool Organisation mit Lanes)

## Troubleshooting

### Problem: Copilot bricht ab und generiert kein BPMN (Timeout)
**Lösung:** 
- Über Prompt klarstellen, dass ein vereinfachtes Prozessmodell erstellt werden soll
- anderes KI-Modell auswählen
- es an einem anderen Tag wieder versuchen
  
## Support und Kontakt

Bei Fragen oder Problemen:
- Projektverantwortliche kontaktieren

---

**Stand:** November 2026  
**Version:** 1.4


