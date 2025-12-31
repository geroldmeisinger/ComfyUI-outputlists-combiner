## Discriminador de Workflow

![Workflow Discriminator](WorkflowDiscriminator/WorkflowDiscriminator.png)

(ComfyUI workflow inclut)

Compara los workflows e los discrimina per n'extraire las valors diferentas coma de listas de sortida individualas.
Podètz utilizar aqueste node per restaurar la creacion de cada imatge individual a partir d'una lista d'imatges amb lo meteis workflow.
Notatz que lo `IMAGE` de ComfyUI conten pas las metadonadas del workflow e vos cal cargar los imatges amb de cargadors especializats d'imatge+metadonadas e connectar las metadonadas a aqueste node.
Los nodes personalizats amb de cargadors de metadonadas incluèron:
* `Load Any File.metadata` -> `JSON OutputList(jsonpath=$.["PNG:Prompt"]).value`
* [Crystool](https://github.com/crystian/ComfyUI-Crystools) `🪛 Load image with metadata.Metadata RAW` -> `🪛 Metadata extractor.prompt`
* [Simple_Readable_Metadata](https://github.com/ShammiG/ComfyUI-Simple_Readable_Metadata-SG) `Simple Readable Metadata-SG.metadata_raw`

### Entradas

| Nom | Tipe | Descripcion |
| --- | --- | --- |
| `objs_0` | `*` | (opcional) Un objecte simple (o una lista d'objectes), generalament d'un workflow. `objs_0` e `more_objs` seràn concatenats e existiran per comoditat, se volètz solament comparar doas objects. |
| `more_objs` | `*` | (opcional) Un autre objecte (o una lista d'objectes), generalament d'un workflow. `objs_0` e `more_objs` seràn concatenats e existiran per comoditat, se volètz solament comparar doas objects. |
| `ignore_jsonpaths` | `STRING` | (opcional) Una lista de JSONPaths de ignorar se volètz enlairar mantun discriminador. |

### Sortidas

| Nom | Tipe | Descripcion |
| --- | --- | --- |
| `list_a` | `* 𝌠` |  |
| `list_b` | `* 𝌠` |  |
| `list_c` | `* 𝌠` |  |
| `list_d` | `* 𝌠` |  |
| `jsonpaths` | `STRING 𝌠` |  |

