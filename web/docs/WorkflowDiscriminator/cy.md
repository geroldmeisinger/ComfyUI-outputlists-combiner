## Diffyniwr Cyflun

![Diffyniwr Cyflun](WorkflowDiscriminator/WorkflowDiscriminator.png)

(Cyflun ComfyUI wedi'i gynnwys)

Cymharu cyfluniau a'u diffyniwr i astyn y gwerthoedd gwahanol fel OutputLists sylfaenol.
Gallwch ddefnyddio'r nod hwn i adfer sut crëwyd pob delwedd unigol o restr o ddelweddau â'r un cyflun.
Sylwer bod metadata'r `IMAGE` yn ComfyUI ddim yn cynnwys metadata'r cyflun a byddwch yn need i lwytho'r delweddau â llwyddyn llwyddoedd sylfaen a gysylltu'r metadata i'r nod hwn.
Mae nodau personol â llwyddyn llwyddoedd yn cynnwys:
* `Load Any File.metadata` -> `JSON OutputList(jsonpath=$.["PNG:Prompt"]).value`
* [Crystool](https://github.com/crystian/ComfyUI-Crystools) `🪛 Load image with metadata.Metadata RAW` -> `🪛 Metadata extractor.prompt`
* [Simple_Readable_Metadata](https://github.com/ShammiG/ComfyUI-Simple_Readable_Metadata-SG) `Simple Readable Metadata-SG.metadata_raw`

### Mewnbwn

| Enw | Math | Disgrifiad |
| --- | --- | --- |
| `objs_0` | `*` | (dewisol) Gwrthrych unigol (neu restr o wrthrychau), yn arfer o gyflun. Bydd `objs_0` a `more_objs` yn cael eu cysylltu a bod yn bodloni ar gyfer cyfleus, os ydych chi'n dymuno cymharu dim ond dwy wrthrych. |
| `more_objs` | `*` | (dewisol) Gwrthrych arall (neu restr o wrthrychau), yn arfer o gyflun. Bydd `objs_0` a `more_objs` yn cael eu cysylltu a bod yn bodloni ar gyfer cyfleus, os ydych chi'n dymuno cymharu dim ond dwy wrthrych. |
| `ignore_jsonpaths` | `STRING` | (dewisol) Rhestr o JSONPaths i anwybyddu os ydych chi'n dymuno gysylltu diffyniwrau lluosog gyda'i gilydd. |

### Allbwn

| Enw | Math | Disgrifiad |
| --- | --- | --- |
| `list_a` | `* 𝌠` |  |
| `list_b` | `* 𝌠` |  |
| `list_c` | `* 𝌠` |  |
| `list_d` | `* 𝌠` |  |
| `jsonpaths` | `STRING 𝌠` |  |

