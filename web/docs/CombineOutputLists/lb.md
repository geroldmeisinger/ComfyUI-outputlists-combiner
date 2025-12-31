## Kombinatioune vun der Ausgabelëscht

![Kombinatioune vun der Ausgabelëscht](CombineOutputLists/CombineOutputLists.png)

(ComfyUI workflow as inbegrëff)

Nim maximal 4 Ausgabelëschte a generéiert all Kombinatioune vun der. 

Beispill: `[1, 2, 3] x ["A", "B"] = [(1, "A"), (1, "B"), (2, "A"), (2, "B"), (3, "A"), (3, "B")]`

`unzip_a` .. `unzip_d` benotzt `is_output_list=True` (indizéiert duerch den Symbol `𝌠`) a gëtt sequentiell duerch déi zugehörenden Nodes verarbeid.

All Lëschte sinn optional a eidel Lëschte ginn ignoréiert.

Technesch berechnet et *das kartesisch Produkt* a gëff all Kombinatioun opgeléist an d'Elementer (`unzip`), wou eidel Lëschte duerch `None` ersetzt ginn a `None` op dem zugehörenden Ausgang sende.

Beispill: `[1, 2] x [] x ["A", "B"] x [] = [(1, None, "A", None), (1, None, "B", None), (2, None, "A", None), (2, None, "B", None)]`

### Input

| Numm | Typ | Beschreiwung |
| --- | --- | --- |
| `list_a` | `*` | (optional) |
| `list_b` | `*` | (optional) |
| `list_c` | `*` | (optional) |
| `list_d` | `*` | (optional) |

### Ausgab

| Numm | Typ | Beschreiwung |
| --- | --- | --- |
| `unzip_a` | `* 𝌠` | Wäert vun den Kombinatioune déi duerch `list_a` entsprëchen. |
| `unzip_b` | `* 𝌠` | Wäert vun den Kombinatioune déi duerch `list_b` entsprëchen. |
| `unzip_c` | `* 𝌠` | Wäert vun den Kombinatioune déi duerch `list_c` entsprëchen. |
| `unzip_d` | `* 𝌠` | Wäert vun den Kombinatioune déi duerch `list_d` entsprëchen. |
| `index` | `INT 𝌠` | Beräich vun 0..count déi als Index benotzt ka ginn. |
| `count` | `INT` | Gesamte Zuel vun den Kombinatioune. |

