<!-- This file was auto-translated with a local LLM and last updated on 2025-12-27. -->
## Combinations de Listes de Sortie

![Combinations de Listes de Sortie](CombineOutputLists/CombineOutputLists.png)

(workflow ComfyUI inclus)

Prend jusqu'à 4 listes de sortie et génère toutes les combinaisons possibles entre elles.

Exemple : `[1, 2, 3] x ["A", "B"] = [(1, "A"), (1, "B"), (2, "A"), (2, "B"), (3, "A"), (3, "B")]`

`unzip_a` .. `unzip_d` utilisent `is_output_list=True` (indiqué par le symbole `𝌠`) et seront traités séquentiellement par les nœuds correspondants.

Toutes les listes sont optionnelles et les listes vides seront ignorées.

Techniquement, il calcule *le produit cartésien* et affiche chaque combinaison décomposée en ses éléments (`unzip`), tandis que les listes vides seront remplacées par des unités de `None` et émettront `None` sur la sortie correspondante.

Exemple : `[1, 2] x [] x ["A", "B"] x [] = [(1, None, "A", None), (1, None, "B", None), (2, None, "A", None), (2, None, "B", None)]`

### Entrées

| Nom | Type | Description |
| --- | --- | --- |
| `list_a` | `*` | (optionnel) |
| `list_b` | `*` | (optionnel) |
| `list_c` | `*` | (optionnel) |
| `list_d` | `*` | (optionnel) |

### Sorties

| Nom | Type | Description |
| --- | --- | --- |
| `unzip_a` | `* 𝌠` | Valeur des combinaisons correspondant à `list_a`. |
| `unzip_b` | `* 𝌠` | Valeur des combinaisons correspondant à `list_b`. |
| `unzip_c` | `* 𝌠` | Valeur des combinaisons correspondant à `list_c`. |
| `unzip_d` | `* 𝌠` | Valeur des combinaisons correspondant à `list_d`. |
| `index` | `INT 𝌠` | Plage de 0..count pouvant être utilisée comme indice. |
| `count` | `INT` | Nombre total de combinaisons. |

