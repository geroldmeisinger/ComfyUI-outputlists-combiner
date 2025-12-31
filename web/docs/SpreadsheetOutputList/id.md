## Spreadsheet OutputList

![Spreadsheet OutputList](SpreadsheetOutputList/SpreadsheetOutputList.png)

(ComfyUI workflow disertakan)

Membuat beberapa OutputList dari spreadsheet (`.csv .tsv .ods .xlsx .xls`).
Anda dapat menggunakan node `Load any File` untuk memuat file dalam encoding base64.
Secara internal menggunakan *pandas* [read_excel](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html) dan [read_csv](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html) untuk memuat file spreadsheet.
Semua daftar menggunakan `is_output_list=True` (ditunjukkan oleh simbol `𝌠`) dan akan diproses secara berurutan oleh node-node yang sesuai.

### Masukan

| Nama | Jenis | Deskripsi |
| --- | --- | --- |
| `rows_and_cols` | `STRING` | Indeks dan nama baris dan kolom dalam spreadsheet. Perhatikan bahwa dalam spreadsheet baris dimulai dari 1, kolom dimulai dari A, sedangkan OutputList berbasis 0 (dalam `select-nth`). |
| `header_rows` | `INT` | Abaikan x baris pertama dalam daftar. Hanya digunakan jika Anda menentukan kolom dalam `rows_and_cols`. |
| `header_cols` | `INT` | Abaikan x kolom pertama dalam daftar. Hanya digunakan jika Anda menentukan baris dalam `rows_and_cols`. |
| `select_nth` | `INT` | Hanya pilih entri ke-n (berbasis 0). Berguna dalam kombinasi dengan pola `PrimitiveInt+control_after_generate=increment`. |
| `string_or_base64` | `STRING` | String CSV/TSV atau file spreadsheet dalam base64 (untuk `.ods .xlsx .xls`). Gunakan node `Load Any File` untuk memuat file sebagai base64. |

### Keluaran

| Nama | Jenis | Deskripsi |
| --- | --- | --- |
| `list_a` | `STRING 𝌠` |  |
| `list_b` | `STRING 𝌠` |  |
| `list_c` | `STRING 𝌠` |  |
| `list_d` | `STRING 𝌠` |  |
| `count` | `INT` | Jumlah item dalam daftar terpanjang. |

