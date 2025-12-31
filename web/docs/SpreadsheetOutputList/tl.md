## Spreadsheet OutputList

![Spreadsheet OutputList](SpreadsheetOutputList/SpreadsheetOutputList.png)

(ComfyUI workflow ang kasama)

Ginagawa ang mga OutputList mula sa isang spreadsheet (`.csv .tsv .ods .xlsx .xls`).
Maaari mong gamitin ang `Load any File` node para i-load ang isang file na nasa base64-encoding.
Nag-uugnay ng *pandas* [read_excel](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html) at [read_csv](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html) para i-load ang mga file ng spreadsheet.
Lahat ng mga list ay gumagamit ng `is_output_list=True` (na ipinapakita ng simbolo `𝌠`) at ipoproseso nang sequence ng mga corresponding nodes.

### Mga Input

| Pangalan | Uri | Paglalarawan |
| --- | --- | --- |
| `rows_and_cols` | `STRING` | Mga index at pangalan ng mga row at column sa spreadsheet. Tandaan na sa mga spreadsheet ang mga row ay nagsisimula sa 1, ang mga column ay nagsisimula sa A, habang ang OutputLists ay 0-based (sa `select-nth`). |
| `header_rows` | `INT` | Balewalain ang mga unang x row sa list. Gamitin lamang kung ikaw ay tumutukoy sa isang col sa `rows_and_cols`. |
| `header_cols` | `INT` | Balewalain ang mga unang x col sa list. Gamitin lamang kung ikaw ay tumutukoy sa isang row sa `rows_and_cols`. |
| `select_nth` | `INT` | Piliin lamang ang nth entry (0-based). Nakakatulong kapag kasama ang `PrimitiveInt+control_after_generate=increment` pattern. |
| `string_or_base64` | `STRING` | CSV/TSV string o spreadsheet file na nasa base64 (para sa `.ods .xlsx .xls`). Gamitin ang `Load Any File` node para i-load ang file bilang base64. |

### Mga Output

| Pangalan | Uri | Paglalarawan |
| --- | --- | --- |
| `list_a` | `STRING 𝌠` |  |
| `list_b` | `STRING 𝌠` |  |
| `list_c` | `STRING 𝌠` |  |
| `list_d` | `STRING 𝌠` |  |
| `count` | `INT` | Bilang ng mga item sa pinakamahabang list. |

