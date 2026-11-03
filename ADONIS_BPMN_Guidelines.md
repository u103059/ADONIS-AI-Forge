# ADONIS BPMN Guidelines: Modellierungsrichtlinien für BPMN-Prozessmodelle

## Überblick

Diese Guidelines definieren die Modellierungsregeln für BPMN 2.0 Prozessmodelle, die in der Prozessmanagement-Software **ADONIS** (BOC Group) erstellt und importiert werden. Die Modelle folgen dem **KOI-Prinzip** (Kunde – Organisation – IT) und werden als Ende-zu-Ende-Prozesse (e2e) abgebildet.

### Referenzdokumente
- ADONIS BPMN Template: `BPMN_ADONIS/BPMN_ADONIS_Template.xml`
- ADONIS Beispielmodelle: `BPMN_ADONIS/`
- GPM-Handbuch der LHS Stuttgart

---

## 1. ADONIS-spezifische Namespace-Definitionen

### Erforderliche Namespaces für ADONIS-Import
```xml
<definitions xmlns="http://www.omg.org/spec/BPMN/20100524/MODEL"
             xmlns:adonis="http://www.boc-group.com"
             xmlns:bpmn="http://www.omg.org/spec/BPMN/20100524/MODEL"
             xmlns:bpmndi="http://www.omg.org/spec/BPMN/20100524/DI"
             xmlns:omgdc="http://www.omg.org/spec/DD/20100524/DC"
             xmlns:omgdi="http://www.omg.org/spec/DD/20100524/DI"
             xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
             id="definition__[UUID]"
             typeLanguage="http://www.w3.org/2001/XMLSchema"
             xsi:schemaLocation="http://www.omg.org/spec/BPMN/20100524/MODEL http://www.omg.org/spec/BPMN/2.0/20100501/BPMN20.xsd"
             targetNamespace="http://www.boc-group.com">
```

### Wichtige Unterschiede zum Standard-BPMN
| Aspekt | Standard-BPMN | ADONIS-BPMN |
|--------|--------------|-------------|
| Namespace DI-Koordinaten | `dc:` / `di:` | `omgdc:` / `omgdi:` |
| Target-Namespace | beliebig | `http://www.boc-group.com` |
| ADONIS-Namespace | nicht vorhanden | `xmlns:adonis="http://www.boc-group.com"` |
| ID-Format | frei wählbar | GUID mit Unterstrich-Präfix: `_[UUID]` |
| Extension-Elements | optional | `adonis:extensionElements` werden bei Import ergänzt |

---

## 2. KOI-Modell: Prozessstruktur

### Grundprinzip
Das **KOI-Modell** definiert die Struktur für Ende-zu-Ende-Prozesse (e2e) mit drei Beteiligten:

| Pool | Beschreibung | Rolle im Prozess |
|------|-------------|-----------------|
| **Kunde** | Interner oder externer Auslöser des Prozesses | Initiiert den Prozess, empfängt das Ergebnis |
| **Organisation** | Verwaltungseinheit, die den Prozess durchführt | Kernprozessausführung |
| **IT** | Fachanwendungen und IT-Systeme | Datenverarbeitung, automatisierte Schritte |

### e2e-Prozess-Prinzipien
- Start- und Endereignis leiten sich **immer vom Kunden** ab
- Die Identifizierung erfolgt über das Unternehmensprozessmodell (UPM)
- Alle Aktivitäten aller Prozessbeteiligten werden dargestellt
- Nur e2e-Prozesse werden als Referenzprozesse im UPM verlinkt

### Pool-Varianten
- **Kunde**: Kann als **Blackbox-Pool** (ohne interne Prozessschritte) oder als Pool mit Lanes modelliert werden
- **Organisation**: Wird immer als Pool mit mindestens einer Lane modelliert; Lanes repräsentieren Rollen/Organisationseinheiten (Schwimmbahnen)
- **IT**: Kann bei Bedarf als **Blackbox-Pool** oder als Pool mit Lanes modelliert werden

