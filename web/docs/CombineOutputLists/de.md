## OutputLists Kombinationen

![OutputLists Kombinationen](CombineOutputLists/CombineOutputLists.png)

(ComfyUI workflow inkludiert)

Nimmt bis zu 4 OutputLists entgegen und generiert jede Kombination daraus.

Beispiel: `[1, 2, 3] x ["A", "B"] = [(1, "A"), (1, "B"), (2, "A"), (2, "B"), (3, "A"), (3, "B")]`

`unzip_a` .. `unzip_d` verwendet(s) `is_output_list=True` (angezeigt durch das Symbol `𝌠`) und wird(n) sequenziell von entsprechenden Knoten verarbeitet.

Alle Listen sind optional und leere Listen werden ignoriert.

Technisch berechnet es das *Kartesische Produkt* und gibt jede Kombination aufgeteilt in ihre Elemente aus (`unzip`), wobei leere Listen durch Einheiten von `None` ersetzt werden und diese `None` auf der jeweiligen Ausgabe emittieren.

Beispiel: `[1, 2] x [] x ["A", "B"] x [] = [(1, None, "A", None), (1, None, "B", None), (2, None, "A", None), (2, None, "B", None)]`

### Eingaben

| Name | Typ | Beschreibung |
| --- | --- | --- |
| `list_a` | `*` | (optional) |
| `list_b` | `*` | (optional) |
| `list_c` | `*` | (optional) |
| `list_d` | `*` | (optional) |

### Ausgaben

| Name | Typ | Beschreibung |
| --- | --- | --- |
| `unzip_a` | `* 𝌠` | Wert der Kombinationen entsprechend `list_a`. |
| `unzip_b` | `* 𝌠` | Wert der Kombinationen entsprechend `list_b`. |
| `unzip_c` | `* 𝌠` | Wert der Kombinationen entsprechend `list_c`. |
| `unzip_d` | `* 𝌠` | Wert der Kombinationen entsprechend `list_d`. |
| `index` | `INT 𝌠` | Bereich von 0..count, welcher als Index verwendet werden kann. |
| `count` | `INT` | Gesamtzahl der Kombinationen. |

