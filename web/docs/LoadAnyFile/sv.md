## Ladda Valfri Fil

![Ladda Valfri Fil](LoadAnyFile/LoadAnyFile.png)

(ComfyUI workflow inkluderad)

Laddar valfri text- eller binär fil och tillhandahåller filinnehållet som sträng eller base64-sträng. Försöker även ladda den som `IMAGE`. Försöker också ladda metadata.

`filepath` stöder ComfyUI:s annoterade sökvägar `[input]` `[output]` eller `[temp]`.
`filepath` stöder också utökning med glob-mönster `subdir/**/*.png`.
Använder internt Python's [glob.iglob](https://docs.python.org/3/library/glob.html#glob.iglob).

`metadata` anropar `exiftool`, om det är installerat och tillgängligt i `PATH`, annars använder `PIL.Image.info` som reserv.

Av säkerhetsskäl stöds endast följande kataloger: `[input] [output] [temp]`.
Av prestandaskäl är antalet filer begränsat till: 1024.

### Inmatningar

| Namn | Typ | Beskrivning |
| --- | --- | --- |
| `filepath` | `STRING` | Basvägen standard till `[input]` användarkatalog. Stöder utökning med glob-mönster `subdir/**/*.png`. Använd suffix ` [input]` ` [output]` eller ` [temp]` (observera ledande blanksteg!) för att ange en annan ComfyUI-användarkatalog. |

### Utmatningar

| Namn | Typ | Beskrivning |
| --- | --- | --- |
| `content` | `STRING 𝌠` | Filinnehåll för textfiler, base64 för binära filer. |
| `image` | `IMAGE 𝌠` | Bildbatch tensor. |
| `mask` | `MASK 𝌠` | Maskbatch tensor. |
| `metadata` | `STRING 𝌠` | Exif-data från ExifTool. Kräver att `exiftool`-kommandot är tillgängligt i `PATH`. |

