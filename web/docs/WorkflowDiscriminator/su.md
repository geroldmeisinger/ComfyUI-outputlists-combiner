## Workflow Discriminator

![Workflow Discriminator](WorkflowDiscriminator/WorkflowDiscriminator.png)

(ComfyUI workflow anu kalebet)

Mamandongan workflow sareng nangtukeunanna pikeun ngaluarkeun nilai-nilaénu anu béda sacara individual dina OutputLists.
Anjeun bisa nganggo ieu node pikeun mambalikkeun cara mana image individual dijieun tina daptar image anu éta ngagunakeun workflow anu samé.
Hatur nu ComfyUI éta `IMAGE` henteu ngandung metadata workflow sareng anjeun kudu ngamuat image nganggo pamunuh image+metadata sareng nyambungkeun metadata ka ieu node.
Node custom anu ngandung pamunuh metadata:
* `Load Any File.metadata` -> `JSON OutputList(jsonpath=$.["PNG:Prompt"]).value`
* [Crystool](https://github.com/crystian/ComfyUI-Crystools) `🪛 Load image with metadata.Metadata RAW` -> `🪛 Metadata extractor.prompt`
* [Simple_Readable_Metadata](https://github.com/ShammiG/ComfyUI-Simple_Readable_Metadata-SG) `Simple Readable Metadata-SG.metadata_raw`

### Inputs

| Nama | Tipe | Deskripsi |
| --- | --- | --- |
| `objs_0` | `*` | (optional) Objék tunggal (atawa daptar objék), biasana tina sebuah workflow. `objs_0` jeung `more_objs` bakal digabungkeun sareng nganana pikeun kenyamanan, upami anjeun ngan hoyong nangtukeun dua objék. |
| `more_objs` | `*` | (optional) Objék laén (atawa daptar objék), biasana tina sebuah workflow. `objs_0` jeung `more_objs` bakal digabungkeun sareng nganana pikeun kenyamanan, upami anjeun ngan hoyong nangtukeun dua objék. |
| `ignore_jsonpaths` | `STRING` | (optional) Daptar JSONPaths anu kudu diabaikan upami anjeun hoyong nganturun discriminators anu sabarapakeun. |

### Outputs

| Nama | Tipe | Deskripsi |
| --- | --- | --- |
| `list_a` | `* 𝌠` |  |
| `list_b` | `* 𝌠` |  |
| `list_c` | `* 𝌠` |  |
| `list_d` | `* 𝌠` |  |
| `jsonpaths` | `STRING 𝌠` |  |

