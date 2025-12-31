## Izvoz seznama preglednice

![Izvoz seznama preglednice](SpreadsheetOutputList/SpreadsheetOutputList.png)

(Vključen je ComfyUI workflow)

Ustvari več seznamov iz preglednice (`.csv .tsv .ods .xlsx .xls`).
Uporabite vozlišče `Load any File` za nalaganje datoteke v base64-kodiranju.
Notranje uporablja *pandas* [read_excel](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html) in [read_csv](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html) za nalaganje datotek preglednic.
Vsi seznami uporabljajo `is_output_list=True` (označeno z `𝌠`) in bodo obdelani zaporedno z ustrezna vozlišča.

### Vhodi

| Ime | Vrsta | Opis |
| --- | --- | --- |
| `rows_and_cols` | `STRING` | Indeksi in imena vrstic in stolpcev v preglednici. Upoštevajte, da v preglednicah začnejo vrstice pri 1, stolpci pri A, medtem ko so seznam izhodov 0-zasnovani (v `select-nth`). |
| `header_rows` | `INT` | Prezri prve x vrstic v seznamu. Uporablja se samo, če določite stolpec v `rows_and_cols`. |
| `header_cols` | `INT` | Prezri prve x stolpcev v seznamu. Uporablja se samo, če določite vrstico v `rows_and_cols`. |
| `select_nth` | `INT` | Izberi samo nth vnos (0-zasnovan). Uporabno v kombinaciji z vzorcem `PrimitiveInt+control_after_generate=increment`. |
| `string_or_base64` | `STRING` | CSV/TSV niz ali datoteka preglednice v base64 (za `.ods .xlsx .xls`). Uporabite vozlišče `Load Any File` za nalaganje datoteke kot base64. |

### Izhodi

| Ime | Vrsta | Opis |
| --- | --- | --- |
| `list_a` | `STRING 𝌠` |  |
| `list_b` | `STRING 𝌠` |  |
| `list_c` | `STRING 𝌠` |  |
| `list_d` | `STRING 𝌠` |  |
| `count` | `INT` | Število elementov v najdaljšem seznamu. |

