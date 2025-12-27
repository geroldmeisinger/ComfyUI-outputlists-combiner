<!-- This file was auto-translated with a local LLM and last updated on 2025-12-27. -->
## קומבינציות של מערך ייצוא

![קומבינציות של מערך ייצוא](CombineOutputLists/CombineOutputLists.png)

(מיפוי של שילוב של ComfyUI)

מקבל עד 4 מערך ייצוא ומייצר כל קומבינציה מהם.

דוגמה: `[1, 2, 3] x ["A", "B"] = [(1, "A"), (1, "B"), (2, "A"), (2, "B"), (3, "A"), (3, "B")]`

`unzip_a` .. `unzip_d` משתמשים ב- `is_output_list=True` (הסמל `𝌠`) ויראו בדוק על ידי נקודות מתאימות.

כל המערך אופציונליים, ומערך ריק ייחל.

במצב טכני הוא מחשב את *המכפלה הקרטזית* ומייצר כל קומבינציה, מפריד את כל הרכיבים (`unzip`), בעוד שמערך ריק יוחלף ב- `None` וירדו `None` על הפלט המתאים.

דוגמה: `[1, 2] x [] x ["A", "B"] x [] = [(1, None, "A", None), (1, None, "B", None), (2, None, "A", None), (2, None, "B", None)]`

### קלט

| שם | סוג | תיאור |
| --- | --- | --- |
| `list_a` | `*` | (אופציונלי) |
| `list_b` | `*` | (אופציונלי) |
| `list_c` | `*` | (אופציונלי) |
| `list_d` | `*` | (אופציונלי) |

### פלט

| שם | סוג | תיאור |
| --- | --- | --- |
| `unzip_a` | `* 𝌠` | ערך של הקומבינציות המתייחסות ל- `list_a`. |
| `unzip_b` | `* 𝌠` | ערך של הקומבינציות המתייחסות ל- `list_b`. |
| `unzip_c` | `* 𝌠` | ערך של הקומבינציות המתייחסות ל- `list_c`. |
| `unzip_d` | `* 𝌠` | ערך של הקומבינציות המתייחסות ל- `list_d`. |
| `index` | `INT 𝌠` | טווח 0..count שמתאים כמפתח. |
| `count` | `INT` | המספר הכולל של הקומבינציות. |

