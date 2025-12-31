## Spreadsheet OutputList

![Spreadsheet OutputList](SpreadsheetOutputList/SpreadsheetOutputList.png)

(ComfyUI workflow san áireamh)

Cruthaíonn OutputLists iolracha ó spreidsheet (`.csv .tsv .ods .xlsx .xls`).
Is féidir leat an nód `Load any File` a úsáid chun comhad a lódáil i base64-encoding.
Úsáideann *pandas* [read_excel](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html) agus [read_csv](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html) de réir teachtaireachta chun comhaid spreidsheet a lódáil.
Úsáideann gach liosta(s) `is_output_list=True` (sonraithe ag an t-síneadh `𝌠`) agus déanfar iad a phróiseáil go sequential trí na nódanna comhfhreagracha.

### Ionchuir

| Ainm | Cineál | Cur Síos |
| --- | --- | --- |
| `rows_and_cols` | `STRING` | Indicéid agus ainmneacha na n-raelacha agus colún i spreidsheet. Tabhair faoi deara go dtíonn raelacha spreidsheet ag 1, dtíonn colúin ag A, agus mar sin is 0-based OutputLists (i `select-nth`). |
| `header_rows` | `INT` | Déan neamhshuim ar na rialacha tosaigh x sa liosta. Úsáidtear ach má shonraíonn tú colún i `rows_and_cols`. |
| `header_cols` | `INT` | Déan neamhshuim ar na colúin tosaigh x sa liosta. Úsáidtear ach má shonraíonn tú rael i `rows_and_cols`. |
| `select_nth` | `INT` | Déan roghnú ach an níos ceann (0-based). Feidhmíochtach i gcomhbháil leis an patrún `PrimitiveInt+control_after_generate=increment`. |
| `string_or_base64` | `STRING` | String CSV/TSV nó comhad spreidsheet i base64 (le haghaidh `.ods .xlsx .xls`). Úsáid nód `Load Any File` chun comhad a lódáil mar base64. |

### Aschuir

| Ainm | Cineál | Cur Síos |
| --- | --- | --- |
| `list_a` | `STRING 𝌠` |  |
| `list_b` | `STRING 𝌠` |  |
| `list_c` | `STRING 𝌠` |  |
| `list_d` | `STRING 𝌠` |  |
| `count` | `INT` | An t-uimhir de níomhais sa liosta is faide. |

