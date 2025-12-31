## Load Any File

![Load Any File](LoadAnyFile/LoadAnyFile.png)

(ComfyUI workflow incluído)

Carga calquera ficheiro de texto ou binario e fornece o contido do ficheiro como cadea ou cadea base64. Ademais intenta cargalo como `IMAGE`. E tamén intenta cargar calquera metadato.

`filepath` admite os camiños de ficheiro anotados de ComfyUI `[input]` `[output]` ou `[temp]`.
`filepath` tamén admite expansións de patróns glob `subdir/**/*.png`.
Internamente usa a [glob.iglob](https://docs.python.org/3/library/glob.html#glob.iglob) de Python.

`metadata` chama a `exiftool`, se está instalado e dispoñible en `PATH`, de outra maneira usa `PIL.Image.info` como alternativa.

Por razóns de seguridade só se admiten os seguintes directorios: `[input] [output] [temp]`.
Por razóns de rendemento o número de ficheiros está limitado a: 1024.

### Entradas

| Nome | Tipo | Descrición |
| --- | --- | --- |
| `filepath` | `STRING` | O directorio base predeterminado é o directorio do usuario `[input]`. Admite expansión de patróns glob `subdir/**/*.png`. Use o sufixo ` [input]` ` [output]` ou ` [temp]` (teña en conta o espazo inicial!) para especificar un directorio de usuario ComfyUI diferente. |

### Saídas

| Nome | Tipo | Descrición |
| --- | --- | --- |
| `content` | `STRING 𝌠` | Contido do ficheiro para ficheiros de texto, base64 para ficheiros binarios. |
| `image` | `IMAGE 𝌠` | Tensor de lote de imaxes. |
| `mask` | `MASK 𝌠` | Tensor de lote de máscaras. |
| `metadata` | `STRING 𝌠` | Datos Exif de ExifTool. Require que o comando `exiftool` estea dispoñible en `PATH`. |

