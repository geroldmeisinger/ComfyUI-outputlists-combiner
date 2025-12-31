## Workflow Discriminator

![Workflow Discriminator](WorkflowDiscriminator/WorkflowDiscriminator.png)

(ComfyUI workflow ap gen yon pwogrè)

Kompare workflow yo ak discrimine yo pou ektrè valè ki diferan anndan OutputLists separe.
Ou kapab itilize nòd sa pou restore kòman chak imaj ki kreye sòti nan yon lis imaj ki gen meme workflow.
Remarke ke `IMAGE` ComfyUI pa gen metadòm workflow la ak ou bezwen chaje imaj yo avèk chajè spesyalize ak lyen metadòm yo nan nòd sa.
Nòd ki gen chajè metadòm yon:
* `Load Any File.metadata` -> `JSON OutputList(jsonpath=$.["PNG:Prompt"]).value`
* [Crystool](https://github.com/crystian/ComfyUI-Crystools) `🪛 Load image with metadata.Metadata RAW` -> `🪛 Metadata extractor.prompt`
* [Simple_Readable_Metadata](https://github.com/ShammiG/ComfyUI-Simple_Readable_Metadata-SG) `Simple Readable Metadata-SG.metadata_raw`

### Antre yo

| Non | Tip | Deskrisyon |
| --- | --- | --- |
| `objs_0` | `*` | (optional) Yon sèl objè (oswa yon lis objè), souvan nan yon workflow. `objs_0` ak `more_objs` ap konkatène ak ap egziste pou konveni, si ou sèlman vle kompare de objè. |
| `more_objs` | `*` | (optional) Yon lòt objè (oswa yon lis objè), souvan nan yon workflow. `objs_0` ak `more_objs` ap konkatène ak ap egziste pou konveni, si ou sèlman vle kompare de objè. |
| `ignore_jsonpaths` | `CHENN` | (optional) Yon lis JSONPaths pou enpoti si ou vle chèn plizyè discriminators ensembò. |

### Sòti yo

| Non | Tip | Deskrisyon |
| --- | --- | --- |
| `list_a` | `* 𝌠` |  |
| `list_b` | `* 𝌠` |  |
| `list_c` | `* 𝌠` |  |
| `list_d` | `* 𝌠` |  |
| `jsonpaths` | `CHENN 𝌠` |  |

