## Load Any File

![Load Any File](LoadAnyFile/LoadAnyFile.png)

(ComfyUI workflow inclòcha)

Carga tot tip de fichièr tèxt o binaire e provesís lo contengut coma cadena o cadena base64. De plus, ensaja de lo cargar coma `IMAGE`. E tanbèt ensaja de cargar tota metadonada.

`filepath` suppòrta los camins de fichièrs annotats de ComfyUI `[input]` `[output]` o `[temp]`.
`filepath` suppòrta tanbèt las extensions de patrons glob `subdir/**/*.png`.
Dins l'interior, utiliza la foncion python [glob.iglob](https://docs.python.org/3/library/glob.html#glob.iglob).

`metadata` invoca `exiftool`, se es installat e disponible dins `PATH`, se non utiliza `PIL.Image.info` coma fallback.

Per de rasons de seguretat, solament los repertòris seguents son suportats: `[input] [output] [temp]`.
Per de rasons de performància, lo nombre de fichièrs es limitat a: 1024.

### Entradas

| Nom | Tipe |Descripcion |
| --- | --- | --- |
| `filepath` | `STRING` | Lo repertòri de basa es per defaut lo repertòri d'utilizaire `[input]`. Supòrta las extensions de patrons glob `subdir/**/*.png`. Utilizatz lo suffix ` [input]` ` [output]` o ` [temp]` (pensez a l'espaci inicial !) per especificar un repertòri d'utilizaire ComfyUI diferent. |

### Sortidas

| Nom | Tipe |Descripcion |
| --- | --- | --- |
| `content` | `STRING 𝌠` | Contengut del fichièr pels fichièrs tèxt, base64 pels fichièrs binaris. |
| `image` | `IMAGE 𝌠` | Tensor de la lista d'imatges. |
| `mask` | `MASK 𝌠` | Tensor de la lista de masquas. |
| `metadata` | `STRING 𝌠` | Donadas Exif de ExifTool. Demandar la comanda `exiftool` per èsser disponibla dins `PATH`. |

