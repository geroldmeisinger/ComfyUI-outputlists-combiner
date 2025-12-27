<!-- This file was auto-translated with a local LLM and last updated on 2025-12-27. -->
## Kombination vun OutputLists

![Kombination vun OutputLists](CombineOutputLists/CombineOutputLists.png)

(ComfyUI workflow eingeschlossen)

Nimmt bis zu 4 OutputLists an an erzeugt alli Kombinationen vun der.

Beispiel: `[1, 2, 3] x ["A", "B"] = [(1, "A"), (1, "B"), (2, "A"), (2, "B"), (3, "A"), (3, "B")]`

`unzip_a` .. `unzip_d` benotzt `is_output_list=True` (d'Zeichen `𝌠`) an wärend séier sequentiel verarbeite vun der entsprechende Node.

All Listen sinn optional an leere Listen wärend ignoriert.

Technisch rechnet es *den kartesischen Produkt* aus an späit d'Kombinationen a d'Elemente („unzip“) aus, wärend leere Listen durch `None` ersetzt gëtt an `None` an der entsprechende Ausgabesignal emittéiert.

Beispiel: `[1, 2] x [] x ["A", "B"] x [] = [(1, None, "A", None), (1, None, "B", None), (2, None, "A", None), (2, None, "B", None)]`

### Eingabes

| Name | Typ | Beschriwwung |
| --- | --- | --- |
| `list_a` | `*` | (optional) |
| `list_b` | `*` | (optional) |
| `list_c` | `*` | (optional) |
| `list_d` | `*` | (optional) |

### Ausgabes

| Name | Typ | Beschriwwung |
| --- | --- | --- |
| `unzip_a` | `* 𝌠` | Wäert vun der Kombinationen, déi `list_a` entspricht. |
| `unzip_b` | `* 𝌠` | Wäert vun der Kombinationen, déi `list_b` entspricht. |
| `unzip_c` | `* 𝌠` | Wäert vun der Kombinationen, déi `list_c` entspricht. |
| `unzip_d` | `* 𝌠` | Wäert vun der Kombinationen, déi `list_d` entspricht. |
| `index` | `INT 𝌠` | Bereich vun 0..count, déi als Index benotzt gëtt. |
| `count` | `INT` | Gesamte Zuel vun Kombinationen. |

