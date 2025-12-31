## Workflow Discriminator

![Workflow Discriminator](WorkflowDiscriminator/WorkflowDiscriminator.png)

(ComfyUI workflow inclòs)

Compara workflows i els discrimina per extreure els valors diferents com a OutputLists individuals.
Pots utilitzar aquest node per restaurar com es va crear cada imatge individual a partir d'una llista d'imatges amb el mateix workflow.
Tingues en compte que el `IMAGE` de ComfyUI no conté les metadades del workflow i necessites carregar les imatges amb carregadors especialitzats d'imatges+metadades i connectar les metadades a aquest node.
Els nodes personalitzats amb carregadors de metadades inclouen:
* `Load Any File.metadata` -> `JSON OutputList(jsonpath=$.["PNG:Prompt"]).value`
* [Crystool](https://github.com/crystian/ComfyUI-Crystools) `🪛 Load image with metadata.Metadata RAW` -> `🪛 Metadata extractor.prompt`
* [Simple_Readable_Metadata](https://github.com/ShammiG/ComfyUI-Simple_Readable_Metadata-SG) `Simple Readable Metadata-SG.metadata_raw`

### Entrades

| Nom | Tipus | Descripció |
| --- | --- | --- |
| `objs_0` | `*` | (opcional) Un objecte simple (o una llista d'objectes), normalment d'un workflow. `objs_0` i `more_objs` es concatenaran junts i existeixen per comoditat, si només vols comparar dos objectes. |
| `more_objs` | `*` | (opcional) Un altre objecte (o una llista d'objectes), normalment d'un workflow. `objs_0` i `more_objs` es concatenaran junts i existeixen per comoditat, si només vols comparar dos objectes. |
| `ignore_jsonpaths` | `STRING` | (opcional) Una llista de JSONPaths a ignorar en cas que vulguis encadenar múltiples discriminadors junts. |

### Sortides

| Nom | Tipus | Descripció |
| --- | --- | --- |
| `list_a` | `* 𝌠` |  |
| `list_b` | `* 𝌠` |  |
| `list_c` | `* 𝌠` |  |
| `list_d` | `* 𝌠` |  |
| `jsonpaths` | `STRING 𝌠` |  |

