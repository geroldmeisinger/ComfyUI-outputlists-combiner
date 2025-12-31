## Cargar Cualquier Archivo

![Load Any File](LoadAnyFile/LoadAnyFile.png)

(ComfyUI workflow incluido)

Carga cualquier archivo de texto o binario y proporciona el contenido del archivo como cadena o cadena base64. Además, intenta cargarlo como `IMAGE`. Y también intenta cargar cualquier metadato.

`filepath` soporta las rutas de archivos anotadas de ComfyUI `[input]` `[output]` o `[temp]`.
`filepath` también soporta expansiones de patrones glob `subdir/**/*.png`.
Internamente utiliza [glob.iglob](https://docs.python.org/3/library/glob.html#glob.iglob) de Python.

`metadata` llama a `exiftool`, si está instalado y disponible en `PATH`, de lo contrario usa `PIL.Image.info` como alternativa.

Por razones de seguridad solo se soportan los siguientes directorios: `[input] [output] [temp]`.
Por razones de rendimiento el número de archivos está limitado a: 1024.

### Entradas

| Nombre | Tipo | Descripción |
| --- | --- | --- |
| `filepath` | `STRING` | Directorio base por defecto es el directorio de usuario `[input]`. Soporta expansión de patrones glob `subdir/**/*.png`. Usa el sufijo ` [input]` ` [output]` o ` [temp]` (¡cuidado con el espacio inicial!) para especificar un directorio de usuario de ComfyUI diferente. |

### Salidas

| Nombre | Tipo | Descripción |
| --- | --- | --- |
| `content` | `STRING 𝌠` | Contenido del archivo para archivos de texto, base64 para archivos binarios. |
| `image` | `IMAGE 𝌠` | Tensor de lote de imagen. |
| `mask` | `MASK 𝌠` | Tensor de lote de máscara. |
| `metadata` | `STRING 𝌠` | Datos Exif de ExifTool. Requiere que el comando `exiftool` esté disponible en `PATH`. |

