## Spreadsheet OutputList

![Spreadsheet OutputList](SpreadsheetOutputList/SpreadsheetOutputList.png)

(ComfyUI workflow ap gen yon pwogrè)

Kreye plizyè OutputLists sòti nan yon tab la (`.csv .tsv .ods .xlsx .xls`).
Ou kapab itilize nòd `Load any File` pou chaje yon fichye an kòd base64.
Anndan ap itilize *pandas* [read_excel](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html) ak [read_csv](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html) pou chaje fichye tab la.
Tout lis yo itilize `is_output_list=True` (indike pa simbòl `𝌠`) ak ap pwosese sèkilyèman pa nòd ki koresponn yo.

### Antre yo

| Non | Tip | Deskrisyon |
| --- | --- | --- |
| `rows_and_cols` | `CHENN` | Endèks ak non lèn ak kolonn nan tab la. Remarke ke nan tab yo lèn kòmanse nan 1, kolonn kòmanse nan A, men OutputLists yo se 0-based (nan `select-nth`). |
| `header_rows` | `ENTYE` | Enpoti premye x lèn nan lis la. Sèlman itilize si ou spesifye yon kolonn nan `rows_and_cols`. |
| `header_cols` | `ENTYE` | Enpoti premye x kolonn nan lis la. Sèlman itilize si ou spesifye yon lèn nan `rows_and_cols`. |
| `select_nth` | `ENTYE` | Sèlman chwazi nth antre (0-based). Utile nan kominasyon ak `PrimitiveInt+control_after_generate=increment` patèn. |
| `string_or_base64` | `CHENN` | Chenn CSV/TSV oswa fichye tab la an kòd base64 (pou `.ods .xlsx .xls`). Ap itilize nòd `Load Any File` pou chaje yon fichye an kòd base64. |

### Sòti yo

| Non | Tip | Deskrisyon |
| --- | --- | --- |
| `list_a` | `CHENN 𝌠` |  |
| `list_b` | `CHENN 𝌠` |  |
| `list_c` | `CHENN 𝌠` |  |
| `list_d` | `CHENN 𝌠` |  |
| `count` | `ENTYE` | Kantite objè nan lis ki pi long. |

