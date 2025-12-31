## לודן אן אנדערע פאيل

![לודן אן אנדערע פאיל](LoadAnyFile/LoadAnyFile.png)

(אינקלוזיוו דער ComfyUI ווערקפלוע)

לודט אן אנדערע טעקסט אדער בינערי פאיל און פארזעצט די פאיל אינטערהאלט ווי סטירינג אדער באזע 64 סטירינג. אדערשעט אירט אסאך צו לודן עס ווי א `IMAGE`. און אסאך צו לודן אן אנדערע מעטאדאטע.

`filepath` צועט צו ComfyUI'ס אנדאטערטע פאילפאטס `[input]` `[output]` אדער `[temp]`.
`filepath` אסאך צועט גלоб-פאטערן אענדערונגען `subdir/**/*.png`.
אינטערען נוצט פיטשאנס'ע [glob.iglob](https://docs.python.org/3/library/glob.html#glob.iglob).

`metadata` רuft `exiftool` auf, ווען עס איז אינסטאלירט און פארפינדיג אן `PATH`, אנדערש נוצט `PIL.Image.info` ווי א פאלבאק.

פון זיכערהייט גרעסערע נייגט נאך די פאלגנדע דירעקטאריען זענען צועט: `[input] [output] [temp]`.
פון פארמאן גרעסערע נייגט די אנטאל פון פאילן איז געלאייט צו: 1024.

### אינפונטס

| נאמען | טיפ | באזיס |
| --- | --- | --- |
| `filepath` | `STRING` | בעזירע דירעקטאריע אינטער אן `[input]` נוצער-דירעקטאריע. צועט גלוב-פאטערן אענדערונגען `subdir/**/*.png`. נוצן סאפיקס ` [input]` ` [output]` אדער ` [temp]` (דערשעט די פארענדערטע וואס איז פארענדערט!) צו ספעציפיצירן אן אנדערע ComfyUI נוצער-דירעקטאריע. |

### אוסגאנגען

| נאמען | טיפ | באזיס |
| --- | --- | --- |
| `content` | `STRING 𝌠` | פאיל אינטערהאלט פאר טעקסט פאילן, באזע 64 פאר בינערי פאילן. |
| `image` | `IMAGE 𝌠` | באנד איבערטערן טענסער. |
| `mask` | `MASK 𝌠` | מאסק באנד איבערטערן טענסער. |
| `metadata` | `STRING 𝌠` | אקסיפ-דאטן פון ExifTool. דערויסט דער `exiftool` ב командע צו זיין פארפינדיג אין `PATH`. |

