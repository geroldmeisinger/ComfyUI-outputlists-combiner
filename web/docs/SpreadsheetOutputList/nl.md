## Spreadsheet OutputList

![Spreadsheet OutputList](SpreadsheetOutputList/SpreadsheetOutputList.png)

(ComfyUI workflow inclusief)

Maakt meerdere OutputLists aan vanuit een spreadsheet (`.csv .tsv .ods .xlsx .xls`).
Je kunt de `Load any File` node gebruiken om een bestand te laden in base64-codering.
Intern gebruikt het *pandas* [read_excel](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html) en [read_csv](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html) om spreadsheetbestanden te laden.
Alle lijsten gebruiken `is_output_list=True` (aangegeven door het symbool `𝌠`) en worden sequentieel verwerkt door overeenkomstige nodes.

### Invoer

| Naam | Type | Beschrijving |
| --- | --- | --- |
| `rows_and_cols` | `STRING` | Indices en namen van rijen en kolommen in de spreadsheet. Let op dat in spreadsheets rijen beginnen bij 1, kolommen bij A, terwijl OutputLists 0-gebaseerd zijn (in `select-nth`). |
| `header_rows` | `INT` | Negeer de eerste x rijen in de lijst. Alleen gebruikt als je een kolom opgeeft in `rows_and_cols`. |
| `header_cols` | `INT` | Negeer de eerste x kolommen in de lijst. Alleen gebruikt als je een rij opgeeft in `rows_and_cols`. |
| `select_nth` | `INT` | Selecteer alleen de nth vermelding (0-gebaseerd). Nuttig in combinatie met het `PrimitiveInt+control_after_generate=increment` patroon. |
| `string_or_base64` | `STRING` | CSV/TSV string of spreadsheetbestand in base64 (voor `.ods .xlsx .xls`). Gebruik de `Load Any File` node om een bestand als base64 te laden. |

### Uitvoer

| Naam | Type | Beschrijving |
| --- | --- | --- |
| `list_a` | `STRING 𝌠` |  |
| `list_b` | `STRING 𝌠` |  |
| `list_c` | `STRING 𝌠` |  |
| `list_d` | `STRING 𝌠` |  |
| `count` | `INT` | Aantal items in de langste lijst. |