---

## 3. Pool-Farben (ADONIS-Konvention)

Die Pool-Farben folgen dem ADONIS-Farbschema und dienen der schnellen visuellen Zuordnung:

| Pool | Farbe | Beschreibung |
|------|-------|-------------|
| **Kunde** | Blau | Externer/interner Auftraggeber |
| **Organisation** | Grün | Verwaltungseinheit/Behörde |
| **IT** | Orange | Fachanwendungen/IT-Systeme |

> **Hinweis**: Die Farbzuordnung erfolgt in ADONIS über die grafische Oberfläche. In der BPMN-XML werden keine Farbattribute exportiert – die Farben werden beim Import in ADONIS automatisch zugewiesen.

---

## 4. Pool-Anordnung und Dimensionen

### Vertikale Pool-Anordnung (KOI-Reihenfolge)
```
┌────────────────────────────────────────────────────┐
│  Kunde (oben)              y = 0,   Höhe = 380px   │
├────────────────────────────────────────────────────┤
│  (Abstand: 10px)                                    │
├────────────────────────────────────────────────────┤
│  IT (Mitte)                y = 390, Höhe = 380px   │
├────────────────────────────────────────────────────┤
│  (Abstand: 10px)                                    │
├────────────────────────────────────────────────────┤
│  Organisation (unten)      y = 780, Höhe = 380px   │
└────────────────────────────────────────────────────┘
```

### Standard-Dimensionen

#### Pools
```xml
<!-- Pool: Breite 1830px, Höhe 380px -->
<omgdc:Bounds x="10" y="[Y_POSITION]" width="1830" height="380"/>

<!-- Lane innerhalb Pool: Breite 1800px (Pool - 30px für Pool-Header) -->
<omgdc:Bounds x="40" y="[Y_POSITION]" width="1800" height="380"/>
```

#### Y-Positionen der Pools
| Pool | Pool y-Position | Lane y-Position |
|------|----------------|-----------------|
| Kunde | 0 | 0 |
| IT | 390 | 390 |
| Organisation | 780 | 780 |

#### Abstand zwischen Pools
- **10px** Abstand zwischen aufeinanderfolgenden Pools

### Pool-Dimensionsübersicht
| Element | x | y | Breite | Höhe |
|---------|---|---|--------|------|
| Pool (Kunde) | 10 | 0 | 1830 | 380 |
| Lane (Kunde) | 40 | 0 | 1800 | 380 |
| Pool (IT) | 10 | 390 | 1830 | 380 |
| Lane (IT) | 40 | 390 | 1800 | 380 |
| Pool (Organisation) | 10 | 780 | 1830 | 380 |
| Lane (Organisation) | 40 | 780 | 1800 | 380 |

---

## 5. Element-Dimensionen

### Standard-Größen (ADONIS-Format)

| Element | Breite | Höhe | Hinweis |
|---------|--------|------|---------|
| **Task** (alle Typen) | 151 | 76 | Größer als Standard-BPMN (100×80) |
| **Start Event** | 36 | 36 | Standard BPMN-Größe |
| **End Event** | 36 | 36 | Standard BPMN-Größe |
| **Intermediate Event** | 36 | 36 | Standard BPMN-Größe |
| **Gateway** (XOR, AND, OR) | 56 | 56 | Größer als Standard-BPMN (50×50) |

> **Wichtig**: ADONIS-Modelle verwenden Task-Dimensionen von **151×76px** und Gateway-Dimensionen von **56×56px**. Dies weicht vom reinen BPMN-Standard (100×80 bzw. 50×50) ab.

---

## 6. Horizontale Positionierung innerhalb der Pools

### Y-Koordinaten-Standards für Elemente

Die Y-Koordinaten für Elemente innerhalb eines Pools berechnen sich relativ zur Pool-Oberkante. Die Elemente werden vertikal zentriert in der Pool-Mitte platziert.

