<!-- This file was auto-translated with a local LLM and last updated on 2025-12-28. -->
##تحويل לINT FLOAT STR

![Convert To Int Float Str](ConvertNumberToIntFloatStr/ConvertNumberToIntFloatStr.png)

(תבנית עבודה של ComfyUI מצורפת)

הופך כל דבר דומה למספר ל-`INT` `FLOAT` `STRING`.
משתמש פנימי ב-`nums_from_string.get_nums` שמאפשר מאוד במספרים שהוא מקבל. כל דבר ממספרים אמיתיים, מספרים עשרוניים אמיתיים, מספרים או מספרים עשרוניים כמחרוזות, מחרוזות שמכילות מספרים מרובים עם מפרידי אלפים.
השתמש במחרוזת `123;234;345` כדי ליצור במהירות רשימה של מספרים. לא השתמש בפסיקים כמפרידים כיוון שהם עלולים להיחשב מפרידי אלפים.
ה-`int`, `float` ו-`string` משתמשים ב-`is_output_list=True` (מסומן בסמל `𝌠`) ויסופרו סדרתי על ידי צמתים מתאימים.

### קלט

| שם | סוג | תיאור |
| --- | --- | --- |
| `any` | `*` | כל דבר שניתן להפוך בצורה משמעותית למחרוזת עם מספרים ניתנים לנתח |

### פלט

| שם | סוג | תיאור |
| --- | --- | --- |
| `int` | `INT 𝌠` | כל המספרים שנמצאו במחרוזת עם עשיריות נמחקות. |
| `float` | `FLOAT 𝌠` | כל המספרים שנמצאו במחרוזת כמספרים עשרוניים. |
| `string` | `STRING 𝌠` | כל המספרים שנמצאו במחרוזת כמספרים עשרוניים המופצים למחרוזת. |
| `count` | `INT` | כמות המספרים שנמצאו בערך. |

