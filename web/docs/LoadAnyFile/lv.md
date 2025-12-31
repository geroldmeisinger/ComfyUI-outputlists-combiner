## Load Any File

![Load Any File](LoadAnyFile/LoadAnyFile.png)

(ComfyUI workflow iekļauts)

Ielādē jebkuru teksta vai bināru failu un nodrošina faila saturu kā virkni vai base64 virkni. Papildus mēģina ielādēt to kā `IMAGE`. Un arī mēģina ielādēt jebkādu metadatus.

`filepath` atbalsta ComfyUI anotētās failu ceļus `[input]` `[output]` vai `[temp]`.
`filepath` arī atbalsta glob-pattern izvērstus `subdir/**/*.png`.
Iekšēji izmanto python [glob.iglob](https://docs.python.org/3/library/glob.html#glob.iglob).

`metadata` izsauc `exiftool`, ja tas ir instalēts un pieejams `PATH`, citādi izmanto `PIL.Image.info` kā atkāpšanās opciju.

Drošības apsvērumu dēļ tiek atbalstītas tikai sekojošas direktorijas: `[input] [output] [temp]`.
Veiktspējas apsvērumu dēļ failu skaits ir ierobežots līdz: 1024.

### Ievades

| Nosaukums | Tips | Apraksts |
| --- | --- | --- |
| `filepath` | `STRING` | Pamata direktorija pēc noklusējuma ir `[input]` lietotāja-direktorija. Atbalsta glob-pattern izvērstus `subdir/**/*.png`. Izmanto sufiksu ` [input]` ` [output]` vai ` [temp]` (ņem vērā priekšējo atstarpju!) lai norādītu citu ComfyUI lietotāja-direktoriju. |

### Izvades

| Nosaukums | Tips | Apraksts |
| --- | --- | --- |
| `content` | `STRING 𝌠` | Faila saturs teksta failiem, base64 bināriem failiem. |
| `image` | `IMAGE 𝌠` | Attēlu grupas tensoris. |
| `mask` | `MASK 𝌠` | Masu grupas tensoris. |
| `metadata` | `STRING 𝌠` | Exif dati no ExifTool. Nepieciešams `exiftool` komandas pieejamība `PATH`. |

