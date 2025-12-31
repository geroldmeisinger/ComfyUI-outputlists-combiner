## Spreadsheet OutputList

![Spreadsheet OutputList](SpreadsheetOutputList/SpreadsheetOutputList.png)

(Workflow ComfyUI inclus)

Crée plusieurs OutputLists à partir d'une feuille de calcul (`.csv .tsv .ods .xlsx .xls`).
Vous pouvez utiliser le nœud `Load any File` pour charger un fichier en codage base64.
Utilise interne *pandas* [read_excel](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html) et [read_csv](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html) pour charger les fichiers de feuilles de calcul.
Toutes les listes utilisent `is_output_list=True` (indiqué par le symbole `𝌠`) et seront traitées séquentiellement par les nœuds correspondants.

### Entrées

| Nom | Type | Description |
| --- | --- | --- |
| `rows_and_cols` | `STRING` | Indices et noms des lignes et colonnes dans la feuille de calcul. Notez que dans les feuilles de calcul, les lignes commencent à 1, les colonnes commencent à A, tandis que les OutputLists sont basées sur 0 (dans `select-nth`). |
| `header_rows` | `INT` | Ignorer les x premières lignes dans la liste. Uniquement utilisé si vous spécifiez une colonne dans `rows_and_cols`. |
| `header_cols` | `INT` | Ignorer les x premières colonnes dans la liste. Uniquement utilisé si vous spécifiez une ligne dans `rows_and_cols`. |
| `select_nth` | `INT` | Sélectionner uniquement la nième entrée (basée sur 0). Utile en combinaison avec le motif `PrimitiveInt+control_after_generate=increment`. |
| `string_or_base64` | `STRING` | Chaîne CSV/TSV ou fichier de feuille de calcul en base64 (pour `.ods .xlsx .xls`). Utilisez le nœud `Load Any File` pour charger un fichier en base64. |

### Sorties

| Nom | Type | Description |
| --- | --- | --- |
| `list_a` | `STRING 𝌠` |  |
| `list_b` | `STRING 𝌠` |  |
| `list_c` | `STRING 𝌠` |  |
| `list_d` | `STRING 𝌠` |  |
| `count` | `INT` | Nombre d'éléments dans la liste la plus longue. |

