<!-- This file was auto-translated with a local LLM and last updated on 2025-12-27. -->
## Combinacion de las Listas de Sortida

![Combinacion de las Listas de Sortida](CombineOutputLists/CombineOutputLists.png)

(Workflow de ComfyUI inclòs)

Prend las listas de sortida fins a 4 e genera tota la combinacion de las meteis.

Exemple: `[1, 2, 3] x ["A", "B"] = [(1, "A"), (1, "B"), (2, "A"), (2, "B"), (3, "A"), (3, "B")]`

`unzip_a` .. `unzip_d` son (son) `is_output_list=True` (indicat per lo simbol `𝌠`) e son processats sequencialment per las nòdas correspòndents.

Totes las listas son opcionals e las listas vides son ignoradas.

Tècnicament, calcula *el producte cartesiano* e emet cada combinacion separada en las seus elements (`unzip`), amb las listas vides que son remplaces per unitats de `None` e emeten `None` en la sortida correspòndent.

Exemple: `[1, 2] x [] x ["A", "B"] x [] = [(1, None, "A", None), (1, None, "B", None), (2, None, "A", None), (2, None, "B", None)]`

### Entradas

| Nom | Tipus | Descripció |
| --- | --- | --- |
| `list_a` | `*` | (opcionau) |
| `list_b` | `*` | (opcionau) |
| `list_c` | `*` | (opcionau) |
| `list_d` | `*` | (opcionau) |

### Sortides

| Nom | Tipus | Descripció |
| --- | --- | --- |
| `unzip_a` | `* 𝌠` | Valor de las combinacions correspondents a `list_a`. |
| `unzip_b` | `* 𝌠` | Valor de las combinacions correspondents a `list_b`. |
| `unzip_c` | `* 𝌠` | Valor de las combinacions correspondents a `list_c`. |
| `unzip_d` | `* 𝌠` | Valor de las combinacions correspondents a `list_d`. |
| `index` | `INT 𝌠` | Rang de 0..count que pòt ser utilizat coma index. |
| `count` | `INT` | Nombre total de combinacions. |

