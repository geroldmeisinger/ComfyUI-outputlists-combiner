## Last inn alle filer

![Last inn alle filer](LoadAnyFile/LoadAnyFile.png)

(ComfyUI workflow inkludert)

Lastar inn alle tekst- eller binærfiler og leverer filinnhaldet som streng eller base64-streng. Prøver òg å lasta inn som `IMAGE`. Prøver òg å lasta inn metadata.

`filepath` støttar ComfyUIs merkte filbaner `[input]` `[output]` eller `[temp]`.
`filepath` støttar òg glob-mønsterutvidingar `subdir/**/*.png`.
Brukar internt Python's [glob.iglob](https://docs.python.org/3/library/glob.html#glob.iglob).

`metadata` kallar `exiftool`, viss det er installert og tilgjengeleg på `PATH`, elles brukar `PIL.Image.info` som reservealternativ.

Av sikkerheitsgrunnar er berre følgjande mapper støtta: `[input] [output] [temp]`.
Av ytegrunnar er talet på filer avgrensa til: 1024.

### Inndata

| Namn | Type | Skildring |
| --- | --- | --- |
| `filepath` | `STRING` | Basismappe standard er `[input]` brukarmappe. Støttar glob-mønsterutviding `subdir/**/*.png`. Bruk suffiks ` [input]` ` [output]` eller ` [temp]` (hugs føregåande mellomrom!) for å spesifisera ein annan ComfyUI brukarmappe. |

### Utdata

| Namn | Type | Skildring |
| --- | --- | --- |
| `content` | `STRING 𝌠` | Filinnhald for tekstfiler, base64 for binærfiler. |
| `image` | `IMAGE 𝌠` | Bildemasse tensor. |
| `mask` | `MASK 𝌠` | Maskebatch tensor. |
| `metadata` | `STRING 𝌠` | Exif-data frå ExifTool. Krev at `exiftool`-kommandoen er tilgjengeleg i `PATH`. |

