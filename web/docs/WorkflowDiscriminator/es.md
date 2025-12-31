## Workflow Discriminator

![Workflow Discriminator](WorkflowDiscriminator/WorkflowDiscriminator.png)

(ComfyUI workflow incluido)

Compara workflows y los discrimina para extraer los valores diferentes como OutputLists individuales.
Puede usar este nodo para restaurar cómo se creó cada imagen individual a partir de una lista de imágenes con el mismo workflow.
Tenga en cuenta que los `IMAGE` de ComfyUI no contienen los metadatos del workflow y necesita cargar las imágenes con cargadores especializados de imagen+metadatos y conectar los metadatos a este nodo.
Los nodos personalizados con cargadores de metadatos incluyen:
* `Load Any File.metadata` -> `JSON OutputList(jsonpath=$.["PNG:Prompt"]).value`
* [Crystool](https://github.com/crystian/ComfyUI-Crystools) `🪛 Load image with metadata.Metadata RAW` -> `🪛 Metadata extractor.prompt`
* [Simple_Readable_Metadata](https://github.com/ShammiG/ComfyUI-Simple_Readable_Metadata-SG) `Simple Readable Metadata-SG.metadata_raw`

### Entradas

| Nombre | Tipo | Descripción |
| --- | --- | --- |
| `objs_0` | `*` | (opcional) Un objeto único (o una lista de objetos), generalmente de un workflow. `objs_0` y `more_objs` se concatenarán juntos y existirán por conveniencia, si solo desea comparar dos objetos. |
| `more_objs` | `*` | (opcional) Otro objeto (o una lista de objetos), generalmente de un workflow. `objs_0` y `more_objs` se concatenarán juntos y existirán por conveniencia, si solo desea comparar dos objetos. |
| `ignore_jsonpaths` | `STRING` | (opcional) Una lista de JSONPaths para ignorar en caso de que desee encadenar múltiples discriminadores juntos. |

### Salidas

| Nombre | Tipo | Descripción |
| --- | --- | --- |
| `list_a` | `* 𝌠` |  |
| `list_b` | `* 𝌠` |  |
| `list_c` | `* 𝌠` |  |
| `list_d` | `* 𝌠` |  |
| `jsonpaths` | `STRING 𝌠` |  |

