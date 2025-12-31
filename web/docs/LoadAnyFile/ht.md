## Load Any File

![Load Any File](LoadAnyFile/LoadAnyFile.png)

(ComfyUI workflow ap gen yon pwogrè)

Chaje tout fichye tèks oswa bina ak pwodui kontni fichye kòm chenn oswa chenn base64. Anplis sa, ap eseye chaje l kòm `IMAGE`. Ak tou, ap eseye chaje tout metadòn yo.

`filepath` ap sipòte anotasyon ComfyUI filepath `[input]` `[output]` oswa `[temp]`.
`filepath` ap sipòte tou ekspansyon glob-pattern `subdir/**/*.png`.
Anndan ap itilize [glob.iglob](https://docs.python.org/3/library/glob.html#glob.iglob) nan Python la.

`metadata` ap rele `exiftool`, si li instale ak disponib nan `PATH`, si non li itilize `PIL.Image.info` kòm yon fòlba.

Pou rezon sekirite sèlman dènye kote sa yo ap sipòte: `[input] [output] [temp]`.
Pou rezon performans, kantite fichye yo limte nan: 1024.

### Antre yo

| Non | Tip | Deskrisyon |
| --- | --- | --- |
| `filepath` | `CHENN` | Dènye kote bazo ap de fòlba `[input]` dènye kote itilizatè a. Ap sipòte ekspansyon glob-pattern `subdir/**/*.png`. Ap itilize suffix ` [input]` ` [output]` oswa ` [temp]` (sou moun espas la!) pou spesifye yon lòt dènye kote itilizatè ComfyUI a. |

### Sòti yo

| Non | Tip | Deskrisyon |
| --- | --- | --- |
| `content` | `CHENN 𝌠` | Kontni fichye pou fichye tèks, base64 pou fichye bina. |
| `image` | `IMAGE 𝌠` | Tensor batch imaj la. |
| `mask` | `MASK 𝌠` | Tensor batch mas la. |
| `metadata` | `CHENN 𝌠` | Done exif sòti nan ExifTool. Bezwen `exiftool` komand la pou disponib nan `PATH`. |

