## KSampler Immediate Save

![KSampler Immediate Save](KSamplerImmediateSave/KSamplerImmediateSave.png)

(ComfyUI workflow incluído)

Expansión do nodo por defecto `CheckpointLoader`, `KSampler`, `VAE Decode` e `Save Image` para procesalos como un só.
Isto é útil se quere gardar as imaxes intermedias para rexas inmediatamente.

*"Un KSampler personalizado só para gardar unha imaxe? Agora xa me convertín no mesmo que perseguín para destruír!"*

### Entradas

| Nome | Tipo | Descrición |
| --- | --- | --- |
| `cpkt_name` | `COMBO` | O nome do punto de comprobación (modelo) a cargar. |
| `positive` | `STRING` | A condición que describe os atributos que quere incluír na imaxe. |
| `negative` | `STRING` | A condición que describe os atributos que quere excluir da imaxe. |
| `latent_image` | `LATENT` | A imaxe latente a desorzar. |
| `seed` | `INT` | A semente aleatoria usada para crear o ruído. |
| `steps` | `INT` | O número de pasos usados no proceso de desorización. |
| `cfg` | `FLOAT` | A escala de Guía Libre de Clasificadores equilibra a creatividade e o cumprimento do prompt. Valores máis altos resultan en imaxes máis axustadas ao prompt, pero valores demasiado altos impactarán negativamente na calidade. |
| `sampler_name` | `COMBO` | O algoritmo usado ao mostrear, isto pode afectar a calidade, velocidade e estilo da saída xerada. |
| `scheduler` | `COMBO` | O programador controla como se retira gradualmente o ruído para formar a imaxe. |
| `denoise` | `FLOAT` | A cantidade de desorización aplicada, valores máis baixos manterán a estrutura da imaxe inicial permitindo mostreo de imaxe a imaxe. |
| `filename_prefix` | `STRING` | O prefixo para o ficheiro a gardar. Pode incluír información de formato como %date:yyyy-MM-dd% ou %Empty Latent Image.width% para incluír valores dos nodos. |

### Saídas

| Nome | Tipo | Descrición |
| --- | --- | --- |
| `image` | `IMAGE` | A imaxe decodificada. |

