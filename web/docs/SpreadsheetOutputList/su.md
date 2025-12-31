## Spreadsheet OutputList

![Spreadsheet OutputList](SpreadsheetOutputList/SpreadsheetOutputList.png)

(ComfyUI workflow included)

Mangaharti OutputList sabarapakeun tina spreadsheet (`.csv .tsv .ods .xlsx .xls`).
Anjeun bisa nganggo `Load any File` node pikeun ngalodha file dina base64-encoding.
Di dasar manggunaakeun *pandas* [read_excel](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html) jeung [read_csv](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html) pikeun ngalodha file spreadsheet.
Sadaya list nganggo(s) `is_output_list=True` (diindikasikeun ku simbol `𝌠`) jeung bakal diprosés secara sequential ku node nu cocog.

### Inputs

| Nama | Tipe | Deskripsi |
| --- | --- | --- |
| `rows_and_cols` | `STRING` | Indeks jeung ngaran baris jeung kolom dina spreadsheet. Catetan: dina spreadsheet baris mimiti di 1, kolom mimiti di A, sementara OutputLists manggunaakeun 0-based (dina `select-nth`). |
| `header_rows` | `INT` | Abaikan x baris mungkam dina list. Hanya dipakékeun nu anjeun ngaspileun kolom dina `rows_and_cols`. |
| `header_cols` | `INT` | Abaikan x kolom mungkam dina list. Hanya dipakékeun nu anjeun ngaspileun baris dina `rows_and_cols`. |
| `select_nth` | `INT` | Pilih hanyana entri nth (0-based). Useful in combination with the `PrimitiveInt+control_after_generate=increment` pattern. |
| `string_or_base64` | `STRING` | String CSV/TSV jeung file spreadsheet dina base64 (pikeun `.ods .xlsx .xls`). Gunaken node `Load Any File` pikeun ngalodha file dina base64. |

### Outputs

| Nama | Tipe | Deskripsi |
| --- | --- | --- |
| `list_a` | `STRING 𝌠` |  |
| `list_b` | `STRING 𝌠` |  |
| `list_c` | `STRING 𝌠` |  |
| `list_d` | `STRING 𝌠` |  |
| `count` | `INT` | Jumlah item dina list anu pangjanten. |

