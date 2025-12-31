## Spreadsheet OutputList

![Spreadsheet OutputList](SpreadsheetOutputList/SpreadsheetOutputList.png)

(ComfyUI-työnkulku mukana)

Luo useita OutputListeja laskentataulukosta (`.csv .tsv .ods .xlsx .xls`).
Voit käyttää `Load any File` -solmua lataamaan tiedoston base64-koodauksessa.
Sisäisesti käyttää *pandas* [read_excel](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html) ja [read_csv](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html) lataamaan laskentataulukkotiedostoja.
Kaikki listat käyttävät `is_output_list=True` (merkitty symbolilla `𝌠`) ja ne käsitellään peräkkäin vastaavien solmujen toimesta.

### Syötteet

| Nimi | Tyyppi | Kuvaus |
| --- | --- | --- |
| `rows_and_cols` | `STRING` | Laskentataulukon rivien ja sarakkeiden indeksit ja nimet. Huomaa, että laskentataulukoissa rivit alkavat 1, sarakkeet alkavat A, kun taas OutputListeissa on 0-pohjainen (in `select-nth`). |
| `header_rows` | `INT` | Jätä ensimmäiset x riviä listasta huomiotta. Käytetään vain, jos määrittelet sarakkeen `rows_and_cols`-kentässä. |
| `header_cols` | `INT` | Jätä ensimmäiset x saraketta listasta huomiotta. Käytetään vain, jos määrittelet rivin `rows_and_cols`-kentässä. |
| `select_nth` | `INT` | Valitse vain nth-kirjain (0-pohjainen). Hyödyllinen yhdessä `PrimitiveInt+control_after_generate=increment`-mallin kanssa. |
| `string_or_base64` | `STRING` | CSV/TSV-merkkijono tai laskentataulukko base64-koodattuna (for `.ods .xlsx .xls`). Käytä `Load Any File` -solmua ladataksesi tiedoston base64-muodossa. |

### Tulosteet

| Nimi | Tyyppi | Kuvaus |
| --- | --- | --- |
| `list_a` | `STRING 𝌠` |  |
| `list_b` | `STRING 𝌠` |  |
| `list_c` | `STRING 𝌠` |  |
| `list_d` | `STRING 𝌠` |  |
| `count` | `INT` | Kohteiden määrä pitkimmässä listassa. |

