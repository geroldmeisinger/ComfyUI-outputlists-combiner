## Laad Elk Bestand

![Laad Elk Bestand](LoadAnyFile/LoadAnyFile.png)

(ComfyUI workflow inbegrepen)

Laadt elk tekst- of binaire bestand en levert de bestandsinhoud als string of base64 string. Probeer ook om het als `IMAGE` te laden. En probeert ook om metadata te laden.

`filepath` ondersteunt ComfyUI's geneste bestandspaden `[input]` `[output]` of `[temp]`.
`filepath` ondersteunt ook glob-patroon uitbreidingen `subdir/**/*.png`.
Intern gebruikt het python's [glob.iglob](https://docs.python.org/3/library/glob.html#glob.iglob).

`metadata` roept `exiftool` aan, indien geïnstalleerd en beschikbaar op `PATH`, anders gebruikt het `PIL.Image.info` als fallback.

Om veiligheidsredenen zijn alleen de volgende mappen ondersteund: `[input] [output] [temp]`.
Om prestatieredenen zijn het aantal bestanden beperkt tot: 1024.

### Invoer

| Naam | Type | Beschrijving |
| --- | --- | --- |
| `filepath` | `STRING` | Basismap standaard naar `[input]` gebruikersmap. Ondersteunt glob-patroon uitbreiding `subdir/**/*.png`. Gebruik suffix ` [input]` ` [output]` of ` [temp]` (let op het voorafgaande witruimte!) om een andere ComfyUI gebruikersmap te specificeren. |

### Uitvoer

| Naam | Type | Beschrijving |
| --- | --- | --- |
| `content` | `STRING 𝌠` | Bestandsinhoud voor tekstbestanden, base64 voor binaire bestanden. |
| `image` | `IMAGE 𝌠` | Image batch tensor. |
| `mask` | `MASK 𝌠` | Mask batch tensor. |
| `metadata` | `STRING 𝌠` | Exif data van ExifTool. Vereist dat `exiftool` command beschikbaar is in `PATH`. |

