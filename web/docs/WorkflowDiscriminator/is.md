## Workflow Discriminator

![Workflow Discriminator](WorkflowDiscriminator/WorkflowDiscriminator.png)

(ComfyUI vinnusvæði included)

Samanburður vinnusvæða og aðskiljanir þeir til að draga út mismunandi gildi sem einstaka OutputList.
Þú getur notað þennan node til að endurheimta hvern einstaka mynd var búin til úr listanum af myndum með sama vinnusvæði.
Athugaðu að ComfyUI's `IMAGE` inniheldur ekki metadata vinnusvæðisins og þú þarft að hlaða inn myndum með sérstökum image+metadata hlaður og tengja metadata við þennan node.
Sérsniðnar node með metadata hlaður inn:
* `Load Any File.metadata` -> `JSON OutputList(jsonpath=$.["PNG:Prompt"]).value`
* [Crystool](https://github.com/crystian/ComfyUI-Crystools) `🪛 Load image with metadata.Metadata RAW` -> `🪛 Metadata extractor.prompt`
* [Simple_Readable_Metadata](https://github.com/ShammiG/ComfyUI-Simple_Readable_Metadata-SG) `Simple Readable Metadata-SG.metadata_raw`

### Inntök

| Nafn | Gerð | Lýsing |
| --- | --- | --- |
| `objs_0` | `*` | (valfrjálst) Eitt hlut (eða listi af hlutum), venjulega af vinnusvæði. `objs_0` og `more_objs` verður sameinað saman og er til að auðvelda, ef þú vilt aðeins samanburður tveggja hluta. |
| `more_objs` | `*` | (valfrjálst) Annað hlut (eða listi af hlutum), venjulega af vinnusvæði. `objs_0` og `more_objs` verður sameinað saman og er til að auðvelda, ef þú vilt aðeins samanburður tveggja hluta. |
| `ignore_jsonpaths` | `STRING` | (valfrjálst) Listi af JSONPaths til að hunsa ef þú vilt sameina margar aðskiljanir saman. |

### Úttök

| Nafn | Gerð | Lýsing |
| --- | --- | --- |
| `list_a` | `* 𝌠` |  |
| `list_b` | `* 𝌠` |  |
| `list_c` | `* 𝌠` |  |
| `list_d` | `* 𝌠` |  |
| `jsonpaths` | `STRING 𝌠` |  |

