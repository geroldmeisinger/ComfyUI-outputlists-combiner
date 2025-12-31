## Last Inn Ethvert Fil

![Last Inn Ethvert Fil](LoadAnyFile/LoadAnyFile.png)

(ComfyUI workflow inkludert)

Laster inn hvilken som helst tekst- eller binærfil og gir filinnholdet som streng eller base64-streng. Prøver også å laste den inn som `IMAGE`. Prøver også å laste inn metadata.

`filepath` støtter ComfyUIs annoterte filbaner `[input]` `[output]` eller `[temp]`.
`filepath` støtter også utvidelser av glob-mønstre `subdir/**/*.png`.
Bruker internt Python's [glob.iglob](https://docs.python.org/3/library/glob.html#glob.iglob).

`metadata` kaller `exiftool`, hvis det er installert og tilgjengelig i `PATH`, ellers bruker `PIL.Image.info` som reserve.

Av sikkerhetsgrunner støttes kun følgende kataloger: `[input] [output] [temp]`.
Av ytelsesgrunner er antall filer begrenset til: 1024.

### Innputter

| Navn | Type | Beskrivelse |
| --- | --- | --- |
| `filepath` | `STRING` | Basismappe standardverdi til `[input]` brukerkatalog. Støtter utvidelse av glob-mønster `subdir/**/*.png`. Bruk suffikset ` [input]` ` [output]` eller ` [temp]` (husk ledende blanktegn!) for å spesifisere en annen ComfyUI brukerkatalog. |

### Utputter

| Navn | Type | Beskrivelse |
| --- | --- | --- |
| `content` | `STRING 𝌠` | Filinnhold for tekstfiler, base64 for binære filer. |
| `image` | `IMAGE 𝌠` | Bildesett tensor. |
| `mask` | `MASK 𝌠` | Maske sett tensor. |
| `metadata` | `STRING 𝌠` | Exif-data fra ExifTool. Krever at `exiftool`-kommandoen er tilgjengelig i `PATH`. |

