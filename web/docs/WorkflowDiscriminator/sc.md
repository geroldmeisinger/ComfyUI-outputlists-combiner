## Discriminadore de su Workflow

![Discriminadore de su Workflow](WorkflowDiscriminator/WorkflowDiscriminator.png)

(ComfyUI workflow included)

Comparat workflows e is discriminat pro iscollere sos valores diferentes comente lista de output individuales.
Podet usare custu node pro restituire comente cada immàgine individuale est istada creada dae una lista de immàgines cun su matessi workflow.
Nota chi su metadata de ComfyUI `IMAGE` non cuntènnit e metadata de su workflow e bi cheret iscàrrere sas immàgines cun cargadores de immàgines + metadata especializados e cunnetare sa metadata a custu node.
Nodos personalizados cun cargadores de metadata inclùntiant:
* `Load Any File.metadata` -> `JSON OutputList(jsonpath=$.["PNG:Prompt"]).value`
* [Crystool](https://github.com/crystian/ComfyUI-Crystools) `🪛 Load image with metadata.Metadata RAW` -> `🪛 Metadata extractor.prompt`
* [Simple_Readable_Metadata](https://github.com/ShammiG/ComfyUI-Simple_Readable_Metadata-SG) `Simple Readable Metadata-SG.metadata_raw`

### Inputs

| Name | Type | Description |
| --- | --- | --- |
| `objs_0` | `*` | (optional) Unu objectu (o una lista de objectos), normale de unu workflow. `objs_0` e `more_objs` ant s’ispinnidos e sunt a disponimentu pro còmmode, si bi cheret cunfrontare isceti do objectos. |
| `more_objs` | `*` | (optional) Un’àtera objectu (o una lista de objectos), normale de unu workflow. `objs_0` e `more_objs` ant s’ispinnidos e sunt a disponimentu pro còmmode, si bi cheret cunfrontare isceti do objectos. |
| `ignore_jsonpaths` | `STRING` | (optional) Una lista de JSONPaths de ignorare si bi cheret unire discrininadores. |

### Outputs

| Name | Type | Description |
| --- | --- | --- |
| `list_a` | `* 𝌠` |  |
| `list_b` | `* 𝌠` |  |
| `list_c` | `* 𝌠` |  |
| `list_d` | `* 𝌠` |  |
| `jsonpaths` | `STRING 𝌠` |  |

