## Spreadsheet OutputList

![Spreadsheet OutputList](SpreadsheetOutputList/SpreadsheetOutputList.png)

(Dołączono workflow ComfyUI)

Tworzy wiele OutputList z arkusza kalkulacyjnego (`.csv .tsv .ods .xlsx .xls`).
Możesz użyć węzła `Load any File`, aby załadować plik w kodowaniu base64.
Wewnętrznie wykorzystuje *pandas* [read_excel](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html) i [read_csv](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html) do ładowania plików arkuszy kalkulacyjnych.
Wszystkie listy używają `is_output_list=True` (oznaczone symbolem `𝌠`) i będą przetwarzane sekwencyjnie przez odpowiednie węzły.

### Wejścia

| Nazwa | Typ | Opis |
| --- | --- | --- |
| `rows_and_cols` | `STRING` | Indeksy i nazwy wierszy i kolumn w arkuszu kalkulacyjnym. Należy pamiętać, że w arkuszach kalkulacyjnych wiersze zaczynają się od 1, kolumny od A, natomiast OutputList są oparte na indeksach 0 (w `select-nth`). |
| `header_rows` | `INT` | Ignoruje pierwsze x wiersze na liście. Używane tylko wtedy, gdy określisz kolumnę w `rows_and_cols`. |
| `header_cols` | `INT` | Ignoruje pierwsze x kolumny na liście. Używane tylko wtedy, gdy określisz wiersz w `rows_and_cols`. |
| `select_nth` | `INT` | Wybiera tylko n-tą pozycję (oparta na indeksie 0). Przydatne w połączeniu z wzorcem `PrimitiveInt+control_after_generate=increment`. |
| `string_or_base64` | `STRING` | Ciąg znaków CSV/TSV lub plik arkusza kalkulacyjnego w kodowaniu base64 (dla `.ods .xlsx .xls`). Użyj węzła `Load Any File`, aby załadować plik jako base64. |

### Wyjścia

| Nazwa | Typ | Opis |
| --- | --- | --- |
| `list_a` | `STRING 𝌠` |  |
| `list_b` | `STRING 𝌠` |  |
| `list_c` | `STRING 𝌠` |  |
| `list_d` | `STRING 𝌠` |  |
| `count` | `INT` | Liczba elementów w najdłuższej liście. |

