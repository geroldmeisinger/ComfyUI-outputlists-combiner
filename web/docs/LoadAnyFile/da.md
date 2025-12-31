## Indlæs enhver fil

![Indlæs enhver fil](LoadAnyFile/LoadAnyFile.png)

(ComfyUI workflow inkluderet)

Indlæser enhver tekst- eller binær fil og leverer filens indhold som streng eller base64 streng. Yderligere forsøger den at indlæse den som et `BILLEDE`. Og forsøger også at indlæse metadata.

`filepath` understøtter ComfyUI's annoterede filstier `[input]` `[output]` eller `[temp]`.
`filepath` understøtter også glob-mønstre `subdir/**/*.png`.
Bruger internt python's [glob.iglob](https://docs.python.org/3/library/glob.html#glob.iglob).

`metadata` kalder `exiftool`, hvis det er installeret og tilgængeligt på `PATH`, ellers bruger `PIL.Image.info` som fallback.

Af sikkerhedsmæssige årsager er kun følgende mapper understøttet: `[input] [output] [temp]`.
Af ydeevneårsager er antallet af filer begrænset til: 1024.

### Input

| Navn | Type | Beskrivelse |
| --- | --- | --- |
| `filepath` | `STRENG` | Basis mappe bruger standard `[input]` brugermappe. Understøtter glob-mønster udvidelse `subdir/**/*.png`. Brug suffiks ` [input]` ` [output]` eller ` [temp]` (husk det ledende mellemrum!) for at specificere en anden ComfyUI brugermappe. |

### Output

| Navn | Type | Beskrivelse |
| --- | --- | --- |
| `content` | `STRENG 𝌠` | Filindhold for tekstfiler, base64 for binære filer. |
| `image` | `BILLEDE 𝌠` | Billedbatch tensor. |
| `mask` | `MASKE 𝌠` | Maskebatch tensor. |
| `metadata` | `STRENG 𝌠` | Exif data fra ExifTool. Kræver at `exiftool` kommandoen er tilgængelig i `PATH`. |

