## Workflow Discriminator

![Workflow Discriminator](WorkflowDiscriminator/WorkflowDiscriminator.png)

(ComfyUI workflow san áireamh)

Comparáidí workflowanna agus déanann iad discriminate chun na luachanna éagsúla a bhaint mar OutputLists iolracha.
Is féidir leat an nód seo a úsáid chun conas gach íomhá a cruthaíodh a aischur ó liosta íomhánna leis an gcéanna workflow.
Tabhair faoi deara nach bhfuil metadata workflow i `IMAGE` ag ComfyUI agus ní mór duit na híomhánna a lódáil le lódálaithe íomhánna+metadata speisialta agus an metadata a nascadh leis an nód seo.
Nóid saincheaptha le lódálaithe metadata a including:
* `Load Any File.metadata` -> `JSON OutputList(jsonpath=$.["PNG:Prompt"]).value`
* [Crystool](https://github.com/crystian/ComfyUI-Crystools) `🪛 Load image with metadata.Metadata RAW` -> `🪛 Metadata extractor.prompt`
* [Simple_Readable_Metadata](https://github.com/ShammiG/ComfyUI-Simple_Readable_Metadata-SG) `Simple Readable Metadata-SG.metadata_raw`

### Ionchuir

| Ainm | Cineál | Cur Síos |
| --- | --- | --- |
| `objs_0` | `*` | (roghnach) Objet amháin (nó liosta objet) de ghnáth de workflow. `objs_0` agus `more_objs` déanfar iad a chomhaid agus a bheidh ann le haghaidh suímh, más mian leat a comparáid dhá objet amháin. |
| `more_objs` | `*` | (roghnach) Objet eile (nó liosta objet) de ghnáth de workflow. `objs_0` agus `more_objs` déanfar iad a chomhaid agus a bheidh ann le haghaidh suímh, más mian leat a comparáid dhá objet amháin. |
| `ignore_jsonpaths` | `STRING` | (roghnach) Liosta de JSONPaths le neamhshuim a dhéanamh i gcás gur mian leat iolrú discriminators a chain. |

### Aschuir

| Ainm | Cineál | Cur Síos |
| --- | --- | --- |
| `list_a` | `* 𝌠` |  |
| `list_b` | `* 𝌠` |  |
| `list_c` | `* 𝌠` |  |
| `list_d` | `* 𝌠` |  |
| `jsonpaths` | `STRING 𝌠` |  |

