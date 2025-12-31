## פלט רשימה טבלאית

![Spreadsheet OutputList](SpreadsheetOutputList/SpreadsheetOutputList.png)

(הזרימה ב-ComfyUI נכללת)

יוצר רשימות פלט מרובות מטבלה (`.csv .tsv .ods .xlsx .xls`).
אתה יכול להשתמש בצומת `Load any File` כדי לטעון קובץ בקידוד base64.
בפנימיות משתמש ב-*pandas* [read_excel](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html) ו-[read_csv](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html) כדי לטעון קבצי טבלה.
כל הרשימות משתמשות ב-`is_output_list=True` (מסומן בסמל `𝌠`) ויהיו מעובדים לפי סדר על ידי צמתים מתאימים.

### קלטים

| שם | סוג | תיאור |
| --- | --- | --- |
| `rows_and_cols` | `STRING` | אינדקסים ושמות של שורות ועמודות בטבלה. שים לב שבטבלאות שורות מתחילות ב-1, עמודות מתחילות ב-A, בעוד שרשימות פלט הן 0-מבוססות (ב-`select-nth`). |
| `header_rows` | `INT` | התעלם מהשורות הראשונות x ברשימה. משמש רק אם אתה מציין עמודה ב-`rows_and_cols`. |
| `header_cols` | `INT` | התעלם מהעמודות הראשונות x ברשימה. משמש רק אם אתה מציין שורה ב-`rows_and_cols`. |
| `select_nth` | `INT` | בחר רק את הרשומה ה-n (מבוססת 0). שימושי בשילוב עם דפוס `PrimitiveInt+control_after_generate=increment`. |
| `string_or_base64` | `STRING` | מחרוזת CSV/TSV או קובץ טבלה ב-base64 (ל-`.ods .xlsx .xls`). השתמש בצומת `Load Any File` כדי לטעון קובץ כ-base64. |

### פלטים

| שם | סוג | תיאור |
| --- | --- | --- |
| `list_a` | `STRING 𝌠` |  |
| `list_b` | `STRING 𝌠` |  |
| `list_c` | `STRING 𝌠` |  |
| `list_d` | `STRING 𝌠` |  |
| `count` | `INT` | מספר הפריטים ברשימה הארוכה ביותר. |

