## Regneark OutputList

![Regneark OutputList](SpreadsheetOutputList/SpreadsheetOutputList.png)

(ComfyUI workflow inkluderet)

Opretter flere OutputList fra et regneark (`.csv .tsv .ods .xlsx .xls`).
Du kan bruge `Load any File` noden til at indlæse en fil i base64-kodning.
Bruger internt *pandas* [read_excel](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html) og [read_csv](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html) til at indlæse regnearkfiler.
Alle lister bruger `is_output_list=True` (angivet af symbolet `𝌠`) og vil blive behandlet sekventielt af tilsvarende noder.

### Input

| Navn | Type | Beskrivelse |
| --- | --- | --- |
| `rows_and_cols` | `STRENG` | Indeks og navne på rækker og kolonner i regnearket. Bemærk at rækker i regneark starter ved 1, kolonner starter ved A, mens OutputList er 0-baseret (i `select-nth`). |
| `header_rows` | `HELTAL` | Ignorer de første x rækker i listen. Bruges kun hvis du specificerer en kolonne i `rows_and_cols`. |
| `header_cols` | `HELTAL` | Ignorer de første x kolonner i listen. Bruges kun hvis du specificerer en række i `rows_and_cols`. |
| `select_nth` | `HELTAL` | Vælg kun det nth element (0-baseret). Nyttigt i kombination med mønstret `PrimitiveInt+control_after_generate=increment`. |
| `string_or_base64` | `STRENG` | CSV/TSV streng eller regnearkfil i base64 (for `.ods .xlsx .xls`). Brug `Load Any File` noden til at indlæse en fil som base64. |

### Output

| Navn | Type | Beskrivelse |
| --- | --- | --- |
| `list_a` | `STRENG 𝌠` |  |
| `list_b` | `STRENG 𝌠` |  |
| `list_c` | `STRENG 𝌠` |  |
| `list_d` | `STRENG 𝌠` |  |
| `count` | `HELTAL` | Antal elementer i den længste liste. |

