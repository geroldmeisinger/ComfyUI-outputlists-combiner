## Spreadsheet OutputList

![Spreadsheet OutputList](SpreadsheetOutputList/SpreadsheetOutputList.png)

(ComfyUI workflow zahrnut)

Vytvoří více OutputListů z tabulky (`.csv .tsv .ods .xlsx .xls`).
Můžete použít uzel `Load any File` pro načtení souboru v base64-kódování.
Interně používá *pandas* [read_excel](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html) a [read_csv](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html) pro načítání souborů tabulek.
Všechny seznamy používají `is_output_list=True` (označeno symbolem `𝌠`) a budou zpracovány sekvenčně odpovídajícími uzly.

### Vstupy

| Název | Typ | Popis |
| --- | --- | --- |
| `rows_and_cols` | `ŘETĚZEC` | Indexy a názvy řádků a sloupců v tabulce. Všimněte si, že v tabulkách řádky začínají na 1, sloupce začínají na A, zatímco OutputListy jsou 0-založené (v `select-nth`). |
| `header_rows` | `CELÉ ČÍSLO` | Ignorovat prvních x řádků v seznamu. Používá se pouze pokud zadáte sloupec v `rows_and_cols`. |
| `header_cols` | `CELÉ ČÍSLO` | Ignorovat prvních x sloupců v seznamu. Používá se pouze pokud zadáte řádek v `rows_and_cols`. |
| `select_nth` | `CELÉ ČÍSLO` | Vybrat pouze n-tou položku (0-založené). Užitečné ve spojení s vzorem `PrimitiveInt+control_after_generate=increment`. |
| `string_or_base64` | `ŘETĚZEC` | Řetězec CSV/TSV nebo soubor tabulky v base64 (pro `.ods .xlsx .xls`). Použijte uzel `Load Any File` pro načtení souboru jako base64. |

### Výstupy

| Název | Typ | Popis |
| --- | --- | --- |
| `list_a` | `ŘETĚZEC 𝌠` |  |
| `list_b` | `ŘETĚZEC 𝌠` |  |
| `list_c` | `ŘETĚZEC 𝌠` |  |
| `list_d` | `ŘETĚZEC 𝌠` |  |
| `count` | `CELÉ ČÍSLO` | Počet položek v nejdelším seznamu. |