| Pool | Task y | Event y | Gateway y | Zentrierungs-Y |
|------|--------|---------|-----------|---------------|
| **Kunde** (y=0, h=380) | 152 | 172 | 162 | 190 |
| **IT** (y=390, h=380) | 542 | 562 | 552 | 580 |
| **Organisation** (y=780, h=380) | 932 | 952 | 942 | 970 |

### Berechnungsformel
```
Task-Y       = Pool-Y + (Pool-Höhe / 2) - (Task-Höhe / 2)  = Pool-Y + 152
Event-Y      = Pool-Y + (Pool-Höhe / 2) - (Event-Höhe / 2) = Pool-Y + 172
Gateway-Y    = Pool-Y + (Pool-Höhe / 2) - (Gateway-Höhe / 2) = Pool-Y + 162
Zentrierung  = Pool-Y + (Pool-Höhe / 2)                     = Pool-Y + 190
```

### Horizontale Task-Anordnung (OBLIGATORISCH)
- **Alle Tasks** in einem Pool verwenden **exakt dieselbe Y-Koordinate**
- Workflow-Elemente folgen einer strikten **Links-nach-Rechts-Anordnung**
- Vertikale Verschiebungen von Tasks sind **nicht erlaubt**
- **X-Abstände**: Minimum 60–80px zwischen Elementen

### Beispiel: Task-Positionierung im Kunde-Pool
```xml
<!-- Start Event -->
<omgdc:Bounds x="120" y="172" width="36" height="36"/>
<!-- Task 1 -->
<omgdc:Bounds x="220" y="152" width="151" height="76"/>
<!-- Task 2 -->
<omgdc:Bounds x="440" y="152" width="151" height="76"/>
<!-- End Event -->
<omgdc:Bounds x="660" y="172" width="36" height="36"/>
```

---

## 7. ID-Konventionen

### ADONIS GUID-Format
Alle IDs in ADONIS-kompatiblen BPMN-Dateien verwenden das GUID-Format mit Unterstrich-Präfix:

```
_[UUID]
Beispiel: _4fa5a368-d049-44be-9953-e9616567fa8b
```

### ID-Zuordnungen
| Element | ID-Format | Beispiel |
|---------|-----------|---------|
| Definition | `definition__[UUID]` | `definition__80c86e00-537e-4a54-...` |
| Collaboration | `Collaboration_[UUID]` | `Collaboration_80c86e00-537e-...` |
| Participant | `_[UUID]` | `_4fa5a368-d049-44be-...` |
| Process | `process_[UUID]` | `process_4fa5a368-d049-...` |
| Lane | `_[UUID]` | `_a1b2c3d4-e5f6-...` |
| Task/Event/Gateway | `_[UUID]` | `_2ab0a752-1b75-...` |
| Sequence Flow | `_[UUID]` | `_070b0d1f-b80d-...` |
| Message Flow | `_[UUID]` | `_ac4c488f-5e30-...` |
| LaneSet | `laneSet_[UUID]` | `laneSet_4fa5a368-...` |

---

## 8. Collaboration und Message Flows

### Collaboration-Struktur
```xml
<collaboration id="Collaboration_[UUID]"
               name="[PROZESSNAME]"
               isClosed="false">
  <participant processRef="process_[KUNDE_UUID]"     name="Kunde"        id="_[UUID]"/>
  <participant processRef="process_[IT_UUID]"         name="IT"           id="_[UUID]"/>
  <participant processRef="process_[ORG_UUID]"        name="Organisation" id="_[UUID]"/>

  <!-- Message Flows zwischen Pools -->
  <messageFlow id="_[UUID]" sourceRef="_[ELEMENT]" targetRef="_[ELEMENT]"/>
</collaboration>
```

