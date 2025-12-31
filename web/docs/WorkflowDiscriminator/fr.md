## Workflow Discriminator

![Workflow Discriminator](WorkflowDiscriminator/WorkflowDiscriminator.png)

(Workflow ComfyUI inclus)

Compare les workflows et les discrimine pour extraire les valeurs différentes sous forme de OutputLists individuelles.
Vous pouvez utiliser ce nœud pour restaurer comment chaque image individuelle a été créée à partir d'une liste d'images avec le même workflow.
Notez que les métadonnées du workflow ne sont pas incluses dans `IMAGE` de ComfyUI et vous devez charger les images avec des chargeurs spécialisés d'images+méta-données et connecter les métadonnées à ce nœud.
Les nœuds personnalisés avec des chargeurs de métadonnées incluent :
* `Load Any File.metadata` -> `JSON OutputList(jsonpath=$.["PNG:Prompt"]).value`
* [Crystool](https://github.com/crystian/ComfyUI-Crystools) `🪛 Load image with metadata.Metadata RAW` -> `🪛 Metadata extractor.prompt`
* [Simple_Readable_Metadata](https://github.com/ShammiG/ComfyUI-Simple_Readable_Metadata-SG) `Simple Readable Metadata-SG.metadata_raw`

### Entrées

| Nom | Type | Description |
| --- | --- | --- |
| `objs_0` | `*` | (optionnel) Un objet unique (ou une liste d'objets), généralement d'un workflow. `objs_0` et `more_objs` seront concaténés ensemble et existent pour commodité, si vous ne souhaitez comparer que deux objets. |
| `more_objs` | `*` | (optionnel) Un autre objet (ou une liste d'objets), généralement d'un workflow. `objs_0` et `more_objs` seront concaténés ensemble et existent pour commodité, si vous ne souhaitez comparer que deux objets. |
| `ignore_jsonpaths` | `STRING` | (optionnel) Une liste de JSONPaths à ignorer au cas où vous souhaiteriez chaîner plusieurs discriminateurs ensemble. |

### Sorties

| Nom | Type | Description |
| --- | --- | --- |
| `list_a` | `* 𝌠` |  |
| `list_b` | `* 𝌠` |  |
| `list_c` | `* 𝌠` |  |
| `list_d` | `* 𝌠` |  |
| `jsonpaths` | `STRING 𝌠` |  |

