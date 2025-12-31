## Load Any File

![Load Any File](LoadAnyFile/LoadAnyFile.png)

(ComfyUI workflow bijgevoegd)

Laod elk text of binary bestand en geef de bestandsinhoud um als string of base64 string. Additionally probeert ‘t ‘t als `IMAGE` te laod. En probeert ook metadata te laod.

`filepath` ondersteunt ComfyUI's genoteerde bestandspaden `[input]` `[output]` of `[temp]`.
`filepath` ondersteunt ook glob-pattern expansies `subdir/**/*.png`.
Intern gebruuk ‘t python's [glob.iglob](https://docs.python.org/3/library/glob.html#glob.iglob).

`metadata` roept `exiftool` aan, es ‘t geïnstalleerd is en beschikbaar is op `PATH`, anders gebruk ‘t `PIL.Image.info` als fallback.

Um veiligheidsredenen zien alleen de volgende mappen ondersteund: `[input] [output] [temp]`.
Um prestatieredenen zien ‘t aantal bestande beperkt tot: 1024.

### Invoere

| Naom | Type | Beschrèving |
| --- | --- | --- |
| `filepath` | `STRING` | Basis map standaard `[input]` gebruikersmap. Ondersteunt glob-pattern expansie `subdir/**/*.png`. Gebruk suffix ` [input]` ` [output]` of ` [temp]` (let op de lege ruimte!) um ‘n andere ComfyUI gebruikersmap te specificeer. |

### Uitvoere

| Naom | Type | Beschrèving |
| --- | --- | --- |
| `content` | `STRING 𝌠` | Bestandsinhoud um text bestande, base64 um binary bestande. |
| `image` | `IMAGE 𝌠` | Image batch tensor. |
| `mask` | `MASK 𝌠` | Mask batch tensor. |
| `metadata` | `STRING 𝌠` | Exif data um ExifTool. Vereist `exiftool` command um beschikbaar te zien op `PATH`. |

