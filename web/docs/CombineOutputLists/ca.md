<!-- This file was auto-translated with a local LLM and last updated on 2025-12-27. -->
## Combinacions de OutputLists

![Combinacions de OutputLists](CombineOutputLists/CombineOutputLists.png)

(Workflow de ComfyUI inclòs)

Toma fins a 4 OutputLists i genera totes les combinacions entre elles.

Exemple: `[1, 2, 3] x ["A", "B"] = [(1, "A"), (1, "B"), (2, "A"), (2, "B"), (3, "A"), (3, "B")]`

`unzip_a` .. `unzip_d` utilitzen `is_output_list=True` (indicat per el símbol `𝌠`) i seran processats seqüencialment per nodes corresponents.

All lists are optional and empty lists will be ignored.

Tècnicament calcula el *producte cartesià* i emet cada combinació separada en els seus elements (`unzip`), mentre que les llistes buides seran substituïdes per unitats de `None` i emeten `None` a l'output corresponent.

Exemple: `[1, 2] x [] x ["A", "B"] x [] = [(1, None, "A", None), (1, None, "B", None), (2, None, "A", None), (2, None, "B", None)]`

### Entrades

| Nom | Tipus | Descripció |
| --- | --- | --- |
| `list_a` | `*` | (opcional) |
| `list_b` | `*` | (opcional) |
| `list_c` | `*` | (opcional) |
| `list_d` | `*` | (opcional) |

### Sortides

| Nom | Tipus | Descripció |
| --- | --- | --- |
| `unzip_a` | `* 𝌠` | Valor de les combinacions corresponents a `list_a`. |
| `unzip_b` | `* 𝌠` | Valor de les combinacions corresponents a `list_b`. |
| `unzip_c` | `* 𝌠` | Valor de les combinacions corresponents a `list_c`. |
| `unzip_d` | `* 𝌠` | Valor de les combinacions corresponents a `list_d`. |
| `index` | `INT 𝌠` | Rang de 0..count que pot utilitzar-se com a índex. |
| `count` | `INT` | Nombre total de combinacions. |

