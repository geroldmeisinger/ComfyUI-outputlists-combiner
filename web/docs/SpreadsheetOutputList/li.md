## Spreadsheet OutputList

![Spreadsheet OutputList](SpreadsheetOutputList/SpreadsheetOutputList.png)

(ComfyUI workflow bijgevoegd)

Maakt meerdere OutputLists um ‘n spreadsheet (`.csv .tsv .ods .xlsx .xls`).
Ge kin ‘t `Load any File` node gebruke um ‘n bestand te laod um base64-encoding.
Intern gebrukt ‘t *pandas* [read_excel](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html) en [read_csv](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html) um spreadsheet bestande te laod.
Alle lijste gebruk `is_output_list=True` (aangegeven door ‘t symbool `𝌠`) en zien verwerkt in sequentiele nodes.

### Invoere

| Naom | Type | Beschrèving |
| --- | --- | --- |
| `rows_and_cols` | `STRING` | Indices en naam um rij en kolom um ‘t spreadsheet. Let op dat in spreadsheets rij um 1 beginne, kolom um A, terwijl OutputLists 0-based zien (in `select-nth`). |
| `header_rows` | `INT` | Negeer de eerste x rij um de lijst. Alleen gebrukt es ge ‘n kolom specificeer um `rows_and_cols`. |
| `header_cols` | `INT` | Negeer de eerste x kolom um de lijst. Alleen gebrukt es ge ‘n rij specificeer um `rows_and_cols`. |
| `select_nth` | `INT` | Alleen ‘t nth item selekteer (0-based). Nuttig um ‘t te combineren um ‘t `PrimitiveInt+control_after_generate=increment` patroon. |
| `string_or_base64` | `STRING` | CSV/TSV string of spreadsheet bestand um base64 (um `.ods .xlsx .xls`). Gebruk ‘t `Load Any File` node um ‘n bestand te laod um base64. |

### Uitvoere

| Naom | Type | Beschrèving |
| --- | --- | --- |
| `list_a` | `STRING 𝌠` |  |
| `list_b` | `STRING 𝌠` |  |
| `list_c` | `STRING 𝌠` |  |
| `list_d` | `STRING 𝌠` |  |
| `count` | `INT` | Aantal items um de langste lijst. |

