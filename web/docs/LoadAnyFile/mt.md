## Load Any File

![Load Any File](LoadAnyFile/LoadAnyFile.png)

(ComfyUI workflow included)

Jibbraw kwalunkwe fajl tal-test jew binary u jipprovdili kontenut tal-fajl bħala string jew string base64. Addizzionalment jipprova jibbrawu bħala `IMAGE`. U jipprova jibbraw anki kwalunkwe metadata.

`filepath` jibbraw ComfyUI's annotated filepaths `[input]` `[output]` jew `[temp]`.
`filepath` jibbraw anke glob-pattern expansions `subdir/**/*.png`.
Interna jibbraw python's [glob.iglob](https://docs.python.org/3/library/glob.html#glob.iglob).

`metadata` jibbraw `exiftool`, jekk jkun installat u disponibbli f`PATH`, inkella jibbraw `PIL.Image.info` bħala fallback.

Għal raġunijiet ta’ ħarsa biss il-following directories jkunu appoġġjati: `[input] [output] [temp]`.
Għal raġunijiet ta’ prestazzjoni il-numru ta’ fajls jkun limitat għal: 1024.

### Inputs

| Isem | Tip | Deskrizzjoni |
| --- | --- | --- |
| `filepath` | `STRING` | Direttorju bażi jibbraw għal `[input]` user-directory. Jibbraw glob-pattern expansion `subdir/**/*.png`. Użaw suffix ` [input]` ` [output]` jew ` [temp]` (fammi l-ħażna tal-żewġ spazji!) biex jiddeżġini direktorju differenti ta’ ComfyUI user-directory. |

### Outputs

| Isem | Tip | Deskrizzjoni |
| --- | --- | --- |
| `content` | `STRING 𝌠` | Kontenut tal-fajl għal fajls tal-test, base64 għal fajls binary. |
| `image` | `IMAGE 𝌠` | Image batch tensor. |
| `mask` | `MASK 𝌠` | Mask batch tensor. |
| `metadata` | `STRING 𝌠` | Data Exif minn ExifTool. Jeħtieġu l-command `exiftool` biex jkun disponibbli f`PATH`. |

