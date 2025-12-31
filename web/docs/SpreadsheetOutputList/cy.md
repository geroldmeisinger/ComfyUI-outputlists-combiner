## Rhif OutputList

![Rhif OutputList](SpreadsheetOutputList/SpreadsheetOutputList.png)

(Cyflun ComfyUI wedi'i gynnwys)

Creu lluosog OutputLists o ffeil sylfaen (`.csv .tsv .ods .xlsx .xls`).
Gallwch ddefnyddio'r nod `Llwytho unrhyw ffeil` i lwytho ffeil yn ymgorffedig base64.
Yn fewnol yn defnyddio *pandas* [read_excel](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html) a [read_csv](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html) i lwytho ffeiliau sylfaen.
Mae'r holl restrau yn defnyddio `is_output_list=True` (nodwyd gan y symbol `𝌠`) a byddai'n cael ei brosesu yn dilynol gan nodau cyfatebol.

### Mewnbwn

| Enw | Math | Disgrifiad |
| --- | --- | --- |
| `rows_and_cols` | `STRING` | Rhifau a enwau rhesi a colofnau yn y sylfaen. Sylwer bod yn sylfaenau rhesi yn dechrau o 1, colofnau yn dechrau o A, fodd bynnag mae OutputLists yn 0-sylfaen (yn `select-nth`). |
| `header_rows` | `INT` | Anwybyddwch y rhagor o x rhesi yn y rhestr. Dim ond yn defnyddio os ydych chi'n nodi col yn `rows_and_cols`. |
| `header_cols` | `INT` | Anwybyddwch y rhagor o x colofnau yn y rhestr. Dim ond yn defnyddio os ydych chi'n nodi rhes yn `rows_and_cols`. |
| `select_nth` | `INT` | Dim ond dewiswch y eitem nheg (0-sylfaen). Defnyddiol yn gyfuniad â'r patrwm `PrimitiveInt+control_after_generate=increment`. |
| `string_or_base64` | `STRING` | Llinyn CSV/TSV neu ffeil sylfaen yn ymgorffedig base64 (ar gyfer `.ods .xlsx .xls`). Defnyddiwch nod `Llwytho unrhyw ffeil` i lwytho ffeil fel base64. |

### Allbwn

| Enw | Math | Disgrifiad |
| --- | --- | --- |
| `list_a` | `STRING 𝌠` |  |
| `list_b` | `STRING 𝌠` |  |
| `list_c` | `STRING 𝌠` |  |
| `list_d` | `STRING 𝌠` |  |
| `count` | `INT` | Nifer y eitemau yn y rhestr hiraf. |

