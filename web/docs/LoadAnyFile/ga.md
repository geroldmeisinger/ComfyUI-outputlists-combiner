## Lódáil Aon Chomhad

![Lódáil Aon Chomhad](LoadAnyFile/LoadAnyFile.png)

(ComfyUI workflow san áireamh)

Lódálann sé aon chomhad téacs nó heanach agus soláthraíonn an t-inneachar an chomhaid mar shreang nó shreang base64. De réir chéim, tries é é a lódáil mar `IMAGE`. Agus freisin, tries é a lódáil aon sonraí sonraí.

Úsáidtear `filepath` ComfyUI's annotated filepaths `[input]` `[output]` nó `[temp]`.
Úsáidtear `filepath` freisin glob-pattern expansions `subdir/**/*.png`.
De réir teachtaireachta, úsáideann python's [glob.iglob](https://docs.python.org/3/library/glob.html#glob.iglob).

Úsáidtear `metadata` `exiftool`, má tá sé suiteáilte agus ar fáil ag `PATH`, de réir chéim, úsáideann `PIL.Image.info` mar aiseolas.

Donn de réasúint amháin na seoltaí seo a leanas a thacaítear: `[input] [output] [temp]`.
Donn de réasúint feidhmiúil, tá líon na gcómhad a chuirtear i dtús: 1024.

### Ionchuir

| Ainm | Cineál | Cur Síos |
| --- | --- | --- |
| `filepath` | `STRING` | An chomhad bunaidh réamhshocraithe go `[input]` comhad-úsáideoir. Tacaíonn sé le glob-pattern expansion `subdir/**/*.png`. Úsáid suffix ` [input]` ` [output]` nó ` [temp]` (tabhair faoi deara an tábáil atá ar tosach!) chun comhad-úsáideoir eile ComfyUI a shonrú. |

### Aschuir

| Ainm | Cineál | Cur Síos |
| --- | --- | --- |
| `content` | `STRING 𝌠` | Inneachar an chomhaid le haghaidh comhaid téacs, base64 le haghaidh comhaid heanach. |
| `image` | `IMAGE 𝌠` | Tensór batch íomhá. |
| `mask` | `MASK 𝌠` | Tensór batch másc. |
| `metadata` | `STRING 𝌠` | Sonraí Exif ó ExifTool. Teastaíonn `exiftool` ordú a bheith ar fáil ag `PATH`. |

