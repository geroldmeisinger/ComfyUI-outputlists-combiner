## Workflow Discriminator

![Workflow Discriminator](WorkflowDiscriminator/WorkflowDiscriminator.png)

(ComfyUI workflow inbegrepen)

Vergelijkt workflows en discrimineert ze om de verschillende waarden als individuele OutputLists te extraheren.
U kunt deze node gebruiken om te herstellen hoe elk individueel beeld werd gemaakt uit een lijst van beelden met dezelfde workflow.
Let op dat ComfyUI's `IMAGE` geen workflow metadata bevat en u de beelden moet laden met gespecialiseerde image+metadata loaders en de metadata verbinden met deze node.
Aangepaste nodes met metadata loaders zijn:
* `Load Any File.metadata` -> `JSON OutputList(jsonpath=$.["PNG:Prompt"]).value`
* [Crystool](https://github.com/crystian/ComfyUI-Crystools) `🪛 Load image with metadata.Metadata RAW` -> `🪛 Metadata extractor.prompt`
* [Simple_Readable_Metadata](https://github.com/ShammiG/ComfyUI-Simple_Readable_Metadata-SG) `Simple Readable Metadata-SG.metadata_raw`

### Invoer

| Naam | Type | Beschrijving |
| --- | --- | --- |
| `objs_0` | `*` | (optioneel) Een enkel object (of een lijst van objecten), meestal van een workflow. `objs_0` en `more_objs` zullen samengevoegd worden en bestaan voor gemak, indien u alleen twee objecten wilt vergelijken. |
| `more_objs` | `*` | (optioneel) Een ander object (of een lijst van objecten), meestal van een workflow. `objs_0` en `more_objs` zullen samengevoegd worden en bestaan voor gemak, indien u alleen twee objecten wilt vergelijken. |
| `ignore_jsonpaths` | `STRING` | (optioneel) Een lijst van JSONPaths om te negeren indien u meerdere discriminators achter elkaar wilt ketenen. |

### Uitvoer

| Naam | Type | Beschrijving |
| --- | --- | --- |
| `list_a` | `* 𝌠` |  |
| `list_b` | `* 𝌠` |  |
| `list_c` | `* 𝌠` |  |
| `list_d` | `* 𝌠` |  |
| `jsonpaths` | `STRING 𝌠` |  |

