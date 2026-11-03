---
description: 'Use when: creating, editing or reviewing BPMN models, documenting tasks and activities, or storing task information in Documentation - Element documentation. Applies to standard BPMN and ADONIS models.'
applyTo: '**/*.bpmn'
---

# Taskinformationen in der Elementdokumentation

- Bei der Erstellung eines BPMN-Modells die fachliche Beschreibung jeder Aktivitaet am zugehoerigen Task speichern. Bei Bearbeitungen vorhandene Dokumentation erhalten und fuer neue oder fachlich geaenderte Tasks aktualisieren.
- Ziel in den Objekteigenschaften ist **Documentation - Element documentation**. Im BPMN-XML dafuer das standardisierte Element `bpmn:documentation` als direktes Kind des jeweiligen Tasks verwenden, nicht am Prozess oder an der Collaboration.
- Die Regel gilt fuer alle Tasktypen, insbesondere `task`, `userTask`, `serviceTask`, `manualTask`, `businessRuleTask`, `scriptTask`, `sendTask` und `receiveTask`, auch innerhalb von Subprozessen.
- Die vorhandene Aktivitaetsbeschreibung aus der Prozessbeschreibung uebernehmen. Zweck, Bearbeitung und Ergebnis sowie bekannte Eingaben, Systeme oder fachliche Vorgaben knapp beschreiben, soweit diese Informationen vorliegen. Keine unbelegten Details erfinden.
- Das `name`-Attribut bleibt eine kurze Benennung der Aktivitaet. Die Dokumentation darf nicht nur den Tasknamen wiederholen. Beschreibungen im Chat, Prozesssteckbrief oder in Textannotationen ersetzen die Elementdokumentation nicht.
- Vorhandene Dokumentation nicht durch leere Inhalte oder Vorlagenplatzhalter ersetzen. Platzhalter aus Templates im erzeugten Modell durch prozessbezogene Beschreibungen ersetzen.
- Klartext mit `textFormat="text/plain"` verwenden und XML-Sonderzeichen korrekt maskieren, insbesondere `&` als `&amp;` und `<` als `&lt;`. Bestehende Sprach- und Umlautkonventionen des Modells beachten.
- `documentation` vor etwaigen `extensionElements`, `incoming` und `outgoing` einfuegen. Die bestehende Namespace-Konvention beibehalten: Bei BPMN als Default-Namespace ist `<documentation>` gleichbedeutend mit `<bpmn:documentation>`.

## XML-Beispiel

```xml
<bpmn:userTask id="Task_Antrag_pruefen" name="Antrag pruefen">
  <bpmn:documentation textFormat="text/plain">Die Sachbearbeitung prueft den eingegangenen Antrag und die beigefuegten Nachweise auf Vollstaendigkeit. Das Pruefergebnis wird fuer die weitere Bearbeitung festgehalten.</bpmn:documentation>
  <bpmn:incoming>Flow_1</bpmn:incoming>
  <bpmn:outgoing>Flow_2</bpmn:outgoing>
</bpmn:userTask>
```

## Qualitaetspruefung

- Jeder neu erstellte oder fachlich geaenderte Task hat eine nicht leere, passende fachliche Elementdokumentation im BPMN-Namespace. Bestehende Luecken bei Reviews als Befund benennen, nicht ohne Auftrag alle Bestandsmodelle migrieren.
- Dokumentation ist direkt dem richtigen Task zugeordnet; XML-Escaping, Elementreihenfolge und Namespace sind korrekt. Im fertigen Modell verbleiben keine Dokumentationsplatzhalter.
- Fuer ADONIS ist die Zuordnung des standardisierten `documentation`-Elements zum UI-Feld **Documentation - Element documentation** anhand der vorhandenen Repository-Beispiele noch nicht bestaetigt. Bei einer Importpruefung einen eindeutigen Testtext im Zielfeld speichern, exportieren und die XML-Zuordnung vergleichen; anschliessend den Import und die Anzeige desselben Textes im Zielfeld pruefen.
- Keine ADONIS-spezifischen Dokumentations-Extensions ohne belegte Zuordnung aus einem Export erfinden. Ohne Import-/Exportpruefung die UI-Zuordnung als unbestaetigt ausweisen, nicht als erfolgreich getestet melden.