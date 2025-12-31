## Číslo OutputList

![Number OutputList](NumberOutputList/NumberOutputList.png)

(ComfyUI workflow je zahrnutý)

Vytvorí OutputList s rozsahom číselných hodnôt.
Používa interné [numpy.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html), pretože pracuje spoľahlivejšie s hodnotami s plávajúcou desatinnou čiarkou.
Ak chcete definovať zoznamy čísel s ľubovoľnými krokmi, pozrite si JSON OutputList a definujte pole, napr. `[1, 42, 123]`.
`int`, `float`, `string` a `index` používajú `is_output_list=True` (označené symbolom `𝌠`) a budú spracované postupne príslušnými uzlami.

### Vstupy

| Názov | Typ | Popis |
| --- | --- | --- |
| `start` | `FLOAT` | Počiatočná hodnota na generovanie rozsahu. |
| `stop` | `FLOAT` | Koncová hodnota. Ak `endpoint=include`, potom sa táto hodnota zahrnie do zoznamu. |
| `num` | `INT` | Počet položiek v zozname (nesmie sa zmiešať s `step`). |
| `endpoint` | `BOOLEAN` | Určuje, či má byť hodnota `stop` zahrnutá alebo vylúčená z položiek. |

### Výstupy

| Názov | Typ | Popis |
| --- | --- | --- |
| `int` | `INT 𝌠` | Hodnota prevádzaná na int (zaokrúhlená nadol/podlžaná). |
| `float` | `FLOAT 𝌠` | Hodnota ako float. |
| `string` | `STRING 𝌠` | Hodnota ako float prevádzaná na reťazec. |
| `index` | `INT 𝌠` | Rozsah 0..count, ktorý môže byť použitý ako index. |
| `count` | `INT` | Rovnaké ako `num`. |

