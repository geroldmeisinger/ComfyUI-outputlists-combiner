## Number OutputList

![Number OutputList](NumberOutputList/NumberOutputList.png)

(ComfyUI workflow bijgevoegd)

Maakt ‘n OutputList um ‘n reeks numerieke waardes.
Gebrukt [numpy.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html) intern, um um ‘t beter te werke um me met floating-point waardes.
Es ge ‘n lijst um nummers met willekeurige stappe wil definieer, kiek dan um de JSON OutputList en definieer ‘n array, b.v. `[1, 42, 123]`.
`int`, `float`, `string` en `index` gebruk `is_output_list=True` (aangegeven door ‘t symbool `𝌠`) en zien verwerkt in sequentiele nodes.

### Invoere

| Naom | Type | Beschrèving |
| --- | --- | --- |
| `start` | `FLOAT` | Start waarde um de reeks te generere. |
| `stop` | `FLOAT` | Einde waarde. Es `endpoint=include` dan is ‘t getal opgenome in de lijst. |
| `num` | `INT` | ‘t Aantal items um de lijst (vergess ‘t neet met ‘n `step`). |
| `endpoint` | `BOOLEAN` | Beslist es de `stop` waarde opgenome of uitgeklèrd moet zien in de items. |

### Uitvoere

| Naom | Type | Beschrèving |
| --- | --- | --- |
| `int` | `INT 𝌠` | De waarde omgerekend um int (afgerond/verlaagd). |
| `float` | `FLOAT 𝌠` | De waarde as ‘n float. |
| `string` | `STRING 𝌠` | De waarde as ‘n float omgerekend um string. |
| `index` | `INT 𝌠` | Reeks um 0..count wat gebrukt kin zien um ‘n index te make. |
| `count` | `INT` | Het zelfde es `num`. |

