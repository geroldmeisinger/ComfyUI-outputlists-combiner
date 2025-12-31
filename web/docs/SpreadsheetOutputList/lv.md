## Spreadsheet OutputList

![Spreadsheet OutputList](SpreadsheetOutputList/SpreadsheetOutputList.png)

(ComfyUI workflow iekļauts)

Izveido vairākus OutputLists no izklājlapas (`.csv .tsv .ods .xlsx .xls`).
Varat izmantot `Load any File` mezglu, lai ielādētu failu base64-kodējumā.
Iekšēji izmanto *pandas* [read_excel](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html) un [read_csv](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html), lai ielādētu izklājlapu failus.
Visi saraksti izmanto `is_output_list=True` (atspoguļots ar simbolu `𝌠`) un tiks apstrādāti secīgi ar atbilstošiem mezgliem.

### Ievades

| Nosaukums | Tips | Apraksts |
| --- | --- | --- |
| `rows_and_cols` | `STRING` | Rindu un kolonnu indeksi un nosaukumi izklājlapā. Ņemiet vērā, ka izklājlapās rindas sākas ar 1, kolonnas sākas ar A, savukārt OutputLists ir 0-pamata (pie `select-nth`). |
| `header_rows` | `INT` | Ignorēt pirmās x rindas sarakstā. Tieši izmantots, ja norādījāt kolonnu `rows_and_cols`. |
| `header_cols` | `INT` | Ignorēt pirmās x kolonnas sarakstā. Tieši izmantots, ja norādījāt rindu `rows_and_cols`. |
| `select_nth` | `INT` | Izvēlēties tikai nth ierakstu (0-pamata). Noderīgi kombinācijā ar `PrimitiveInt+control_after_generate=increment` paraugu. |
| `string_or_base64` | `STRING` | CSV/TSV virkne vai izklājlapas fails base64 (priekš `.ods .xlsx .xls`). Izmantojiet `Load Any File` mezglu, lai ielādētu failu kā base64. |

### Izvades

| Nosaukums | Tips | Apraksts |
| --- | --- | --- |
| `list_a` | `STRING 𝌠` |  |
| `list_b` | `STRING 𝌠` |  |
| `list_c` | `STRING 𝌠` |  |
| `list_d` | `STRING 𝌠` |  |
| `count` | `INT` | Elementu skaits garākajā sarakstā. |

