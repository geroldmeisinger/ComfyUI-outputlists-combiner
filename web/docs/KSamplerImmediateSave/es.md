## KSampler Guardado Inmediato

![KSampler Immediate Save](KSamplerImmediateSave/KSamplerImmediateSave.png)

(ComfyUI workflow incluido)

Expansión de nodo del `CheckpointLoader`, `KSampler`, `VAE Decode` y `Save Image` por defecto para procesar como uno solo.
Esto es útil si desea guardar las imágenes intermedias para cuadrículas inmediatamente.

*"¿Un KSampler personalizado solo para guardar una imagen? Ahora me he convertido en la cosa que perseguía destruir!"*

### Entradas

| Nombre | Tipo | Descripción |
| --- | --- | --- |
| `cpkt_name` | `COMBO` | El nombre del punto de control (modelo) a cargar. |
| `positive` | `STRING` | La condición que describe los atributos que desea incluir en la imagen. |
| `negative` | `STRING` | La condición que describe los atributos que desea excluir de la imagen. |
| `latent_image` | `LATENT` | La imagen latente a desruido. |
| `seed` | `INT` | La semilla aleatoria utilizada para crear el ruido. |
| `steps` | `INT` | El número de pasos utilizados en el proceso de desruido. |
| `cfg` | `FLOAT` | La escala de Guía Libre de Clasificador equilibra creatividad y adherencia al prompt. Valores más altos resultan en imágenes que coinciden más estrechamente con el prompt, sin embargo valores demasiado altos impactarán negativamente la calidad. |
| `sampler_name` | `COMBO` | El algoritmo utilizado al muestrear, esto puede afectar la calidad, velocidad y estilo de la salida generada. |
| `scheduler` | `COMBO` | El programador controla cómo se elimina gradualmente el ruido para formar la imagen. |
| `denoise` | `FLOAT` | La cantidad de desruido aplicado, valores más bajos mantendrán la estructura de la imagen inicial permitiendo muestreo de imagen a imagen. |
| `filename_prefix` | `STRING` | El prefijo para el archivo a guardar. Esto puede incluir información de formato como %date:yyyy-MM-dd% o %Empty Latent Image.width% para incluir valores de nodos. |

### Salidas

| Nombre | Tipo | Descripción |
| --- | --- | --- |
| `image` | `IMAGE` | La imagen decodificada. |

