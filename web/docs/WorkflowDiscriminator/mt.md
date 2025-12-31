## Workflow Discriminator

![Workflow Discriminator](WorkflowDiscriminator/WorkflowDiscriminator.png)

(ComfyUI workflow inkluż)

Jegħmel konfrontazzjoni bejn workflows u jidiskriminahom biex jibdlu l-valuri differenti bħala OutputLists individwali.
Tista’ tużah dan in-nod biex tirrestawra kif kollha imma ġew magħmul minn lista ta’ immaġini b’workflow ugwali.
Imnien li `IMAGE` ta’ ComfyUI m’għandhax il-metadata tal-workflow u trid taħdem immaġini bil-metadda ta’ specializzati u tikkonnettahom mal-nod.
In-nodi custom bil-metadda ta’ loaders inklużi:
* `Load Any File.metadata` -> `JSON OutputList(jsonpath=$.["PNG:Prompt"]).value`
* [Crystool](https://github.com/crystian/ComfyUI-Crystools) `🪛 Load image with metadata.Metadata RAW` -> `🪛 Metadata extractor.prompt`
* [Simple_Readable_Metadata](https://github.com/ShammiG/ComfyUI-Simple_Readable_Metadata-SG) `Simple Readable Metadata-SG.metadata_raw`

### Inputs

| Isem | Tip | Deskrizzjoni |
| --- | --- | --- |
| `objs_0` | `*` | (opzjonali) Oġġett singolu (jew lista ta’ oġġetti), ġeneralmenti ta’ workflow. `objs_0` u `more_objs` jkunu konnettati malajr u jeżistu għal konvenjenza, jekk jogħġbok tixtieġu bissi konfrontazzjoni bejn żewġ oġġetti. |
| `more_objs` | `*` | (opzjonali) Oġġett ieħor (jew lista ta’ oġġetti), ġeneralmenti ta’ workflow. `objs_0` u `more_objs` jkunu konnettati malajr u jeżistu għal konvenjenza, jekk jogħġbok tixtieġu bissi konfrontazzjoni bejn żewġ oġġetti. |
| `ignore_jsonpaths` | `STRING` | (opzjonali) Lista ta’ JSONPaths li jinżlu jekk trid taħdem bħal bosta discriminators magħquda. |

### Outputs

| Isem | Tip | Deskrizzjoni |
| --- | --- | --- |
| `list_a` | `* 𝌠` |  |
| `list_b` | `* 𝌠` |  |
| `list_c` | `* 𝌠` |  |
| `list_d` | `* 𝌠` |  |
| `jsonpaths` | `STRING 𝌠` |  |