### Typische Message-Flow-Muster im KOI-Modell
| Von | Nach | Beispiel |
|-----|------|---------|
| Kunde → Organisation | Antrag einreichen | Antrag, Anfrage, Dokumente |
| Organisation → IT | Datenverarbeitungsauftrag | Verarbeitungsauftrag |
| IT → Organisation | Verarbeitungsergebnis | Daten, Bescheid-Daten |
| Organisation → Kunde | Bescheid/Ergebnis | Bewilligung, Ablehnung |

### Message-Flow-Routing (BPMN-DI)
Message Flows zwischen Pools werden über **Waypoints** mit Zwischenpunkten an den Pool-Grenzen geroutet:

```xml
<!-- Kunde → Organisation (kreuzt IT-Pool) -->
<bpmndi:BPMNEdge bpmnElement="_[MSGFLOW_UUID]">
  <omgdi:waypoint x="295" y="228"/>   <!-- Unterkante Kunde-Element -->
  <omgdi:waypoint x="295" y="780"/>   <!-- Oberkante Organisation-Pool -->
  <omgdi:waypoint x="138" y="780"/>   <!-- Horizontale Verschiebung -->
  <omgdi:waypoint x="138" y="952"/>   <!-- Ziel-Element in Organisation -->
</bpmndi:BPMNEdge>
```

---

## 9. Prozess-Elemente

### Process-Grundstruktur
```xml
<process name="[POOL_NAME]"
         id="process_[UUID]"
         isExecutable="false"
         isClosed="false"
         processType="None">
  <laneSet id="laneSet_[UUID]">
    <lane name="[LANE_NAME]" id="_[UUID]">
      <flowNodeRef>_[ELEMENT_UUID]</flowNodeRef>
      <!-- Weitere flowNodeRef -->
    </lane>
  </laneSet>
  <!-- Start Event, Tasks, End Event, Sequence Flows -->
</process>
```

### Prozess-Attribute
- `isExecutable="false"` — Modelle sind nicht für Engine-Ausführung vorgesehen
- `isClosed="false"` — Standard für ADONIS
- `processType="None"` — Standard-Prozesstyp
- `isForCompensation="false"` — Standard für Tasks

### Start-/End-Events im KOI-Modell
| Pool | Typisches Start-Event | Typisches End-Event |
|------|----------------------|---------------------|
| **Kunde** | None Start Event | None End Event |
| **IT** | Message Start Event | None/Message End Event |
| **Organisation** | Message Start Event | None End Event |

> **Hinweis**: IT- und Organisations-Pools starten häufig mit Message-Start-Events, da sie durch eine Nachricht vom jeweils anderen Pool ausgelöst werden.

---

## 10. Sequence Flows (BPMN-DI)

### Grundstruktur
```xml
<bpmndi:BPMNEdge bpmnElement="_[FLOW_UUID]">
  <omgdi:waypoint x="[X_START]" y="[Y_CENTER]"/>
  <omgdi:waypoint x="[X_END]" y="[Y_CENTER]"/>
</bpmndi:BPMNEdge>
```

### Waypoint-Berechnung
- **Horizontale Flows**: Start-X = Element-X + Element-Breite; End-X = nächstes Element-X
- **Y-Koordinate**: Zentrierung des Elements (Pool-Y + 190 für alle Pools)

```xml
<!-- Beispiel: Start Event → Task im Kunde-Pool -->
<bpmndi:BPMNEdge bpmnElement="_[FLOW_UUID]">
  <omgdi:waypoint x="156" y="190"/>  <!-- Start Event rechter Rand: 120 + 36 = 156 -->
  <omgdi:waypoint x="220" y="190"/>  <!-- Task linker Rand: x=220 -->
</bpmndi:BPMNEdge>

<!-- Beispiel: Task → End Event im Kunde-Pool -->
<bpmndi:BPMNEdge bpmnElement="_[FLOW_UUID]">
  <omgdi:waypoint x="371" y="190"/>  <!-- Task rechter Rand: 220 + 151 = 371 -->
  <omgdi:waypoint x="440" y="190"/>  <!-- End Event linker Rand: x=440 -->
</bpmndi:BPMNEdge>
```

