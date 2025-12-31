## Spreadsheet OutputList

![Spreadsheet OutputList](SpreadsheetOutputList/SpreadsheetOutputList.png)

(ComfyUI workflow inkluderad)

Skapar flera OutputList från ett kalkylblad (`.csv .tsv .ods .xlsx .xls`).
Du kan använda `Load any File`-noden för att ladda en fil i base64-kodning.
Använder internt *pandas* [read_excel](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html) och [read_csv](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html) för att ladda kalkylbladsfiler.
Alla listor använder `is_output_list=True` (indikerat av symbolen `𝌠`) och kommer att bearbetas sekventiellt av motsvarande noder.

### Ingångar

| Namn | Typ | Beskrivning |
| --- | --- | --- |
| `rows_and_cols` | `STRING` | Index och namn på rader och kolumner i kalkylbladet. Observera att rader i kalkylblad börjar vid 1, kolumner börjar vid A, medan OutputList är 0-baserade (i `select-nth`). |
| `header_rows` | `INT` | Ignorera de första x raderna i listan. Används endast om du anger en kolumn i `rows_and_cols`. |
| `header_cols` | `INT` | Ignorera de första x kolumnerna i listan. Används endast om du anger en rad i `rows_and_cols`. |
| `select_nth` | `INT` | Välj endast den n:te posten (0-baserad). Användbart i kombination med mönstret `PrimitiveInt+control_after_generate=increment`. |
| `string_or_base64` | `STRING` | CSV/TSV-sträng eller kalkylbladsfil i base64 (för `.ods .xlsx .xls`). Använd `Load Any File`-noden för att ladda en fil som base64. |

### Utgångar

| Namn | Typ | Beskrivning |
| --- | --- | --- |
| `list_a` | `STRING 𝌠` |  |
| `list_b` | `STRING 𝌠` |  |
| `list_c` | `STRING 𝌠` |  |
| `list_d` | `STRING 𝌠` |  |
| `count` | `INT` | Antal objekt i den längsta listan. |

