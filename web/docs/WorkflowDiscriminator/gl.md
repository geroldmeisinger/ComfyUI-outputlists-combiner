## Workflow Discriminator

![Workflow Discriminator](WorkflowDiscriminator/WorkflowDiscriminator.png)

(ComfyUI workflow incluído)

Compára workflows e discrimínaos para extraer os valores diferentes como OutputLists individuais.
Pode usar este nodo para restaurar como se creou cada imaxe individual dende unha lista de imaxes co mesmo workflow.
Teña en conta que o `IMAGE` de ComfyUI non contén os metadatos do workflow e precisa cargar as imaxes con cargadores especializados de imaxe+metadatos e conectar os metadatos a este nodo.
Os nodos personalizados con cargadores de metadatos inclúen:
* `Load Any File.metadata` -> `JSON OutputList(jsonpath=$.["PNG:Prompt"]).value`
* [Crystool](https://github.com/crystian/ComfyUI-Crystools) `🪛 Load image with metadata.Metadata RAW` -> `🪛 Metadata extractor.prompt`
* [Simple_Readable_Metadata](https://github.com/ShammiG/ComfyUI-Simple_Readable_Metadata-SG) `Simple Readable Metadata-SG.metadata_raw`

### Entradas

| Nome | Tipo | Descrición |
| --- | --- | --- |
| `objs_0` | `*` | (opcional) Un obxecto único (ou unha lista de obxectos), normalmente dun workflow. `objs_0` e `more_objs` serán concatenados xuntos e existen por conveniencia, se só quere comparar dous obxectos. |
| `more_objs` | `*` | (opcional) Outro obxecto (ou unha lista de obxectos), normalmente dun workflow. `objs_0` e `more_objs` serán concatenados xuntos e existen por conveniencia, se só quere comparar dous obxectos. |
| `ignore_jsonpaths` | `STRING` | (opcional) Unha lista de JSONPaths a ignorar no caso de querer encadear múltiples discriminadores xuntos. |

### Saídas

| Nome | Tipo | Descrición |
| --- | --- | --- |
| `list_a` | `* 𝌠` |  |
| `list_b` | `* 𝌠` |  |
| `list_c` | `* 𝌠` |  |
| `list_d` | `* 𝌠` |  |
| `jsonpaths` | `STRING 𝌠` |  |

