## שילובים של OutputLists

![OutputLists Combinations](CombineOutputLists/CombineOutputLists.png)

(הזרמת ComfyUI מצורפת)

מקבל עד 4 OutputLists ומייצר את כל השילובים האפשריים.

דוגמה: `[1, 2, 3] x ["A", "B"] = [(1, "A"), (1, "B"), (2, "A"), (2, "B"), (3, "A"), (3, "B")]`

`unzip_a` .. `unzip_d` משתמשים ב-`is_output_list=True` (מסומנים על ידי הסמל `𝌠`) ומעובדים ברצף על ידי צמתים מתאימים.

כל הרשימות אופציונליות והרשימות הריקות יהתעלמו מהן.

במונחים טכניים, המחשב את *המכפלה קרטזית* ופלט כל שילוב מפוצל לרכיביו (`unzip`), כאשר רשימות ריקות יוחלפו ביחידות של `None` ויתנו `None` על הפלט המתאים.

דוגמה: `[1, 2] x [] x ["A", "B"] x [] = [(1, None, "A", None), (1, None, "B", None), (2, None, "A", None), (2, None, "B", None)]`

### קלטים

| שם | סוג | תיאור |
| --- | --- | --- |
| `list_a` | `*` | (אופציונלי) |
| `list_b` | `*` | (אופציונלי) |
| `list_c` | `*` | (אופציונלי) |
| `list_d` | `*` | (אופציונלי) |

### פלטים

| שם | סוג | תיאור |
| --- | --- | --- |
| `unzip_a` | `* 𝌠` | ערך של השילובים שמתאימים ל-`list_a`. |
| `unzip_b` | `* 𝌠` | ערך של השילובים שמתאימים ל-`list_b`. |
| `unzip_c` | `* 𝌠` | ערך של השילובים שמתאימים ל-`list_c`. |
| `unzip_d` | `* 𝌠` | ערך של השילובים שמתאימים ל-`list_d`. |
| `index` | `INT 𝌠` | טווח של 0..count שיכולה לשמש כאינדקס. |
| `count` | `INT` | מספר כולל של שילובים. |

