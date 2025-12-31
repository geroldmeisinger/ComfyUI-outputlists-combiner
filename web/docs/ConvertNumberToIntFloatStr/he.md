## המרה למספר שלם, מספר עשרוני, מחרוזת

![Convert To Int Float Str](ConvertNumberToIntFloatStr/ConvertNumberToIntFloatStr.png)

(הזרימה ב-ComfyUI נכללת)

ממיר כל דבר דומה למספר ל-`INT` `FLOAT` `STRING`.
משתמש ב-`nums_from_string.get_nums` פנימית, אשר מתנהגת בצורה מאוד פורשת במספרים שהיא מקבלת. כל דבר החל ממספרים שלמים אמיתיים, מספרים עשרוניים אמיתיים, מספרים שלמים או עשרוניים כמחרוזות, מחרוזות שמכילות מספרים מרובים עם פסיקים לאלפים.
שימוש במחרוזת `123;234;345` כדי ליצור במהירות רשימה של מספרים. אל תשתמש בפסיקים כמפרידים כיוון שהם עלולים להיחשב כפסיקי אלפים.
`int`, `float` ו-`string` משתמשים ב-`is_output_list=True` (מסומן בסמל `𝌠`) ויהיו מעובדים לפי סדר על ידי צמתים מתאימים.

### קלטים

| שם | סוג | תיאור |
| --- | --- | --- |
| `any` | `*` | כל מה שיכולה להיחשב כמחרוזת עם מספרים ניתנים לניתוח |

### פלטים

| שם | סוג | תיאור |
| --- | --- | --- |
| `int` | `INT 𝌠` | כל המספרים שנמצאו במחרוזת עם חיתוך של עשרוניים. |
| `float` | `FLOAT 𝌠` | כל המספרים שנמצאו במחרוזת כמספרים עשרוניים. |
| `string` | `STRING 𝌠` | כל המספרים שנמצאו במחרוזת כמספרים עשרוניים המומרים למחרוזת. |
| `count` | `INT` | מספר המספרים שנמצאו בערך. |

