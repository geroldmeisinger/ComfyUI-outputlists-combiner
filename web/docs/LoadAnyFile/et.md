## Lae mis tahes fail

![Lae mis tahes fail](LoadAnyFile/LoadAnyFile.png)

(ComfyUI töövoog on kaasatud)

Laadib mis tahes teksti või binaarfaili ja pakkub faili sisu sõne või base64 sõneena. Lisaks proovib seda laadida kui `IMAGE`. Ja proovib ka laadida kogu metaandmeid.

`filepath` toetab ComfyUI annoteeritud failiteed `[input]` `[output]` või `[temp]`.
`filepath` toetab ka glob-mustrite laiendusi `subdir/**/*.png`.
Sisemiselt kasutab pythoni [glob.iglob](https://docs.python.org/3/library/glob.html#glob.iglob).

`metadata` kutsub `exiftool` kõrval, kui see on paigaldatud ja saadaval `PATH`-is, vastasel juhul kasutab `PIL.Image.info` tagasihoidjana.

Turvalisusest hoiatuseks on toetatud ainult järgmised kataloogid: `[input] [output] [temp]`.
Jõudlusest hoiatuseks on failide arv piiratud: 1024.

### Sisendid

| Nimi | Tüüp | Kirjeldus |
| --- | --- | --- |
| `filepath` | `STRING` | Baaskataloogiks vaikimisi `[input]` kasutajakataloog. Toetab glob-mustrite laiendusi `subdir/**/*.png`. Kasuta sufiksit ` [input]` ` [output]` või ` [temp]` (märkida algne tühik!) erineva ComfyUI kasutajakataloogi määramiseks. |

### Väljundid

| Nimi | Tüüp | Kirjeldus |
| --- | --- | --- |
| `content` | `STRING 𝌠` | Faili sisu tekstifailide jaoks, base64 binaarfailide jaoks. |
| `image` | `IMAGE 𝌠` | Pildi partii tensor. |
| `mask` | `MASK 𝌠` | Maski partii tensor. |
| `metadata` | `STRING 𝌠` | Exif andmed ExifToolist. Vajab `exiftool` käsu olekut `PATH`-is. |

