# Technische Dokumentation - GovModeler

## Übersicht
Diese Dokumentation beschreibt die technischen Grundlagen und Voraussetzungen zur Nutzung des GovModelers für die KI-gestützte Erstellung von BPMN-Prozessmodellen.

## Systemvoraussetzungen

### Software-Anforderungen
- **Visual Studio Code** (Version 1.80 oder höher)
- **GitHub Copilot Subscription** (optional)

### Betriebssystem
- Windows 10/11
- macOS 10.15 oder höher
- Linux (Ubuntu 20.04 oder höher empfohlen)

## Erforderliche VS Code Extensions

### 1. GitHub Copilot (erforderlich)
**Extension ID:** `GitHub.copilot`

**Zweck:** KI-gestützte Code- und BPMN-Generierung


### 2. GitHub Copilot Chat (erforderlich)
**Extension ID:** `GitHub.copilot-chat`

**Zweck:** Interaktive Kommunikation mit Copilot für Prozessmodellierung


### 3. Camunda Modeler by Miragon (erforderlich)
**Extension ID:** `miragon-gmbh.vs-code-bpmn-modeler`

**Zweck:** Visuelle Darstellung, Simulierung und Bearbeitung von BPMN-Diagrammen


### 4. GitHub Pull Requests (empfohlen)
**Extension ID:** `github.vscode-pull-request-github`

**Zweck:** Review and manage your GitHub pull requests and issues directly in VS Code


### 5. GitHub Repositories (empfohlen)
**Extension ID:** `github.remotehub`

**Zweck:** The GitHub Repositories extension lets you quickly browse, search, edit, and commit to any remote GitHub repository directly from within Visual Studio Code.

### 6. Camunda Forms Editor (erforderlich)
**Extension ID:** `davidmart.camunda-forms-editor`

**Zweck:** Der Editor wird benötigt, um Formualare zu erstellen

### 6. VS Code Speech (optional)
**Extension ID:** `ms-vscode.vscode-speech`

**Zweck:** A VS Code extension to bring speech-to-text and other voice capabilities to VS Code.

### 7. German language support for VS Code Speech (optional)
**Extension ID:** `ms-vscode.vscode-speech-language-pack-de-de`

**Zweck:** German language support for speech-to-text and other voice capabilities in VS Code.


## BPMN-Generierung mit Copilot Chat
1. Öffnen Sie Copilot Chat (`Ctrl+Alt+I` / `Cmd+Alt+I`)
2. KI-Modell auswählen
3. Agenten auswählen (KOI, KO, I, Forms)
4. Prozess benennen oder einsprechen

## Form-Generierung mit Copilot Chat
1. Agent "Forms" auswählen
2. Aktivität im BPMN-Modell benennen für das ein Formular erstellt werden soll

## Prozesssteckbrief-Generierung mit Copilot Chat
1. Agent "Steckbrief" auswählen
2. Erstellung über Prompt anstoßen, z. B. "Erstelle Steckbrief"

## Troubleshooting

### Problem: Copilot bricht ab und generiert kein BPMN (Timeout)
**Lösung:** 
- Über Prompt klarstellen, dass ein vereinfachtes Prozessnmodell erstellt werden soll
- anderes KI-Modell auswählen
- es an einem anderen Tag wieder versuchen
  
## Support und Kontakt

Bei Fragen oder Problemen:
- GitHub Issues: https://github.com/ovaltinetippins/GovModeler_KOI/issues
- Projektverantwortliche kontaktieren

---

**Stand:** Januar 2026  
**Version:** 1.3


