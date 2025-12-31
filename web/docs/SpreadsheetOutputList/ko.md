## Spreadsheet OutputList

![Spreadsheet OutputList](SpreadsheetOutputList/SpreadsheetOutputList.png)

(ComfyUI workflow 포함)

스프레드시트 (`.csv .tsv .ods .xlsx .xls`)에서 여러 OutputList를 생성합니다.
`Load any File` 노드를 사용하여 base64 인코딩으로 파일을 로드할 수 있습니다.
내부적으로 *pandas* [read_excel](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html)과 [read_csv](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html)를 사용하여 스프레드시트 파일을 로드합니다.
모든 목록은 `is_output_list=True` (기호 `𝌠`으로 표시됨)를 사용하며, 해당 노드에 의해 순차적으로 처리됩니다.

### 입력

| 이름 | 유형 | 설명 |
| --- | --- | --- |
| `rows_and_cols` | `STRING` | 스프레드시트의 행과 열의 인덱스와 이름입니다. 스프레드시트에서 행은 1부터 시작하고 열은 A부터 시작하지만, OutputList는 0부터 시작한다는 점에 주의하세요 (`select-nth`에서). |
| `header_rows` | `INT` | 목록에서 첫 번째 x 행을 무시합니다. `rows_and_cols`에 열을 지정한 경우에만 사용됩니다. |
| `header_cols` | `INT` | 목록에서 첫 번째 x 열을 무시합니다. `rows_and_cols`에 행을 지정한 경우에만 사용됩니다. |
| `select_nth` | `INT` | n번째 항목만 선택합니다 (0부터 시작). `PrimitiveInt+control_after_generate=increment` 패턴과 함께 사용할 때 유용합니다. |
| `string_or_base64` | `STRING` | CSV/TSV 문자열 또는 base64로 인코딩된 스프레드시트 파일 (`.ods .xlsx .xls`용). 파일을 base64로 로드하려면 `Load Any File` 노드를 사용하세요. |

### 출력

| 이름 | 유형 | 설명 |
| --- | --- | --- |
| `list_a` | `STRING 𝌠` |  |
| `list_b` | `STRING 𝌠` |  |
| `list_c` | `STRING 𝌠` |  |
| `list_d` | `STRING 𝌠` |  |
| `count` | `INT` | 가장 긴 목록의 항목 수입니다. |

