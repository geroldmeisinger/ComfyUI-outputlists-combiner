## Workflow Discriminator

![Workflow Discriminator](WorkflowDiscriminator/WorkflowDiscriminator.png)

(ComfyUI workflow bijgevoegd)

Vergeliekt workflows en discriminateert ze um ‘t verschillende waardes te extrahere um individuele OutputLists te maken.
Ge kin ‘t node gebruke um ‘t te herstellen hoe elk individuele beeld gemaak is um ‘n lijst um beelde met ‘t zelfde workflow.
Let op dat ComfyUI's `IMAGE` geen workflow metadata bevat en ge moe te beelde laode um ‘n gespecialiseerde beeld+metadata laoders en de metadata verbinne um ‘t node.
Custom nodes um metadata laoders zien:
* `Load Any File.metadata` -> `JSON OutputList(jsonpath=$.["PNG:Prompt"]).value`
* [Crystool](https://github.com/crystian/ComfyUI-Crystools) `🪛 Load image with metadata.Metadata RAW` -> `🪛 Metadata extractor.prompt`
* [Simple_Readable_Metadata](https://github.com/ShammiG/ComfyUI-Simple_Readable_Metadata-SG) `Simple Readable Metadata-SG.metadata_raw`

### Invoere

| Naom | Type | Beschrèving |
| --- | --- | --- |
| `objs_0` | `*` | (optioneel) ‘n enkele object (of ‘n lijst um objecte), meestal um ‘n workflow. `objs_0` en `more_objs` zien samengevoegd en zien um ‘t gemak, es ge allèn ‘t te vergelieke um twee objecte. |
| `more_objs` | `*` | (optioneel) ‘n ander object (of ‘n lijst um objecte), meestal um ‘n workflow. `objs_0` en `more_objs` zien samengevoegd en zien um ‘t gemak, es ge allèn ‘t te vergelieke um twee objecte. |
| `ignore_jsonpaths` | `STRING` | (optioneel) ‘n lijst um JSONPaths um ‘t te negeren um es ge ‘n aantal discriminators te keten. |

### Uitvoere

| Naom | Type | Beschrèving |
| --- | --- | --- |
| `list_a` | `* 𝌠` |  |
| `list_b` | `* 𝌠` |  |
| `list_c` | `* 𝌠` |  |
| `list_d` | `* 𝌠` |  |
| `jsonpaths` | `STRING 𝌠` |  |

