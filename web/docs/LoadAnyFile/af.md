## Laai enige lêer

![Laai enige lêer](LoadAnyFile/LoadAnyFile.png)

(ComfyUI workflow ingesluit)

Laai enige teks- of binaire lêer en verskaf die lêerinhoud as string of base64 string. Probeer ook om dit as `IMAGE` te laai. En probeer ook om enige metadata te laai.

`filepath` ondersteun ComfyUI se geanoteerde lêerpad: `[input]` `[output]` of `[temp]`.
`filepath` ondersteun ook glob-patroon uitbreidings `subdir/**/*.png`.
Gebruik intern python se [glob.iglob](https://docs.python.org/3/library/glob.html#glob.iglob).

`metadata` roep `exiftool` op, indien dit geïnstalleer en beskikbaar is by `PATH`, anders gebruik `PIL.Image.info` as terugvalopsie.

Weens sekuriteit redene word slegs die volgende gidsen ondersteun: `[input] [output] [temp]`.
Weens werkverrigting redene is die aantal lêers beperk tot: 1024.

### Invoere

| Naam | Tipe | Beskrywing |
| --- | --- | --- |
| `filepath` | `STRING` | Basiskatalogus standaard op `[input]` gebruiker-katalogus. Ondersteun glob-patroon uitbreiding `subdir/**/*.png`. Gebruik suffix ` [input]` ` [output]` of ` [temp]` (let op die voorafgaande spasie!) om 'n ander ComfyUI gebruiker-katalogus te spesifiseer. |

### Uitvoere

| Naam | Tipe | Beskrywing |
| --- | --- | --- |
| `content` | `STRING 𝌠` | Lêerinhoud vir tekslêers, base64 vir binaire lêers. |
| `image` | `IMAGE 𝌠` | Beeld batch tensor. |
| `mask` | `MASK 𝌠` | Masker batch tensor. |
| `metadata` | `STRING 𝌠` | Exif data van ExifTool. Vereis dat `exiftool` opdrag beskikbaar is in `PATH`. |

