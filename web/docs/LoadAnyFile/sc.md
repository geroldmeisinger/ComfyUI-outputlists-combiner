## Càrriga unu Archìviu Chi Si Siat

![Càrriga unu Archìviu Chi Si Siat](LoadAnyFile/LoadAnyFile.png)

(ComfyUI workflow inclùidu)

Càrriga unu archìviu de testu o binàriu e frunet su contenutu de s’archìviu comente stringa o stringa base64. In prus, attempat de carrigare s’archìviu comente `IMAGE`. E prus, attempat de carrigare cada metadata.

`filepath` suportat sas rutas de archìviu annotadas de ComfyUI `[input]` `[output]` o `[temp]`.
`filepath` suportat ancu sas espansiónes de modelu glob `subdir/**/*.png`.
In s’istadu impreadu python sas [glob.iglob](https://docs.python.org/3/library/glob.html#glob.iglob).

`metadata` chiamat s’atzessu `exiftool`, si est istalladu e disponìbile in `PATH`, in s’altru casu impread s’atzessu `PIL.Image.info` comente fallback.

Pro resones de siguresa sunt suportadas isceti sas cartellas segus: `[input] [output] [temp]`.
Pro resones de performàntzia su numeru de archìvios est limitadu a: 1024.

### Inputs

| Nome | Tipu | Descritzione |
| --- | --- | --- |
| `filepath` | `STRING` | Sa cartella base est predefinida a sa cartella de s’impreadore `[input]`. Suportat sas espansiónes de modelu glob `subdir/**/*.png`. Imprea su suffìtziu ` [input]` ` [output]` o ` [temp]` (si cunvintiat su spàtziu in antis!) pro specificare una cartella de s’impreadore de ComfyUI diferente. |

### Outputs

| Nome | Tipu | Descritzione |
| --- | --- | --- |
| `content` | `STRING 𝌠` | Contenutu de s’archìviu pro archìvios de testu, base64 pro archìvios binàrios. |
| `image` | `IMAGE 𝌠` | Tensor de unu grupu de immàgines. |
| `mask` | `MASK 𝌠` | Tensor de unu grupu de màscaras. |
| `metadata` | `STRING 𝌠` | Datos Exif dae ExifTool. Rechedet chi su cumandu `exiftool` siat disponìbile in `PATH`. |

