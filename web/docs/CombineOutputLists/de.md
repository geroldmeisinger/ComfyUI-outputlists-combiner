<!-- This file was auto-translated with a local LLM and last updated on 2025-12-27. -->
## Kombinationen von OutputLists

![Kombinationen von OutputLists](CombineOutputLists/CombineOutputLists.png)

(ComfyUI Workflow enthalten)

Nimmt bis zu 4 OutputLists auf und erzeugt jede Kombination daraus.

Beispiel: `[1, 2, 3] x ["A", "B"] = [(1, "A"), (1, "B"), (2, "A"), (2, "B"), (3, "A"), (3, "B")]`

`unzip_a` .. `unzip_d` verwenden `is_output_list=True` (durch das Symbol `𝌠` angegeben) und werden nacheinander von den entsprechenden Knoten verarbeitet.

Alle Listen sind optional und leere Listen werden ignoriert.

Technisch berechnet es das *kartesische Produkt* und gibt jede Kombination in ihre Elemente aufgeteilt aus (`unzip`), wobei leere Listen durch `None` ersetzt werden und auf dem entsprechenden Ausgang `None` emittieren.

Beispiel: `[1, 2] x [] x ["A", "B"] x [] = [(1, None, "A", None), (1, None, "B", None), (2, None, "A", None), (2, None, "B", None)]`

### Eingänge

| Name | Typ | Beschreibung |
| --- | --- | --- |
| `list_a` | `*` | (optional) |
| `list_b` | `*` | (optional) |
| `list_c` | `*` | (optional) |
| `list_d` | `*` | (optional) |

### Ausgaben

| Name | Typ | Beschreibung |
| --- | --- | --- |
| `unzip_a` | `* 𝌠` | Der Wert der Kombinationen, die auf `list_a` bezogen sind. |
| `unzip_b` | `* 𝌠` | Der Wert der Kombinationen, die auf `list_b` bezogen sind. |
| `unzip_c` | `* 𝌠` | Der Wert der Kombinationen, die auf `list_c` bezogen sind. |
| `unzip_d` | `* 𝌠` | Der Wert der Kombinationen, die auf `list_d` bezogen sind. |
| `index` | `INT 𝌠` | Bereich von 0..count, der als Index verwendet werden kann. |
| `count` | `INT` | Gesamtanzahl der Kombinationen. |

