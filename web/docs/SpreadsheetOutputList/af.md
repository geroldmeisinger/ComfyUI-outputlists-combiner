## Spreadsheel OutputList

![Spreadsheel OutputList](SpreadsheetOutputList/SpreadsheetOutputList.png)

(ComfyUI workflow ingesluit)

Skep verskeie OutputLists vanaf 'n spreedblad (`.csv .tsv .ods .xlsx .xls`).
Jy kan die `Laai enige Lêer` node gebruik om 'n lêer in base64-kodering te laai.
Gebruik intern *pandas* [read_excel](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html) en [read_csv](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html) om spreedblad lêers te laai.
Alle lyste gebruik(s) `is_output_list=True` (aangedui deur die simbool `𝌠`) en sal sekwensieel deur ooreenstemmende nodes verwerk word.

### Invoere

| Naam | Tipe | Beskrywing |
| --- | --- | --- |
| `rows_and_cols` | `STRING` | Indicies en name van rye en kolomme in die spreedblad. Merk op dat in spreedblad rye begin by 1, kolomme begin by A, terwyl OutputLists 0-gebaseer is (in `select-nth`). |
| `header_rows` | `INT` | Ignoreer die eerste x rye in die lys. Net gebruik as jy 'n kolom spesifiseer in `rows_and_cols`. |
| `header_cols` | `INT` | Ignoreer die eerste x kolomme in die lys. Net gebruik as jy 'n ry spesifiseer in `rows_and_cols`. |
| `select_nth` | `INT` | Selekteer net die nth inskrywing (0-gebaseer). Nuttig in kombinasie met die `PrimitiveInt+control_after_generate=increment` patroon. |
| `string_or_base64` | `STRING` | CSV/TSV string of spreedblad lêer in base64 (vir `.ods .xlsx .xls`). Gebruik `Laai enige Lêer` node om 'n lêer as base64 te laai. |

### Uitvoere

| Naam | Tipe | Beskrywing |
| --- | --- | --- |
| `list_a` | `STRING 𝌠` |  |
| `list_b` | `STRING 𝌠` |  |
| `list_c` | `STRING 𝌠` |  |
| `list_d` | `STRING 𝌠` |  |
| `count` | `INT` | Aantal items in die langste lys. |

