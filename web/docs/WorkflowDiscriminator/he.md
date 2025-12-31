## מבדיל עבודה

![Workflow Discriminator](WorkflowDiscriminator/WorkflowDiscriminator.png)

(הזרימה ב-ComfyUI נכללת)

השוואה של עבודות וחלוקתן כדי לחלץ ערכים שונים כרשימות פלט נפרדות.
אתה יכול להשתמש בצומת זה כדי לשחזר איך כל תמונה בודדת נוצרה מרשימה של תמונות עם אותו עבודה.
שימו לב ש-`IMAGE` של ComfyUI לא מכיל את נתוני העל של העבודה וצריך לטעון את התמונות עם מטענים מיוחדים של תמונות+נתוני על ולקשר את נתוני העל לצומת זה.
צמתים מותאמים עם מטענים של נתוני על כולל:
* `Load Any File.metadata` -> `JSON OutputList(jsonpath=$.["PNG:Prompt"]).value`
* [Crystool](https://github.com/crystian/ComfyUI-Crystools) `🪛 Load image with metadata.Metadata RAW` -> `🪛 Metadata extractor.prompt`
* [Simple_Readable_Metadata](https://github.com/ShammiG/ComfyUI-Simple_Readable_Metadata-SG) `Simple Readable Metadata-SG.metadata_raw`

### קלטים

| שם | סוג | תיאור |
| --- | --- | --- |
| `objs_0` | `*` | (אופציונלי) אובייקט בודד (או רשימה של אובייקטים), בדרך כלל של עבודה. `objs_0` ו-`more_objs` ישלבו יחד וקיימים לצורך נוחות, אם אתה רוצה להשוות רק שני אובייקטים. |
| `more_objs` | `*` | (אופציונלי) אובייקט נוסף (או רשימה של אובייקטים), בדרך כלל של עבודה. `objs_0` ו-`more_objs` ישלבו יחד וקיימים לצורך נוחות, אם אתה רוצה להשוות רק שני אובייקטים. |
| `ignore_jsonpaths` | `STRING` | (אופציונלי) רשימה של JSONPaths להתעלם מהם אם אתה רוצה לצרף כמה מבדילים יחד. |

### פלטים

| שם | סוג | תיאור |
| --- | --- | --- |
| `list_a` | `* 𝌠` |  |
| `list_b` | `* 𝌠` |  |
| `list_c` | `* 𝌠` |  |
| `list_d` | `* 𝌠` |  |
| `jsonpaths` | `STRING 𝌠` |  |

