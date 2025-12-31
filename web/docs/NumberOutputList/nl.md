## Number OutputList

![Number OutputList](NumberOutputList/NumberOutputList.png)

(ComfyUI workflow inbegrepen)

Maakt een OutputList met een reeks numerieke waarden.
Gebruikt intern [numpy.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html), omdat het betrouwbaarder werkt met floating-point waarden.
Als je nummerlijsten met willekeurige stappen wilt definiëren, kijk dan naar de JSON OutputList en definieer een array, bijvoorbeeld `[1, 42, 123]`.
`int`, `float`, `string` en `index` gebruiken `is_output_list=True` (aangegeven door het symbool `𝌠`) en worden sequentieel verwerkt door overeenkomstige nodes.

### Invoer

| Naam | Type | Beschrijving |
| --- | --- | --- |
| `start` | `FLOAT` | Startwaarde om de reeks van te genereren. |
| `stop` | `FLOAT` | Eindwaarde. Als `endpoint=include` dan is dit getal opgenomen in de lijst. |
| `num` | `INT` | Het aantal items in de lijst (verwar dit niet met een `step`). |
| `endpoint` | `BOOLEAN` | Bepaalt of de `stop`-waarde moet worden opgenomen of uitgesloten in de items. |

### Uitvoer

| Naam | Type | Beschrijving |
| --- | --- | --- |
| `int` | `INT 𝌠` | De waarde geconverteerd naar int (afgerond naar beneden/afgebroken). |
| `float` | `FLOAT 𝌠` | De waarde als een float. |
| `string` | `STRING 𝌠` | De waarde als een float geconverteerd naar string. |
| `index` | `INT 𝌠` | Bereik van 0..count die kan worden gebruikt als index. |
| `count` | `INT` | Hetzelfde als `num`. |

