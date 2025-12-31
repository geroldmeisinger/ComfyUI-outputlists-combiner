## Spreadsheet OutputList

![Spreadsheet OutputList](SpreadsheetOutputList/SpreadsheetOutputList.png)

(ComfyUI workflow inclus)

Creează mai multe OutputList-uri dintr-un fișier de tip spreadsheet (`.csv .tsv .ods .xlsx .xls`).
Poți folosi nodul `Load any File` pentru a încărca un fișier în format base64.
În mod intern folosește *pandas* [read_excel](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html) și [read_csv](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html) pentru a încărca fișiere de tip spreadsheet.
Toate listele folosesc `is_output_list=True` (indicat de simbolul `𝌠`) și vor fi procesate secvențial de nodurile corespunzătoare.

### Intrări

| Nume | Tip | Descriere |
| --- | --- | --- |
| `rows_and_cols` | `STRING` | Indicii și numele rândurilor și coloanelor din spreadsheet. Rețineți că în fișierele de tip spreadsheet, rândurile încep de la 1, coloanele încep de la A, în timp ce OutputList-urile sunt 0-bazate (în `select-nth`). |
| `header_rows` | `INT` | Ignoră primele x rânduri din listă. Folosit doar dacă specifici o coloană în `rows_and_cols`. |
| `header_cols` | `INT` | Ignoră primele x coloane din listă. Folosit doar dacă specifici un rând în `rows_and_cols`. |
| `select_nth` | `INT` | Selectează doar intrarea de ordinul n (0-bazat). Util în combinație cu modelul `PrimitiveInt+control_after_generate=increment`. |
| `string_or_base64` | `STRING` | Șir CSV/TSV sau fișier de tip spreadsheet în base64 (pentru `.ods .xlsx .xls`). Folosește nodul `Load Any File` pentru a încărca un fișier în format base64. |

### Ieșiri

| Nume | Tip | Descriere |
| --- | --- | --- |
| `list_a` | `STRING 𝌠` |  |
| `list_b` | `STRING 𝌠` |  |
| `list_c` | `STRING 𝌠` |  |
| `list_d` | `STRING 𝌠` |  |
| `count` | `INT` | Numărul de elemente din cea mai lungă listă. |

