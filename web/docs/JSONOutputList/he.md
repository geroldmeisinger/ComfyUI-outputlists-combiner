## פלט JSON כרשימה

![JSON OutputList](JSONOutputList/JSONOutputList.png)

(הזרימה ב-ComfyUI נכללת)

יוצר רשימה פלט על ידי חילוץ מערך או מילון מאובייקטי JSON.
משתמש בתחביר JSONPath כדי לחלץ את הערכים, ראה [JSONPath בוויקיפדיה](https://en.wikipedia.org/wiki/JSONPath) .
כל הערכים התואמים מופרדים לרשימה ארוכה אחת.
ניתן גם להשתמש בצומת זה כדי ליצור אובייקטים ממחרוזות טקסט כמו `[1, 2, 3]`.
`key`, `value`, `int` ו-`float` משתמשים ב-`is_output_list=True` (מסומן בסמל `𝌠`) ויהיו מעובדים לפי סדר על ידי צמתים מתאימים.

### קלטים

| שם | סוג | תיאור |
| --- | --- | --- |
| `jsonpath` | `STRING` | JSONPath המשמש לחלץ את הערכים. |
| `json` | `STRING` | מחרוזת JSON אשר מתרגם לאובייקט. |
| `obj` | `*` | (אופציונלי) אובייקט מכל סוג שילווה את מחרוזת ה-JSON |

### פלטים

| שם | סוג | תיאור |
| --- | --- | --- |
| `key` | `STRING 𝌠` | המפתח עבור מילונים או אינדקס עבור מערך (כמחרוזת). טכנית זה אינדקס גלובלי של הרשימה המופרدة עבור כל שאינו מפתח. |
| `value` | `STRING 𝌠` | הערך כמחרוזת. |
| `int` | `INT 𝌠` | הערך כמספר שלם (אם הוא לא יכול לנתח את המספר, מוגדר כברירת מחדל ל-0). |
| `float` | `FLOAT 𝌠` | הערך כמספר עשרוני (אם הוא לא יכול לנתח את המספר, מוגדר כברירת מחדל ל-0). |
| `count` | `INT` | מספר כולל של פריטים ברשימה המופרדה |
| `debug` | `STRING` | פלט ניפוי שגיאות של כל האובייקטים התואמים כמחרוזת JSON מעוצבת |

