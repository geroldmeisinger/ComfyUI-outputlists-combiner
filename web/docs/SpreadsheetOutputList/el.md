## Spreadsheet OutputList

![Spreadsheet OutputList](SpreadsheetOutputList/SpreadsheetOutputList.png)

(Συμπεριλαμβανόμενη η ComfyUI workflow)

Δημιουργεί πολλαπλά OutputList από ένα φύλλο εργασίας (`.csv .tsv .ods .xlsx .xls`).
Μπορείτε να χρησιμοποιήσετε τον κόμβο `Load any File` για να φορτώσετε ένα αρχείο σε κωδικοποίηση base64.
Εσωτερικά χρησιμοποιεί το *pandas* [read_excel](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html) και [read_csv](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html) για τη φόρτωση αρχείων φύλλων εργασίας.
Όλες οι λίστες χρησιμοποιούν `is_output_list=True` (δείχνει με το σύμβολο `𝌠`) και θα επεξεργαστούν σε ακολουθία από τους αντίστοιχους κόμβους.

### Εισόδοι

| Όνομα | Τύπος | Περιγραφή |
| --- | --- | --- |
| `rows_and_cols` | `STRING` | Οι δείκτες και οι ονομασίες των γραμμών και στηλών στο φύλλο εργασίας. Σημειώστε ότι στα φύλλα εργασίας οι γραμμές ξεκινούν από 1, οι στήλες από το A, ενώ τα OutputList είναι βασισμένα στο 0 (στο `select-nth`). |
| `header_rows` | `INT` | Αγνοήστε τις πρώτες x γραμμές στη λίστα. Χρησιμοποιείται μόνο αν καθορίσετε μια στήλη στο `rows_and_cols`. |
| `header_cols` | `INT` | Αγνοήστε τις πρώτες x στήλες στη λίστα. Χρησιμοποιείται μόνο αν καθορίσετε μια γραμμή στο `rows_and_cols`. |
| `select_nth` | `INT` | Επιλέξτε μόνο την nth καταχώρηση (βασισμένη στο 0). Χρήσιμο σε συνδυασμό με το πρότυπο `PrimitiveInt+control_after_generate=increment`. |
| `string_or_base64` | `STRING` | Συμβολοσειρά CSV/TSV ή αρχείο φύλλου εργασίας σε base64 (για `.ods .xlsx .xls`). Χρησιμοποιήστε τον κόμβο `Load Any File` για να φορτώσετε ένα αρχείο ως base64. |

### Έξοδοι

| Όνομα | Τύπος | Περιγραφή |
| --- | --- | --- |
| `list_a` | `STRING 𝌠` |  |
| `list_b` | `STRING 𝌠` |  |
| `list_c` | `STRING 𝌠` |  |
| `list_d` | `STRING 𝌠` |  |
| `count` | `INT` | Αριθμός στοιχείων στη μεγαλύτερη λίστα. |

