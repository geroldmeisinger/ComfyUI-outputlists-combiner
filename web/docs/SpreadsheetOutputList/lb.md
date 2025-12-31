## Spreadsheet OutputList

![Spreadsheet OutputList](SpreadsheetOutputList/SpreadsheetOutputList.png)

(ComfyUI workflow d'ofgesech)

Erstellt e puer OutputLists aus enger Spreadsheet (`.csv .tsv .ods .xlsx .xls`).
Dir kënnt den `Load any File` Node benotzen, fir e Fichier mat base64-Kodéierung ze lueden.
Intern benotzt dës Node *pandas* [read_excel](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html) an [read_csv](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html), fir Spreadsheetdateien ze lueden.
All Lëschte benotzen (s) `is_output_list=True` (indizéiert duerch den Symbol `𝌠`) an ginn sequentiell duerch d'entspriechend Nodes verarbeit.

### Input

| Numm | Typ | Beschreiwung |
| --- | --- | --- |
| `rows_and_cols` | `STRING` | Indizes an Numm vun den Reie an Kolonnen an der Spreadsheet. Opgepasst, well an Spreadsheet Reie mat 1 starte, Kolonnen mat A, wärendd d'Späichlisten 0-basiert (an `select-nth`) sinn. |
| `header_rows` | `INT` | Ignoriéiert d'éischt x Reie an der Lëscht. Eegescht, wann Dir eng Kolonn an `rows_and_cols` specifizéiert. |
| `header_cols` | `INT` | Ignoriéiert d'éischt x Kolonnen an der Lëscht. Eegescht, wann Dir eng Reie an `rows_and_cols` specifizéiert. |
| `select_nth` | `INT` | Wählt nëmmen d'nth Element (0-basiert). Nützlech an Kombinatioun mat der `PrimitiveInt+control_after_generate=increment` Muster. |
| `string_or_base64` | `STRING` | CSV/TSV String oder Spreadsheet Fichier mat base64 (fir `.ods .xlsx .xls`). Benotzt den `Load Any File` Node, fir e Fichier als base64 ze lueden. |

### Output

| Numm | Typ | Beschreiwung |
| --- | --- | --- |
| `list_a` | `STRING 𝌠` |  |
| `list_b` | `STRING 𝌠` |  |
| `list_c` | `STRING 𝌠` |  |
| `list_d` | `STRING 𝌠` |  |
| `count` | `INT` | Zuel vun Elementer an der längsten Lëscht. |

