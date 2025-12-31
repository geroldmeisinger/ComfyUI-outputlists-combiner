## Henda hvørjari fílu

![Henda hvørjari fílu](LoadAnyFile/LoadAnyFile.png)

(ComfyUI workflow íðgu)

Hendar hvørjari tekst ella binæra fílu og leverar fíluna innihald sum streng ella base64 streng. Tíðari roynir at henda ta sum `IMAGE`. Og einnig roynir at henda allar metadata.

`filepath` styður ComfyUI's merkt fílunavn `[input]` `[output]` ella `[temp]`.
`filepath` styður einnig glob-mønster útviding `subdir/**/*.png`.
Innanlandsum nýtir python's [glob.iglob](https://docs.python.org/3/library/glob.html#glob.iglob).

`metadata` kallar `exiftool`, um ta er uppsettur og tilgjarnur á `PATH`, annars nýtir `PIL.Image.info` sum fallback.

Um trygdar ástæður eru einasteiðir mappurir styðdir: `[input] [output] [temp]`.
Um avkastan ástæður er tal av fílum avgjørd til: 1024.

### Inntak

| Navn | Slag | Lýsing |
| --- | --- | --- |
| `filepath` | `STRING` | Grundmappurin er sjálvum `[input]` brúkarføri. Styður glob-mønster útviding `subdir/**/*.png`. Nýt `suffix` ` [input]` ` [output]` ella ` [temp]` (margt við fyrsta whitespace!) til at tilkenda ein annan ComfyUI brúkarføri. |

### Úttak

| Navn | Slag | Lýsing |
| --- | --- | --- |
| `content` | `STRING 𝌠` | Fílun innihald fyri tekstfílur, base64 fyri binær fílur. |
| `image` | `IMAGE 𝌠` | Mynd batch tensor. |
| `mask` | `MASK 𝌠` | Mask batch tensor. |
| `metadata` | `STRING 𝌠` | Exif data frá ExifTool. Krevur `exiftool` kommando til at vera tilgjarnur á `PATH`. |

