## Load Any File

![Load Any File](LoadAnyFile/LoadAnyFile.png)

(ComfyUI vinnusvæði included)

Hleður inn hvaða texta eða tvíkóða skrá og gefur skráarinnihald sem streng eða base64 streng. Auk þess reynir það að hlaða henni inn sem `IMAGE`. Og reynir einnig að hlaða inn hvaða lýsigögnum sem er.

`filepath` styður ComfyUI's merkt skráarslóðir `[input]` `[output]` eða `[temp]`.
`filepath` styður líka glob-mynstur útvíkkingu `subdir/**/*.png`.
Innri notar python's [glob.iglob](https://docs.python.org/3/library/glob.html#glob.iglob).

`metadata` kallar `exiftool`, ef það er uppsett og tiltækt á `PATH`, annars notar `PIL.Image.info` sem fallback.

Af öryggisástæðum eru aðeins eftirfarandi möppur studdar: `[input] [output] [temp]`.
Af hraðaástæðum er fjöldi skráa takmarkaður á: 1024.

### Inntök

| Nafn | Gerð | Lýsing |
| --- | --- | --- |
| `filepath` | `STRING` | Grundmappa stillir sjálfgefið `[input]` notandamappa. Styður glob-mynstur útvíkkingu `subdir/**/*.png`. Nota ending ` [input]` ` [output]` eða ` [temp]` (taka eftir fyrirfarandi bil!) til að tilgreina annað ComfyUI notandamappa. |

### Úttök

| Nafn | Gerð | Lýsing |
| --- | --- | --- |
| `content` | `STRING 𝌠` | Skráarinnihald fyrir textaskrár, base64 fyrir tvíkóða skrár. |
| `image` | `IMAGE 𝌠` | Mynd röð tensor. |
| `mask` | `MASK 𝌠` | Maskeð röð tensor. |
| `metadata` | `STRING 𝌠` | Exif gögn frá ExifTool. Krefst `exiftool` skipunar til að vera tiltækt á `PATH`. |

