## Workflow Discriminator

![Workflow Discriminator](WorkflowDiscriminator/WorkflowDiscriminator.png)

(ComfyUI workflow included)

Kinukumpara ang mga workflow at hinahati ang mga ito upang i-extract ang magkakaibang mga value bilang mga indibidwal na OutputList.
Maaari mong gamitin ang node na ito upang ibalik kung paano ginawa ang bawat indibidwal na imahe mula sa isang listahan ng mga imahe na may parehong workflow.
Tandaan na hindi naglalaman ang `IMAGE` ng ComfyUI ng metadata ng workflow at kailangan mong i-load ang mga imahe gamit ang mga specialized na image+metadata loader at ikonekta ang metadata sa node na ito.
Ang mga custom node na may metadata loader ay kasama ang:
* `Load Any File.metadata` -> `JSON OutputList(jsonpath=$.["PNG:Prompt"]).value`
* [Crystool](https://github.com/crystian/ComfyUI-Crystools) `🪛 Load image with metadata.Metadata RAW` -> `🪛 Metadata extractor.prompt`
* [Simple_Readable_Metadata](https://github.com/ShammiG/ComfyUI-Simple_Readable_Metadata-SG) `Simple Readable Metadata-SG.metadata_raw`

### Mga Input

| Pangalan | Uri | Paglalarawan |
| --- | --- | --- |
| `objs_0` | `*` | (opsyonal) Isang indibidwal na object (o isang listahan ng mga object), karaniwan ng isang workflow. Ang `objs_0` at `more_objs` ay magiging isang kasama at magiging convenient, kung gusto mo lamang i-compare ang dalawang object. |
| `more_objs` | `*` | (opsyonal) Isa pang object (o isang listahan ng mga object), karaniwan ng isang workflow. Ang `objs_0` at `more_objs` ay magiging isang kasama at magiging convenient, kung gusto mo lamang i-compare ang dalawang object. |
| `ignore_jsonpaths` | `STRING` | (opsyonal) Isang listahan ng JSONPaths na i-iiwan na hindi kasama kung gusto mong i-chain ang maraming discriminator. |

### Mga Output

| Pangalan | Uri | Paglalarawan |
| --- | --- | --- |
| `list_a` | `* 𝌠` |  |
| `list_b` | `* 𝌠` |  |
| `list_c` | `* 𝌠` |  |
| `list_d` | `* 𝌠` |  |
| `jsonpaths` | `STRING 𝌠` |  |

