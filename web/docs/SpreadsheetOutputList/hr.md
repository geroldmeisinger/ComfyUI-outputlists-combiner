## Spreadsheet OutputList

![Spreadsheet OutputList](SpreadsheetOutputList/SpreadsheetOutputList.png)

(ComfyUI workflow uključen)

Stvara više OutputList-a iz tablice (`.csv .tsv .ods .xlsx .xls`).
Možete koristiti čvor `Load any File` za učitavanje datoteke u base64-kodiranju.
Unutarnje koristi *pandas* [read_excel](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html) i [read_csv](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html) za učitavanje datoteka tablica.
Svi popisi koriste(s) `is_output_list=True` (označeno simbolom `𝌠`) i bit će obrađeni redoslijedom odgovarajućim čvorovima.

### Ulazi

| Ime | Vrsta | Opis |
| --- | --- | --- |
| `rows_and_cols` | `NIZ ZNAKOVA` | Indeksi i imena redaka i stupaca u tablici. Imajte na umu da u tablicama redovi počinju od 1, stupci počinju od A, dok OutputListovi koriste 0-zasnovani indeks (u `select-nth`). |
| `header_rows` | `CJELI BROJ` | Zanemari prva x redaka u listi. Koristi se samo ako navedete stupac u `rows_and_cols`. |
| `header_cols` | `CJELI BROJ` | Zanemari prva x stupaca u listi. Koristi se samo ako navedete redak u `rows_and_cols`. |
| `select_nth` | `CJELI BROJ` | Odaberi samo n-ti unos (0-zasnovano). Korisno u kombinaciji s `PrimitiveInt+control_after_generate=povećanje` uzorkom. |
| `string_or_base64` | `NIZ ZNAKOVA` | CSV/TSV niz znakova ili datoteka tablice u base64 (za `.ods .xlsx .xls`). Koristite čvor `Load Any File` za učitavanje datoteke kao base64. |

### Izlazi

| Ime | Vrsta | Opis |
| --- | --- | --- |
| `list_a` | `NIZ ZNAKOVA 𝌠` |  |
| `list_b` | `NIZ ZNAKOVA 𝌠` |  |
| `list_c` | `NIZ ZNAKOVA 𝌠` |  |
| `list_d` | `NIZ ZNAKOVA 𝌠` |  |
| `count` | `CJELI BROJ` | Broj stavki u najdužem popisu. |

