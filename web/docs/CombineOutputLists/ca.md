## Combinacions de llistes de sortida

![Combinacions de llistes de sortida](CombineOutputLists/CombineOutputLists.png)

(ComfyUI workflow inclosa)

Agafa fins a 4 llistes de sortida i genera totes les combinacions possibles.

Exemple: `[1, 2, 3] x ["A", "B"] = [(1, "A"), (1, "B"), (2, "A"), (2, "B"), (3, "A"), (3, "B")]`

`unzip_a` .. `unzip_d` utilitza(n) `is_output_list=True` (indicat pel símbol `𝌠`) i seran processats seqüencialment pels nodes corresponents.

Totes les llistes són opcionals i les llistes buides seran ignorades.

Tècnicament calcula *el producte cartesià* i genera cada combinació dividida en els seus elements (`unzip`), mentre que les llistes buides seran reemplaçades amb unitats de `None` i aquestes generaràn `None` a la sortida corresponent.

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
| `unzip_a` | `* 𝌠` | Valor de les combinacions corresponent a `list_a`. |
| `unzip_b` | `* 𝌠` | Valor de les combinacions corresponent a `list_b`. |
| `unzip_c` | `* 𝌠` | Valor de les combinacions corresponent a `list_c`. |
| `unzip_d` | `* 𝌠` | Valor de les combinacions corresponent a `list_d`. |
| `index` | `INT 𝌠` | Interval de 0..count que pot ser utilitzat com a índex. |
| `count` | `INT` | Nombre total de combinacions. |

