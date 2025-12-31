## טען כל קובץ

![Load Any File](LoadAnyFile/LoadAnyFile.png)

(הזרמת ComfyUI מצורפת)

טוען כל קובץ טקסט או ثنائي ומספק את תוכן הקובץ כטקסט או כטקסט base64. בנוסף מנסה לטעון אותו כ`IMAGE`. ונסה גם לטעון_metadata.

`filepath` תומך בנתיבי קבצים הממוספרים של ComfyUI `[input]` `[output]` או `[temp]`.
`filepath` גם תומך בהרחבות דפוס glob `subdir/**/*.png`.
בפנימה משתמש ב-[glob.iglob](https://docs.python.org/3/library/glob.html#glob.iglob) של Python.

`metadata` קורא ל `exiftool`, אם הוא מותקן וזמין ב `PATH`, אחרת משתמש ב `PIL.Image.info` כחלופה.

לأسباب אمنיות רק הספריות הבאות נתמכות: `[input] [output] [temp]`.
לأسباب ביצועים מספר הקבצים מוגבל ל: 1024.

### קלטים

| שם | סוג | תיאור |
| --- | --- | --- |
| `filepath` | `STRING` | ספריית בסיס כברירת מחדל `[input]` ספריית המשתמש. תומך בהרחבות דפוס glob `subdir/**/*.png`. השתמש בסופית ` [input]` ` [output]` או ` [temp]` (שים לב לרווח המובנה!) כדי לציין ספריית משתמש ComfyUI שונה. |

### פלטים

| שם | סוג | תיאור |
| --- | --- | --- |
| `content` | `STRING 𝌠` | תוכן הקובץ לקבצים טקסטואליים, base64 לקבצים ثنائيים. |
| `image` | `IMAGE 𝌠` | טנזור אוספים של תמונה. |
| `mask` | `MASK 𝌠` | טנזור אוספים של מסכה. |
| `metadata` | `STRING 𝌠` | נתוני Exif מ ExifTool. דורש שהפקודה `exiftool` תהייה זמינה ב `PATH`. |

