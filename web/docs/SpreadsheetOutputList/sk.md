## Výstupný zoznam tabuľky

![Výstupný zoznam tabuľky](SpreadsheetOutputList/SpreadsheetOutputList.png)

(ComfyUI workflow je zahrnutý)

Vytvorí viacero výstupných zoznamov z tabuľky (`.csv .tsv .ods .xlsx .xls`).
Môžete použiť uzol `Load any File` na načítanie súboru v kódovaní base64.
Interné použitie *pandas* [read_excel](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html) a [read_csv](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html) na načítanie súborov tabuliek.
Všetky zoznamy používajú `is_output_list=True` (označené symbolom `𝌠`) a budú spracované postupne príslušnými uzlami.

### Vstupy

| Názov | Typ | Popis |
| --- | --- | --- |
| `rows_and_cols` | `STRING` | Indexy a názvy riadkov a stĺpcov v tabuľke. Všimnite si, že v tabuľkách riadky začínajú od 1, stĺpce začínajú od A, zatiaľ čo výstupné zoznamy sú 0-založené (v `select-nth`). |
| `header_rows` | `INT` | Ignorovať prvých x riadkov v zozname. Používa sa iba ak zadefinujete stĺpec v `rows_and_cols`. |
| `header_cols` | `INT` | Ignorovať prvých x stĺpcov v zozname. Používa sa iba ak zadefinujete riadok v `rows_and_cols`. |
| `select_nth` | `INT` | Vybrať iba n-tý vstup (0-založený). Užitočné v kombinácii s vzorom `PrimitiveInt+control_after_generate=increment`. |
| `string_or_base64` | `STRING` | CSV/TSV reťazec alebo súbor tabuľky v base64 (pre `.ods .xlsx .xls`). Použite uzol `Load Any File` na načítanie súboru ako base64. |

### Výstupy

| Názov | Typ | Popis |
| --- | --- | --- |
| `list_a` | `STRING 𝌠` |  |
| `list_b` | `STRING 𝌠` |  |
| `list_c` | `STRING 𝌠` |  |
| `list_d` | `STRING 𝌠` |  |
| `count` | `INT` | Počet položiek v najdlhšom zozname. |