---

## 11. Labels (BPMNLabel)

### Positionierungsregeln
- **Events**: Label unterhalb des Elements, Breite 60px, Höhe 40px
- **Tasks**: Label innerhalb des Task-Shapes (kein separates BPMNLabel nötig)
- **Gateways**: Label oberhalb oder seitlich, Breite 60px, Höhe 40px
- **Pools/Lanes**: Label vertikal am linken Rand (automatisch durch `isHorizontal="true"`)

### Label-Dimensionen (ADONIS-Standard)
```xml
<!-- Event-Label -->
<bpmndi:BPMNLabel>
  <omgdc:Bounds x="[LABEL_X]" y="[LABEL_Y]" width="60" height="40"/>
</bpmndi:BPMNLabel>

<!-- Gateway-Label -->
<bpmndi:BPMNLabel>
  <omgdc:Bounds x="[LABEL_X]" y="[LABEL_Y]" width="60" height="40"/>
</bpmndi:BPMNLabel>
```

---

## 12. ADONIS Extension Elements

### Modell-Attribute
ADONIS fügt beim Export `extensionElements` mit spezifischen Modell-Attributen hinzu:

```xml
<extensionElements>
  <adonis:modelattributes>
    <adonis:attribute name="A_COMPLIANCE" type="ENUM" ...>
      <adonis:value>Kein Eintrag</adonis:value>
    </adonis:attribute>
    <!-- Weitere Attribute: A_PROCESS_MANAGEMENT_MATURITY, A_MONITORING_NCS, etc. -->
  </adonis:modelattributes>
</extensionElements>
```

### Connector-Attribute
```xml
<extensionElements>
  <adonis:connector>
    <adonis:attribute name="DISPLAY_DENOMNIATION" .../>
  </adonis:connector>
</extensionElements>
```

> **Hinweis**: Diese Extension-Elemente werden bei Import in ADONIS automatisch ergänzt. Beim Erstellen neuer Modelle müssen sie nicht manuell hinzugefügt werden.

---

## 13. Lanes und Schwimmbahnen

### Lanes für Rollen und Verantwortlichkeiten
Lanes (Schwimmbahnen) innerhalb eines Pools repräsentieren **Rollen** oder **Organisationseinheiten**:

```xml
<laneSet id="laneSet_[UUID]">
  <lane name="Sachbearbeitung" id="_[UUID]">
    <flowNodeRef>_[TASK1_UUID]</flowNodeRef>
    <flowNodeRef>_[TASK2_UUID]</flowNodeRef>
  </lane>
  <lane name="Sachgebietsleitung" id="_[UUID]">
    <flowNodeRef>_[TASK3_UUID]</flowNodeRef>
  </lane>
</laneSet>
```

### Lane-Benennungskonvention
- Rollenbezeichnungen verwenden (z. B. "Sachbearbeitung", "Sachgebietsleitung")
- **Nicht** nach Personen, sondern nach Funktionen benennen
- Lanes im Organisations-Pool sind typisch; Kunde-Pool hat oft nur eine Lane

---

## 14. Mehrere Lanes pro Pool (Multi-Lane-Layout)

Bei mehreren Lanes innerhalb eines Pools wird die Pool-Höhe gleichmäßig aufgeteilt:

### 2 Lanes pro Pool
```xml
<!-- Pool gesamt: Höhe 380px -->
<omgdc:Bounds x="10"  y="780" width="1830" height="380"/>
<!-- Lane 1: Höhe 190px -->
<omgdc:Bounds x="40"  y="780" width="1800" height="190"/>
<!-- Lane 2: Höhe 190px -->
<omgdc:Bounds x="40"  y="970" width="1800" height="190"/>
```

