## Spreadsheet OutputList

![Spreadsheet OutputList](SpreadsheetOutputList/SpreadsheetOutputList.png)

(ComfyUI radni tok je uključen)

Pravi više OutputList-a iz tablice (`.csv .tsv .ods .xlsx .xls`).
Možete koristiti čvor `Load any File` za učitavanje datoteke u base64-kodiranju.
Unutrašnje korištenje *pandas* [read_excel](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html) i [read_csv](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html) za učitavanje datoteka tablica.
Svi liste koriste `is_output_list=True` (označeno simbolom `𝌠`) i biće obrađeni redoslijedom odgovarajućim čvorovima.

### Ulazi

| Naziv | Tip | Opis |
| --- | --- | --- |
| `rows_and_cols` | `NIZ ZNAKOVA` | Indeksi i imena redova i kolona u tablici. Napomena: u tablicama redovi počinju od 1, kolone počinju od A, dok OutputListovi koriste 0-baziran (u `select-nth`). |
| `header_rows` | `INT` | Zanemari prve x redova u listi. Koristi se samo ako specificirate kolonu u `rows_and_cols`. |
| `header_cols` | `INT` | Zanemari prve x kolona u listi. Koristi se samo ako specificirate red u `rows_and_cols`. |
| `select_nth` | `INT` | Selektuj samo n-tu stavku (0-bazirano). Korisno u kombinaciji sa `PrimitiveInt+control_after_generate=increment` uzorkom. |
| `string_or_base64` | `NIZ ZNAKOVA` | CSV/TSV niz znakova ili datoteka tablice u base64 (za `.ods .xlsx .xls`). Koristi čvor `Load Any File` za učitavanje datoteke kao base64. |

### Izlazi

| Naziv | Tip | Opis |
| --- | --- | --- |
| `list_a` | `STRING 𝌠` |  |
| `list_b` | `STRING 𝌠` |  |
| `list_c` | `STRING 𝌠` |  |
| `list_d` | `STRING 𝌠` |  |
| `count` | `INT` | Broj stavki u najdužoj listi. |

