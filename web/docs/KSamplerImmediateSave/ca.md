## KSampler Immediate Save

![KSampler Immediate Save](KSamplerImmediateSave/KSamplerImmediateSave.png)

(ComfyUI workflow inclòs)

Expansió de nodes del `CheckpointLoader`, `KSampler`, `VAE Decode` i `Save Image` per processar com un sol node.
Això és útil si vols desar les imatges intermèdies per a quadrícules immediatament.

*"Un KSampler personalitzat només per desar una imatge? Ara m'he convertit en la cosa que buscava destruir!"*

### Entrades

| Nom | Tipus | Descripció |
| --- | --- | --- |
| `cpkt_name` | `COMBO` | El nom del punt de control (model) a carregar. |
| `positive` | `STRING` | La condició que descriu els atributs que vols incloure a la imatge. |
| `negative` | `STRING` | La condició que descriu els atributs que vols excloure de la imatge. |
| `latent_image` | `LATENT` | La imatge latent a desbruitar. |
| `seed` | `INT` | La llavor aleatòria utilitzada per crear el soroll. |
| `steps` | `INT` | El nombre de passos utilitzats en el procés de desbruitat. |
| `cfg` | `FLOAT` | L'escala de Guia Lliure de Classificadors equilibra la creativitat i l'adherència a la petició. Valors més alts resulten en imatges més ajustades a la petició, però valors massa alts impactaran negativament la qualitat. |
| `sampler_name` | `COMBO` | L'algorisme utilitzat en mostreig, això pot afectar la qualitat, velocitat i estil de la sortida generada. |
| `scheduler` | `COMBO` | El programador controla com el soroll es retira gradualment per formar la imatge. |
| `denoise` | `FLOAT` | La quantitat de desbruitat aplicada, valors més baixos mantindran l'estructura de la imatge inicial permetent mostreig imatge a imatge. |
| `filename_prefix` | `STRING` | El prefix per al fitxer a desar. Això pot incloure informació de format com %date:yyyy-MM-dd% o %Empty Latent Image.width% per incloure valors dels nodes. |

### Sortides

| Nom | Tipus | Descripció |
| --- | --- | --- |
| `image` | `IMAGE` | La imatge descodificada. |

