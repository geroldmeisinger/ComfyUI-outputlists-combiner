## פלט רשימה מחרוזת

![String OutputList](StringOutputList/StringOutputList.png)

(הזרימה ב-ComfyUI נכללת)

יוצר רשימה פלט על ידי פיצול המחרוזת בשדה הטקסט עם מפריד.
`value` ו-`index` משתמשים ב-`is_output_list=True` (מסומן בסמל `𝌠`) ויהיו מעובדים לפי סדר על ידי צמתים מתאימים.

### קלטים

| שם | סוג | תיאור |
| --- | --- | --- |
| `separator` | `STRING` | המחרוזת המשמשת לפיצול ערכי שדה הטקסט. |
| `values` | `STRING` | הטקסט שברצונך לפרק לרשימה. שים לב שהמחרוזת נוקה מסיומות שורות חדשות לפני הפיצול, וכל פריט נוקה שוב מרווחים. |

### פלטים

| שם | סוג | תיאור |
| --- | --- | --- |
| `value` | `* 𝌠` | הערכים מהרשימה. |
| `index` | `INT 𝌠` | טווח של 0..count. אתה יכול להשתמש בזה כאינדקס. |
| `count` | `INT` | מספר הפריטים ברשימה. |
| `inspect_combo` | `COMBO` | פלט מטושטש שתוכלו להשתמש בו כדי לקשר ל-`COMBO` ולמלא אותו בערכיו. החיבור יוגדר מחדש אוטומטית לפלט `value`. |

