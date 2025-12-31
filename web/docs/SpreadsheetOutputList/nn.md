## Spreadsheet OutputList

![Spreadsheet OutputList](SpreadsheetOutputList/SpreadsheetOutputList.png)

(ComfyUI workflow inkludert)

Lagar fleire OutputList frå eit regneark (`.csv .tsv .ods .xlsx .xls`).
Du kan bruke `Load any File`-noden for å lasta inn ei fil i base64-koding.
Intern brukar *pandas* [read_excel](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html) og [read_csv](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html) for å lasta inn regnearkfiler.
Alle listene brukar `is_output_list=True` (indikert av symbolet `𝌠`) og vil bli handsama sekvensielt av tilhøyrande noder.

### Inndata

| Namn | Type | Skildring |
| --- | --- | --- |
| `rows_and_cols` | `STRING` | Indekser og namn på rader og kolonnar i regnearket. Merk at i regneark startar rader på 1, kolonnar startar på A, medan OutputList er 0-basert (i `select-nth`). |
| `header_rows` | `INT` | Ignorer dei første x radene i lista. Berre brukt dersom du oppgjev ein kolonne i `rows_and_cols`. |
| `header_cols` | `INT` | Ignorer dei første x kolonnene i lista. Berre brukt dersom du oppgjev ein rad i `rows_and_cols`. |
| `select_nth` | `INT` | Vel berre den nth oppføringa (0-basert). Nyttig i kombinasjon med mønsteret `PrimitiveInt+control_after_generate=increment`. |
| `string_or_base64` | `STRING` | CSV/TSV-streng eller regnearkfil i base64 (for `.ods .xlsx .xls`). Bruk `Load Any File`-noden for å lasta inn ei fil som base64. |

### Utdata

| Namn | Type | Skildring |
| --- | --- | --- |
| `list_a` | `STRING 𝌠` |  |
| `list_b` | `STRING 𝌠` |  |
| `list_c` | `STRING 𝌠` |  |
| `list_d` | `STRING 𝌠` |  |
| `count` | `INT` | Tal på element i den lengste lista. |

