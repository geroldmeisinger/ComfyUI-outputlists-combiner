<!-- This file was auto-translated with a local LLM and last updated on 2025-12-27. -->
## Kombinácie OutputListov

![Kombinácie OutputListov](CombineOutputLists/CombineOutputLists.png)

(zahrnutý ComfyUI workflow)

Prijíma až 4 OutputListy a generuje všetky ich kombinácie.

Príklad: `[1, 2, 3] x ["A", "B"] = [(1, "A"), (1, "B"), (2, "A"), (2, "B"), (3, "A"), (3, "B")]`

`unzip_a` .. `unzip_d` používa `is_output_list=True` (označené symbolom `𝌠`) a budú postupne spracované príslušnými uzlami.

Všetky zoznamy sú voľné a prázdne zoznamy budú ignorované.

Technicky vypočíta *kartézsky súčin* a výstupom sú každé kombinácie rozdelené na ich prvky (`unzip`), pričom prázdne zoznamy budú nahradené jednotkami `None` a výstupom `None` na príslušnom výstupe.

Príklad: `[1, 2] x [] x ["A", "B"] x [] = [(1, None, "A", None), (1, None, "B", None), (2, None, "A", None), (2, None, "B", None)]`

### Vstupy

| Meno | Typ | Popis |
| --- | --- | --- |
| `list_a` | `*` | (voliteľné) |
| `list_b` | `*` | (voliteľné) |
| `list_c` | `*` | (voliteľné) |
| `list_d` | `*` | (voliteľné) |

### Výstupy

| Meno | Typ | Popis |
| --- | --- | --- |
| `unzip_a` | `* 𝌠` | Hodnota kombinácií prislúšiacich k `list_a`. |
| `unzip_b` | `* 𝌠` | Hodnota kombinácií prislúšiacich k `list_b`. |
| `unzip_c` | `* 𝌠` | Hodnota kombinácií prislúšiacich k `list_c`. |
| `unzip_d` | `* 𝌠` | Hodnota kombinácií prislúšiacich k `list_d`. |
| `index` | `INT 𝌠` | Riešenie od 0..count, ktoré môže byť použité ako index. |
| `count` | `INT` | Celkový počet kombinácií. |

