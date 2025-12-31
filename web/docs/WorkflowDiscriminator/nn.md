## Workflow Discriminator

![Workflow Discriminator](WorkflowDiscriminator/WorkflowDiscriminator.png)

(ComfyUI workflow inkludert)

Samanliknar workflow og skilljer dei for å uttrekkje dei ulike verdiane som individuelle OutputList.
Du kan bruke denne noden for å gjenopprette korleis kvar enkelt bilete vart laga frå ei liste med bilete med same workflow.
Merk at ComfyUI sitt `IMAGE` ikkje inneheldt workflow metadata og du må laste inn bila med spesialiserte image+metadata lastarar og kopla metadata til denne noden.
Egendefinerte noder med metadata lastarar inkluderer:
* `Load Any File.metadata` -> `JSON OutputList(jsonpath=$.["PNG:Prompt"]).value`
* [Crystool](https://github.com/crystian/ComfyUI-Crystools) `🪛 Load image with metadata.Metadata RAW` -> `🪛 Metadata extractor.prompt`
* [Simple_Readable_Metadata](https://github.com/ShammiG/ComfyUI-Simple_Readable_Metadata-SG) `Simple Readable Metadata-SG.metadata_raw`

### Inndata

| Namn | Type | Skildring |
| --- | --- | --- |
| `objs_0` | `*` | (valfritt) Eit enkelt objekt (eller ei liste med objekt), vanlegvis av ein workflow. `objs_0` og `more_objs` vil bli kome inn i katalogen og eksisterer for konvensjon, viss du berre vil samanlikne to objekt. |
| `more_objs` | `*` | (valfritt) Eit anna objekt (eller ei liste med objekt), vanlegvis av ein workflow. `objs_0` og `more_objs` vil bli kome inn i katalogen og eksisterer for konvensjon, viss du berre vil samanlikne to objekt. |
| `ignore_jsonpaths` | `STRING` | (valfritt) Ein liste med JSONPaths å ignorere viss du vil kjede fleire diskriminatorar sammen. |

### Utdata

| Namn | Type | Skildring |
| --- | --- | --- |
| `list_a` | `* 𝌠` |  |
| `list_b` | `* 𝌠` |  |
| `list_c` | `* 𝌠` |  |
| `list_d` | `* 𝌠` |  |
| `jsonpaths` | `STRING 𝌠` |  |

