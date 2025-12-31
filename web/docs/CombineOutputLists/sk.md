## Prepojenie výstupných zoznamov

![Prepojenie výstupných zoznamov](CombineOutputLists/CombineOutputLists.png)

(ComfyUI workflow je zahrnutý)

Prijme až 4 výstupné zoznamy a vygeneruje každú kombináciu z nich.

Príklad: `[1, 2, 3] x ["A", "B"] = [(1, "A"), (1, "B"), (2, "A"), (2, "B"), (3, "A"), (3, "B")]`

`unzip_a` .. `unzip_d` používajú `is_output_list=True` (označené symbolom `𝌠`) a budú spracované postupne príslušnými uzlami.

Všetky zoznamy sú voliteľné a prázdne zoznamy budú ignorované.

Technicky vypočíta *karteziánsky súčin* a výstup každej kombinácie rozdelí na jednotlivé prvky (`unzip`), pričom prázdne zoznamy budú nahradené jednotkami `None` a vydajú `None` na príslušný výstup.

Príklad: `[1, 2] x [] x ["A", "B"] x [] = [(1, None, "A", None), (1, None, "B", None), (2, None, "A", None), (2, None, "B", None)]`

### Vstupy

| Názov | Typ | Popis |
| --- | --- | --- |
| `list_a` | `*` | (voliteľné) |
| `list_b` | `*` | (voliteľné) |
| `list_c` | `*` | (voliteľné) |
| `list_d` | `*` | (voliteľné) |

### Výstupy

| Názov | Typ | Popis |
| --- | --- | --- |
| `unzip_a` | `* 𝌠` | Hodnota kombinácií zodpovedajúcich `list_a`. |
| `unzip_b` | `* 𝌠` | Hodnota kombinácií zodpovedajúcich `list_b`. |
| `unzip_c` | `* 𝌠` | Hodnota kombinácií zodpovedajúcich `list_c`. |
| `unzip_d` | `* 𝌠` | Hodnota kombinácií zodpovedajúcich `list_d`. |
| `index` | `INT 𝌠` | Rozsah 0..count, ktorý možno použiť ako index. |
| `count` | `INT` | Celkový počet kombinácií. |

