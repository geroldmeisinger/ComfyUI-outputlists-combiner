## פלט מספר כרשימה

![Number OutputList](NumberOutputList/NumberOutputList.png)

(הזרימה ב-ComfyUI נכללת)

יוצר רשימה פלט עם טווח של ערכים מספריים.
משתמש ב-[numpy.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html) פנימית, כי הוא עובד יותר אמינות עם ערכים עשרוניים.
אם אתה רוצה להגדיר רשימות מספריות עם צעדים אקראיים במקום, בדוק את JSON OutputList והגדר מערך, למשל `[1, 42, 123]`.
`int`, `float`, `string` ו-`index` משתמשים ב-`is_output_list=True` (מסומן בסמל `𝌠`) ויהיו מעובדים לפי סדר על ידי צמתים מתאימים.

### קלטים

| שם | סוג | תיאור |
| --- | --- | --- |
| `start` | `FLOAT` | ערך התחלה ליצירת טווח. |
| `stop` | `FLOAT` | ערך סיום. אם `endpoint=include` אז המספר הזה יכלול ברשימה. |
| `num` | `INT` | מספר הפריטים ברשימה (אל תבלבל אותו עם `step`). |
| `endpoint` | `BOOLEAN` | מחליט אם ערך `stop` צריך להכלל או להתרחק מהפריטים. |

### פלטים

| שם | סוג | תיאור |
| --- | --- | --- |
| `int` | `INT 𝌠` | הערך המומר למספר שלם (מעוגל למטה/נחתך). |
| `float` | `FLOAT 𝌠` | הערך כמספר עשרוני. |
| `string` | `STRING 𝌠` | הערך כמספר עשרוני המומר למחרוזת. |
| `index` | `INT 𝌠` | טווח של 0..count שיכול לשמש כאינדקס. |
| `count` | `INT` | אותו דבר כמו `num`. |

