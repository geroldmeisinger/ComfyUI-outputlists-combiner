## Workflow Discriminator

![Workflow Discriminator](WorkflowDiscriminator/WorkflowDiscriminator.png)

(ComfyUI workflow inkludiert)

Vergleicht Workflows und unterscheidet sie, um die verschiedenen Werte als individuelle OutputLists zu extrahieren.
Sie können diesen Knoten verwenden, um wiederherzustellen, wie jeweils ein einzelnes Bild aus einer Liste von Bildern mit dem gleichen Workflow erstellt wurde.
Beachten Sie, dass ComfyUIs `IMAGE` keine Workflow-Metadaten enthält und Sie die Bilder mit spezialisierten Image+Metadata-Ladern laden müssen und die Metadaten mit diesem Knoten verbinden müssen.
Benutzerdefinierte Knoten mit Metadatenladern sind:
* `Load Any File.metadata` -> `JSON OutputList(jsonpath=$.["PNG:Prompt"]).value`
* [Crystool](https://github.com/crystian/ComfyUI-Crystools) `🪛 Load image with metadata.Metadata RAW` -> `🪛 Metadata extractor.prompt`
* [Simple_Readable_Metadata](https://github.com/ShammiG/ComfyUI-Simple_Readable_Metadata-SG) `Simple Readable Metadata-SG.metadata_raw`

### Eingaben

| Name | Typ | Beschreibung |
| --- | --- | --- |
| `objs_0` | `*` | (optional) Ein einzelnes Objekt (oder eine Liste von Objekten), normalerweise aus einem Workflow. `objs_0` und `more_objs` werden zusammengeführt und existieren aus Bequemlichkeitsgründen, wenn Sie nur zwei Objekte vergleichen möchten. |
| `more_objs` | `*` | (optional) Ein weiteres Objekt (oder eine Liste von Objekten), normalerweise aus einem Workflow. `objs_0` und `more_objs` werden zusammengeführt und existieren aus Bequemlichkeitsgründen, wenn Sie nur zwei Objekte vergleichen möchten. |
| `ignore_jsonpaths` | `ZEICHENKETTE` | (optional) Eine Liste von JSONPaths, die ignoriert werden sollen, falls Sie mehrere Discriminatoren hintereinander verkettet haben möchten. |

### Ausgaben

| Name | Typ | Beschreibung |
| --- | --- | --- |
| `list_a` | `* 𝌠` |  |
| `list_b` | `* 𝌠` |  |
| `list_c` | `* 𝌠` |  |
| `list_d` | `* 𝌠` |  |
| `jsonpaths` | `ZEICHENKETTE 𝌠` |  |

