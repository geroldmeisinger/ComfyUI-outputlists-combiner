## Load Any File

![Load Any File](LoadAnyFile/LoadAnyFile.png)

(ComfyUI workflow d'ofgesech)

Luedt all Text- oder Binarydatei a gëtt den Dateiinhalt als String oder base64-String. Aproch, et wäert esouwuel als `IMAGE` lueden. An probéiert och, all Metadaten ze lueden.

`filepath` ënnerstëtzt ComfyUI's annotéiert Dateipfade `[input]` `[output]` oder `[temp]`.
`filepath` ënnerstëtzt och glob-Pattern-Erweidungen `subdir/**/*.png`.
Intern benotzt dës Node python's [glob.iglob](https://docs.python.org/3/library/glob.html#glob.iglob).

`metadata` ruft `exiftool` op, wann et installéiert a zu `PATH` disponibel ass, andeern gëtt `PIL.Image.info` als Fallback benotzt.

Aus Sicherheetsgrënn sinn nëmmen dës Verwaltungsdirektoiren ënnerstëtzt: `[input] [output] [temp]`.
Aus Performanzgrënn ass d'Zuel vun den Dateie op: 1024 limitéiert.

### Input

| Numm | Typ | Beschreiwung |
| --- | --- | --- |
| `filepath` | `STRING` | Basiskatalog, deefolleg op `[input]` Benotzerkatalog. Ënnerstëtzt glob-Pattern-Erweidung `subdir/**/*.png`. Benotzt den Suffix ` [input]` ` [output]` oder ` [temp]` (denk de führenden Leerzeechen!) fir e aneren ComfyUI Benotzerkatalog ze specifizéieren. |

### Output

| Numm | Typ | Beschreiwung |
| --- | --- | --- |
| `content` | `STRING 𝌠` | Dateiinhalt fir Textdateien, base64 fir Binarydateien. |
| `image` | `IMAGE 𝌠` | Bild Batch Tensor. |
| `mask` | `MASK 𝌠` | Maske Batch Tensor. |
| `metadata` | `STRING 𝌠` | Exif Daten vun ExifTool. Benéiht `exiftool` Befehl zu `PATH` disponibel. |

