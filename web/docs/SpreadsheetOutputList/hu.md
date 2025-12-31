## Spreadsheet OutputList

![Spreadsheet OutputList](SpreadsheetOutputList/SpreadsheetOutputList.png)

(ComfyUI workflow mellékletként)

Több OutputList-et hoz létre egy táblázatból (`.csv .tsv .ods .xlsx .xls`).
Használhatod a `Load any File` csomópontot a fájl base64-kódolásban való betöltéséhez.
Belsőleg a *pandas* [read_excel](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html) és [read_csv](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html) függvényeket használja a táblázatfájlok betöltéséhez.
Minden lista használja a `is_output_list=True` (a `𝌠` szimbólummal jelölt) és szekvenciálisan feldolgozásra kerülnek a megfelelő csomópontokban.

### Bemenetek

| Név | Típus | Leírás |
| --- | --- | --- |
| `rows_and_cols` | `STRING` | A sorok és oszlopok indexei és nevei a táblázatban. Megjegyzés: a táblázatokban a sorok 1-től kezdődnek, az oszlopok A-tól kezdődnek, míg az OutputListek 0-alapúak (a `select-nth`-ben). |
| `header_rows` | `INT` | Az első x sor figyelmen kívül hagyása a listában. Csak akkor használt, ha megadod az oszlopot a `rows_and_cols`-ban. |
| `header_cols` | `INT` | Az első x oszlop figyelmen kívül hagyása a listában. Csak akkor használt, ha megadod a sort a `rows_and_cols`-ban. |
| `select_nth` | `INT` | Csak az nth bejegyzés kiválasztása (0-alapú). Hasznos a `PrimitiveInt+control_after_generate=increment` minta kombinációjában. |
| `string_or_base64` | `STRING` | CSV/TSV sztring vagy táblázatfájl base64-kódolva (a `.ods .xlsx .xls` fájlokhoz). Használd a `Load Any File` csomópontot a fájl base64-kódolásban való betöltéséhez. |

### Kimenetek

| Név | Típus | Leírás |
| --- | --- | --- |
| `list_a` | `STRING 𝌠` |  |
| `list_b` | `STRING 𝌠` |  |
| `list_c` | `STRING 𝌠` |  |
| `list_d` | `STRING 𝌠` |  |
| `count` | `INT` | A leghosszabb lista elemeinek száma. |

