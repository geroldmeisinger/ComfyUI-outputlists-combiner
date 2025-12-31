## Getal OutputList

![Getal OutputList](NumberOutputList/NumberOutputList.png)

(ComfyUI workflow ingesluit)

Skep 'n OutputList met 'n reeks numeriese waardes.
Gebruik intern [numpy.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html), omdat dit meer betroubaar werk met dryfkomma waardes.
As jy wil om getallies te definieer met arbitrêre stappe eerder kyk na die JSON OutputList en definieer 'n array, byvoorbeeld `[1, 42, 123]`.
`int`, `float`, `string` en `index` gebruik `is_output_list=True` (aangedui deur die simbool `𝌠`) en sal sekwensieel deur ooreenstemmende nodes verwerk word.

### Invoere

| Naam | Tipe | Beskrywing |
| --- | --- | --- |
| `start` | `FLOAT` | Beginwaarde om die reeks van te genereer. |
| `stop` | `FLOAT` | Eindwaarde. As `endpoint=include` dan is hierdie getal in die lys ingesluit. |
| `num` | `INT` | Die aantal items in die lys (verwys dit nie met 'n `step`). |
| `endpoint` | `BOOLEAN` | Besluit of die `stop` waarde in die items ingesluit of uitgesluit moet word. |

### Uitvoere

| Naam | Tipe | Beskrywing |
| --- | --- | --- |
| `int` | `INT 𝌠` | Die waarde omgeskakel na int (afgerond af/verdeel). |
| `float` | `FLOAT 𝌠` | Die waarde as 'n float. |
| `string` | `STRING 𝌠` | Die waarde as 'n float omgeskakel na string. |
| `index` | `INT 𝌠` | Reeks van 0..count wat as 'n index gebruik kan word. |
| `count` | `INT` | Selfde as `num`. |

