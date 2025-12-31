## Combinasons de las listas de sortida

![Combinasons de las listas de sortida](CombineOutputLists/CombineOutputLists.png)

(ComfyUI workflow incluch)

Prene fins a 4 listas de sortida e generà totas las combinasons.

Exemple: `[1, 2, 3] x ["A", "B"] = [(1, "A"), (1, "B"), (2, "A"), (2, "B"), (3, "A"), (3, "B")]`

`unzip_a` .. `unzip_d` utiliza(s) `is_output_list=True` (indicat per lo simbòl `𝌠`) e serà processat sequencialament per las nodes correspondents.

Totas las listas son facultativas e las listas voidas seràn ignoradas.

Tècnicament calcula *lo producte cartesià* e emèt cada combinason separada en sos elements (`unzip`), lors de las listas voidas seràn remplaçadas per de units de `None` e emetràn `None` sus la sortida respectiva.

Exemple: `[1, 2] x [] x ["A", "B"] x [] = [(1, None, "A", None), (1, None, "B", None), (2, None, "A", None), (2, None, "B", None)]`

### Entradas

| Nom | Tipe | Descripcion |
| --- | --- | --- |
| `list_a` | `*` | (facultatiu) |
| `list_b` | `*` | (facultatiu) |
| `list_c` | `*` | (facultatiu) |
| `list_d` | `*` | (facultatiu) |

### Sortidas

| Nom | Tipe | Descripcion |
| --- | --- | --- |
| `unzip_a` | `* 𝌠` | Valor de las combinasons correspondents a `list_a`. |
| `unzip_b` | `* 𝌠` | Valor de las combinasons correspondents a `list_b`. |
| `unzip_c` | `* 𝌠` | Valor de las combinasons correspondents a `list_c`. |
| `unzip_d` | `* 𝌠` | Valor de las combinasons correspondents a `list_d`. |
| `index` | `INT 𝌠` | Interval de 0..count que pòt èsser utilizat coma un indèx. |
| `count` | `INT` | Nombre total de combinasons. |

