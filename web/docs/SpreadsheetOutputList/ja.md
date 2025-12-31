## Spreadsheet OutputList

![Spreadsheet OutputList](SpreadsheetOutputList/SpreadsheetOutputList.png)

(ComfyUI workflowが含まれます)

スプレッドシート（`.csv .tsv .ods .xlsx .xls`）から複数のOutputListを作成します。
`Load any File` ノードを使用してbase64エンコーディングでファイルをロードできます。
内部的には *pandas* [read_excel](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html) と [read_csv](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html) を使用してスプレッドシートファイルをロードします。
すべてのリストは `is_output_list=True` (記号 `𝌠` で示されます) を使用し、対応するノードによって順次処理されます。

### 入力

| 名前 | タイプ | 説明 |
| --- | --- | --- |
| `rows_and_cols` | `STRING` | スプレッドシートの行と列のインデックスと名前。スプレッドシートでは行は1から始まり、列はAから始まる一方、OutputListは0ベース（`select-nth`で）です。 |
| `header_rows` | `INT` | リストの最初のx行を無視します。`rows_and_cols` で列を指定した場合のみ使用されます。 |
| `header_cols` | `INT` | リストの最初のx列を無視します。`rows_and_cols` で行を指定した場合のみ使用されます。 |
| `select_nth` | `INT` | n番目のエントリのみを選択（0ベース）。`PrimitiveInt+control_after_generate=increment` パターンと組み合わせて便利です。 |
| `string_or_base64` | `STRING` | CSV/TSV文字列またはbase64のスプレッドシートファイル（`.ods .xlsx .xls`用）。ファイルをbase64としてロードするには `Load Any File` ノードを使用してください。 |

### 出力

| 名前 | タイプ | 説明 |
| --- | --- | --- |
| `list_a` | `STRING 𝌠` |  |
| `list_b` | `STRING 𝌠` |  |
| `list_c` | `STRING 𝌠` |  |
| `list_d` | `STRING 𝌠` |  |
| `count` | `INT` | 最も長いリストのアイテム数。 |

