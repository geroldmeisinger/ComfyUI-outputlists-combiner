## Spreadsheet OutputList

![Spreadsheet OutputList](SpreadsheetOutputList/SpreadsheetOutputList.png)

(ComfyUI workflow inclòs)

Crea múltiples OutputLists des d'una fulla de càlcul (`.csv .tsv .ods .xlsx .xls`).
Pots utilitzar el node `Load any File` per carregar un fitxer en codificació base64.
Internament utilitza *pandas* [read_excel](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html) i [read_csv](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html) per carregar fitxers de fulla de càlcul.
Totes les llistes utilitzen `is_output_list=True` (indicat pel símbol `𝌠`) i seran processades seqüencialment per nodes corresponents.

### Entrades

| Nom | Tipus | Descripció |
| --- | --- | --- |
| `rows_and_cols` | `STRING` | Índexs i noms de files i columnes a la fulla de càlcul. Tingues en compte que a les fulla de càlcul les files comencen a 1, les columnes comencen a A, mentre que les OutputLists són basades en 0 (a `select-nth`). |
| `header_rows` | `INT` | Ignora les primeres x files de la llista. Només s'utilitza si especifiques una columna a `rows_and_cols`. |
| `header_cols` | `INT` | Ignora les primeres x columnes de la llista. Només s'utilitza si especifiques una fila a `rows_and_cols`. |
| `select_nth` | `INT` | Només selecciona l'entrada n-èssima (basada en 0). Útil en combinació amb el patró `PrimitiveInt+control_after_generate=increment`. |
| `string_or_base64` | `STRING` | Cadena CSV/TSV o fitxer de fulla de càlcul en base64 (per a `.ods .xlsx .xls`). Utilitza el node `Load Any File` per carregar un fitxer com a base64. |

### Sortides

| Nom | Tipus | Descripció |
| --- | --- | --- |
| `list_a` | `STRING 𝌠` |  |
| `list_b` | `STRING 𝌠` |  |
| `list_c` | `STRING 𝌠` |  |
| `list_d` | `STRING 𝌠` |  |
| `count` | `INT` | Nombre d'elements a la llista més llarga. |

