## KSampler Omedelbar Spara

![KSampler Omedelbar Spara](KSamplerImmediateSave/KSamplerImmediateSave.png)

(ComfyUI workflow inkluderad)

Nodexpansion av standard `CheckpointLoader`, `KSampler`, `VAE Decode` och `Save Image` för att bearbeta som en enhet.
Detta är användbart om du vill spara mellanbilder för rutnät omedelbart.

*"En anpassad KSampler bara för att spara en bild? Nu har jag blivit det jag ville förstöra!"*

### Ingångar

| Namn | Typ | Beskrivning |
| --- | --- | --- |
| `cpkt_name` | `COMBO` | Namnet på kontrollpunkten (modellen) som ska laddas. |
| `positive` | `STRING` | Villkoret som beskriver attributen du vill inkludera i bilden. |
| `negative` | `STRING` | Villkoret som beskriver attributen du vill undanta från bilden. |
| `latent_image` | `LATENT` | Den latenta bilden att avbrusad. |
| `seed` | `INT` | Den slumpmässiga frö som används för att skapa bruset. |
| `steps` | `INT` | Antalet steg som används i avbrusningsprocessen. |
| `cfg` | `FLOAT` | Skalan för Classifier-Free Guidance balanserar kreativitet och efterlevnad av prompten. Högre värden resulterar i bilder som mer nära matchar prompten, men för höga värden påverkar kvalitén negativt. |
| `sampler_name` | `COMBO` | Algoritmen som används vid sampling, detta kan påverka kvalitén, hastigheten och stilen på den genererade utdata. |
| `scheduler` | `COMBO` | Schemat kontrollerar hur bruset gradvis tas bort för att forma bilden. |
| `denoise` | `FLOAT` | Mängden avbrusning som appliceras, lägre värden behåller strukturen i den ursprungliga bilden och tillåter för bild-till-bild sampling. |
| `filename_prefix` | `STRING` | Prefixet för filen som ska sparas. Detta kan inkludera formateringsinformation såsom %date:yyyy-MM-dd% eller %Empty Latent Image.width% för att inkludera värden från noder. |

### Utgångar

| Namn | Typ | Beskrivning |
| --- | --- | --- |
| `image` | `IMAGE` | Den avkodade bilden. |

