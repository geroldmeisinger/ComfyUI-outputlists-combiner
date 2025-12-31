## Spreadsheet OutputList

![Spreadsheet OutputList](SpreadsheetOutputList/SpreadsheetOutputList.png)

(Aliran kerja ComfyUI disertakan)

Menghasilkan pelbagai OutputList dari spreadsheet (`.csv .tsv .ods .xlsx .xls`).
Anda boleh menggunakan nod `Load any File` untuk memuat fail dalam pengenkodan base64.
Secara dalaman menggunakan *pandas* [read_excel](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html) dan [read_csv](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html) untuk memuat fail spreadsheet.
Semua senarai menggunakan `is_output_list=True` (ditunjukkan oleh simbol `𝌠`) dan akan diproses secara berurutan oleh nod yang bersesuaian.

### Input

| Nama | Jenis | Keterangan |
| --- | --- | --- |
| `rows_and_cols` | `STRING` | Indeks dan nama baris dan lajur dalam spreadsheet. Perhatikan bahawa dalam spreadsheet baris bermula pada 1, lajur bermula pada A, manakala OutputList adalah berdasarkan 0 (dalam `select-nth`). |
| `header_rows` | `INT` | Abaikan x baris pertama dalam senarai. Hanya digunakan jika anda menentukan lajur dalam `rows_and_cols`. |
| `header_cols` | `INT` | Abaikan x lajur pertama dalam senarai. Hanya digunakan jika anda menentukan baris dalam `rows_and_cols`. |
| `select_nth` | `INT` | Hanya pilih entri ke-n (berdasarkan 0). Berguna dalam kombinasi dengan corak `PrimitiveInt+control_after_generate=increment`. |
| `string_or_base64` | `STRING` | Rentetan CSV/TSV atau fail spreadsheet dalam base64 (untuk `.ods .xlsx .xls`). Gunakan nod `Load Any File` untuk memuat fail sebagai base64. |

### Output

| Nama | Jenis | Keterangan |
| --- | --- | --- |
| `list_a` | `STRING 𝌠` |  |
| `list_b` | `STRING 𝌠` |  |
| `list_c` | `STRING 𝌠` |  |
| `list_d` | `STRING 𝌠` |  |
| `count` | `INT` | Bilangan item dalam senarai terpanjang. |

