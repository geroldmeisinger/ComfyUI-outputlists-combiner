## Spreadsheet OutputList

![Spreadsheet OutputList](SpreadsheetOutputList/SpreadsheetOutputList.png)

(ComfyUI workflow inkludert)

Oppretter flere OutputList fra et regneark (`.csv .tsv .ods .xlsx .xls`).
Du kan bruke `Load any File`-noden for å laste inn en fil i base64-koding.
Intern bruker *pandas* [read_excel](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html) og [read_csv](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html) for å laste inn regnearkfiler.
Alle listene bruker `is_output_list=True` (indikert med symbolet `𝌠`) og vil bli behandlet sekvensielt av tilsvarende noder.

### Innputter

| Navn | Type | Beskrivelse |
| --- | --- | --- |
| `rows_and_cols` | `STRING` | Indekser og navn på rader og kolonner i regnearket. Merk at i regneark starter rader på 1, kolonner starter på A, mens OutputList er 0-basert (i `select-nth`). |
| `header_rows` | `INT` | Ignorer de første x radene i listen. Brukes bare hvis du spesifiserer en kolonne i `rows_and_cols`. |
| `header_cols` | `INT` | Ignorer de første x kolonnene i listen. Brukes bare hvis du spesifiserer en rad i `rows_and_cols`. |
| `select_nth` | `INT` | Velg bare den nth oppføringen (0-basert). Nyttig i kombinasjon med mønsteret `PrimitiveInt+control_after_generate=increment`. |
| `string_or_base64` | `STRING` | CSV/TSV-streng eller regnearkfil i base64 (for `.ods .xlsx .xls`). Bruk `Load Any File`-noden for å laste inn en fil som base64. |

### Utputter

| Navn | Type | Beskrivelse |
| --- | --- | --- |
| `list_a` | `STRING 𝌠` |  |
| `list_b` | `STRING 𝌠` |  |
| `list_c` | `STRING 𝌠` |  |
| `list_d` | `STRING 𝌠` |  |
| `count` | `INT` | Antall elementer i den lengste listen. |