### Pool-Höhe bei vielen Lanes
Bei mehr als 2 Lanes kann die Pool-Höhe proportional vergrößert werden. Die Y-Positionen der nachfolgenden Pools verschieben sich entsprechend.

---

## 15. Gateway-Typen und Darstellung

### Unterstützte Gateways
| Gateway | BPMN-Element | isMarkerVisible | Verwendung |
|---------|-------------|-----------------|-----------|
| Exklusiv (XOR) | `exclusiveGateway` | `true` | Entweder/Oder-Entscheidung |
| Parallel (AND) | `parallelGateway` | — | Alle Pfade gleichzeitig |
| Inklusiv (OR) | `inclusiveGateway` | `true` | Mindestens ein Pfad |
| Ereignisbasiert | `eventBasedGateway` | — | Wartet auf eintreffende Ereignisse |

### Gateway-Positionierung
```xml
<!-- Gateway im Organisations-Pool -->
<bpmndi:BPMNShape bpmnElement="_[GATEWAY_UUID]">
  <omgdc:Bounds x="[X]" y="942" width="56" height="56"/>
</bpmndi:BPMNShape>
```

---

## 16. Best Practices

### Konsistenz
- Einheitliches GUID-Format für alle IDs
- Konsistente Pool-Dimensionen (1830×380)
- Gleiche Abstände zwischen Elementen
- **OBLIGATORISCH**: Alle Tasks in einem Pool auf identischer Y-Koordinate

### Lesbarkeit
- Logischer Fluss von **links nach rechts** (OBLIGATORISCH)
- Vermeidung von Linienkreuzungen bei Sequence Flows
- Message Flows klar zwischen Pools routen
- Aussagekräftige Elementnamen (z. B. "Antrag prüfen" statt "Task 1")

### ADONIS-Kompatibilität
- `targetNamespace="http://www.boc-group.com"` verwenden
- `omgdc:`/`omgdi:` Präfixe statt `dc:`/`di:`
- GUID-Format für alle IDs
- `isHorizontal="true"` für Pools und Lanes
- `isExecutable="false"` für alle Prozesse

### Wartbarkeit
- Klare Prozessnamen im Collaboration-Element
- Modularer Aufbau bei komplexen Prozessen (Sub-Prozesse)
- Kommentare im XML bei komplexen Message-Flow-Routings

### Validierung
- Alle `bpmnElement`-Referenzen müssen auf existierende Elemente verweisen
- Jede Lane muss alle zugeordneten `flowNodeRef`-Elemente enthalten
- Waypoints müssen geometrisch sinnvoll sein (innerhalb der Pool-Grenzen)
- Tasks MÜSSEN auf identischer Y-Koordinate pro Pool positioniert sein

---

## 17. Zusammenfassung: Checkliste für neue Prozessmodelle

- [ ] KOI-Struktur: 3 Pools (Kunde, Organisation, IT)
- [ ] Pool-Reihenfolge: Kunde (oben) → IT (Mitte) → Organisation (unten)
- [ ] Pool-Dimensionen: 1830×380px, Lane: 1800×380px
- [ ] Pool-Abstände: 10px zwischen Pools
- [ ] ADONIS-Namespaces korrekt gesetzt (`adonis`, `omgdc`, `omgdi`)
- [ ] Target-Namespace: `http://www.boc-group.com`
- [ ] IDs im GUID-Format mit Unterstrich-Präfix
- [ ] Task-Dimensionen: 151×76px
- [ ] Event-Dimensionen: 36×36px
- [ ] Gateway-Dimensionen: 56×56px
- [ ] Horizontale Task-Anordnung (gleiche Y-Koordinate pro Pool)
- [ ] Links-nach-Rechts-Fluss
- [ ] Message Flows zwischen Pools definiert
- [ ] Start-/End-Events für jeden Pool vorhanden
- [ ] Lanes mit Rollen-/Funktionsbezeichnungen
- [ ] e2e-Perspektive: Prozess beginnt und endet beim Kunden
