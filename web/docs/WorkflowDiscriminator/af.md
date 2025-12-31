## Workflow Diskrimineerder

![Workflow Diskrimineerder](WorkflowDiscriminator/WorkflowDiscriminator.png)

(ComfyUI workflow ingesluit)

Vergelyk workflows en diskrimineer hulle om die verskillende waardes te onttrek as individuele OutputLists.
Jy kan hierdie node gebruik om te herstel hoe elk individuele beeld geskep is vanaf 'n lys beelde met dieselfde workflow.
Merk op dat ComfyUI se `IMAGE` nie die workflow metadata bevat nie en jy moet die beelde laai met gespesialiseerde image+metadata laaiers en die metadata aan hierdie node koppel.
Aangepaste nodes met metadata laaiers sluit in:
* `Laai enige Lêer.metadata` -> `JSON OutputList(jsonpath=$.["PNG:Prompt"]).value`
* [Crystool](https://github.com/crystian/ComfyUI-Crystools) `🪛 Laai beeld met metadata.Metadata RAW` -> `🪛 Metadata extractor.prompt`
* [Simple_Readable_Metadata](https://github.com/ShammiG/ComfyUI-Simple_Readable_Metadata-SG) `Simple Readable Metadata-SG.metadata_raw`

### Invoere

| Naam | Tipe | Beskrywing |
| --- | --- | --- |
| `objs_0` | `*` | (opsioneel) 'n Enkele objek (of 'n lys objekte), gewoonlik van 'n workflow. `objs_0` en `more_objs` sal saamgevoeg word en bestaan vir gemak, as jy slegs twee objekte wil vergelyk. |
| `more_objs` | `*` | (opsioneel) 'n Ander objek (of 'n lys objekte), gewoonlik van 'n workflow. `objs_0` en `more_objs` sal saamgevoeg word en bestaan vir gemak, as jy slegs twee objekte wil vergelyk. |
| `ignore_jsonpaths` | `STRING` | (opsioneel) 'n Lys JSONPaths om te ignoreer as jy verskeie diskrimineerders wil ketting. |

### Uitvoere

| Naam | Tipe | Beskrywing |
| --- | --- | --- |
| `list_a` | `* 𝌠` |  |
| `list_b` | `* 𝌠` |  |
| `list_c` | `* 𝌠` |  |
| `list_d` | `* 𝌠` |  |
| `jsonpaths` | `STRING 𝌠` |  |

