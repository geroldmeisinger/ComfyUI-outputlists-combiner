## Tabeli väljundloend

![Tabeli väljundloend](SpreadsheetOutputList/SpreadsheetOutputList.png)

(ComfyUI töövoog on kaasatud)

Loob mitmeid väljundloendeid tabelist (`.csv .tsv .ods .xlsx .xls`).
Saad kasutada `Load any File` sõlme, et laadida fail base64-kodeerimisega.
Sisemiselt kasutab *pandas* [read_excel](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html) ja [read_csv](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html) tabelifailide laadimiseks.
Kõik loendid kasutavad `is_output_list=True` (märgitud sümboliga `𝌠`) ja neid töödeldakse järjestikku vastavate sõlmede poolt.

### Sisendid

| Nimi | Tüüp | Kirjeldus |
| --- | --- | --- |
| `rows_and_cols` | `STRING` | Tabeli ridade ja veergude indeksid ja nimed. Pange tähele, et tabelites read algavad 1-st, veerud algavad A-st, samas kui väljundloendid on 0-põhised (või `select-nth`). |
| `header_rows` | `INT` | Ignoreeri esimest x rida loendis. Kasutatakse ainult siis, kui sa määratled veeru `rows_and_cols` sees. |
| `header_cols` | `INT` | Ignoreeri esimest x veergu loendis. Kasutatakse ainult siis, kui sa määratled rea `rows_and_cols` sees. |
| `select_nth` | `INT` | Vali ainult nt sissekanne (0-põhine). Kasulik koos `PrimitiveInt+control_after_generate=increment` mustriga. |
| `string_or_base64` | `STRING` | CSV/TSV string või tabelifail base64-kodeeringus (või `.ods .xlsx .xls`). Kasuta `Load Any File` sõlme, et laadida fail base64-kodeeringus. |

### Väljundid

| Nimi | Tüüp | Kirjeldus |
| --- | --- | --- |
| `list_a` | `STRING 𝌠` |  |
| `list_b` | `STRING 𝌠` |  |
| `list_c` | `STRING 𝌠` |  |
| `list_d` | `STRING 𝌠` |  |
| `count` | `INT` | Kõige pikema loendi elementide arv. |

