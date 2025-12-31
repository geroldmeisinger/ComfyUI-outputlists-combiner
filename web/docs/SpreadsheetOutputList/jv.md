## OutputList Spreadsheet

![OutputList Spreadsheet](SpreadsheetOutputList/SpreadsheetOutputList.png)

(Workflow ComfyUI kalebu)

Nggawé OutputList ganda saka spreadsheet (`.csv .tsv .ods .xlsx .xls`).
Sampeyan bisa nggunakaké node `Load any File` supaya nglmuat file kanthi encoding base64.
Ing ngisoré nggunakaké *pandas* [read_excel](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html) lan [read_csv](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html) supaya nglmuat file spreadsheet.
Kabeh daptar nggunakaké `is_output_list=True` (indikasi dening simbol `𝌠`) lan bakal diprosés kanthi urutan dening node sing padha.

### Input

| Jeneng | Tipe | Description |
| --- | --- | --- |
| `rows_and_cols` | `STRING` | Indeks lan jeneng saka baris lan kolom ing spreadsheet. Catet yen ing spreadsheet baris munggung ing 1, kolom munggung ing A, amarga OutputLists iki 0-based (ing `select-nth`). |
| `header_rows` | `INT` | Abaikan x baris pertama ing daptar. Mung digunakaké yen sampeyan nyebutake kolom ing `rows_and_cols`. |
| `header_cols` | `INT` | Abaikan x kolom pertama ing daptar. Mung digunakaké yen sampeyan nyebutake baris ing `rows_and_cols`. |
| `select_nth` | `INT` | Mung pilih entri ke-n (0-based). Bisa digunakaké dening kombinasi karo pola `PrimitiveInt+control_after_generate=increment`. |
| `string_or_base64` | `STRING` | String CSV/TSV utawa file spreadsheet kanthi base64 (kanggo `.ods .xlsx .xls`). Nggunakaké node `Load Any File` supaya nglmuat file kanthi base64. |

### Output

| Jeneng | Tipe | Description |
| --- | --- | --- |
| `list_a` | `STRING 𝌠` |  |
| `list_b` | `STRING 𝌠` |  |
| `list_c` | `STRING 𝌠` |  |
| `list_d` | `STRING 𝌠` |  |
| `count` | `INT` | Jumlah item ing daptar paling dawa. |

