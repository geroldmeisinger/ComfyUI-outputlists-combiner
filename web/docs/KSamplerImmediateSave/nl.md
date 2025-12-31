## KSampler Direct Opslaan

![KSampler Direct Opslaan](KSamplerImmediateSave/KSamplerImmediateSave.png)

(ComfyUI workflow inbegrepen)

Node uitbreiding van de standaard `CheckpointLoader`, `KSampler`, `VAE Decode` en `Save Image` om als één proces te verwerken.
Dit is handig als je de tussenliggende afbeeldingen voor grids direct wilt opslaan.

*"Een aangepaste KSampler alleen om een afbeelding op te slaan? Nu ben ik hetzelfde geworden wat ik probeerde te vernietigen!"*

### Invoeren

| Naam | Type | Beschrijving |
| --- | --- | --- |
| `cpkt_name` | `COMBO` | De naam van het checkpoint (model) om te laden. |
| `positive` | `STRING` | De voorwaarde die de kenmerken beschrijft die je in de afbeelding wilt opnemen. |
| `negative` | `STRING` | De voorwaarde die de kenmerken beschrijft die je uit de afbeelding wilt uitsluiten. |
| `latent_image` | `LATENT` | De latent afbeelding om te ontrafelen. |
| `seed` | `INT` | De willekeurige seed gebruikt voor het genereren van de ruis. |
| `steps` | `INT` | Het aantal stappen gebruikt in het ontrafelingsproces. |
| `cfg` | `FLOAT` | De Classifier-Free Guidance schaal balancert creativiteit en naleving van de prompt. Hogere waarden resulteren in afbeeldingen die nauwkeuriger overeenkomen met de prompt, maar te hoge waarden zullen de kwaliteit negatief beïnvloeden. |
| `sampler_name` | `COMBO` | Het algoritme gebruikt bij het sampelen, dit kan de kwaliteit, snelheid en stijl van de gegenereerde uitvoer beïnvloeden. |
| `scheduler` | `COMBO` | De scheduler bepaalt hoe de ruis geleidelijk wordt verwijderd om de afbeelding te vormen. |
| `denoise` | `FLOAT` | Het aantal ontrafelingsprocessen toegepast, lagere waarden behouden de structuur van de initiële afbeelding waardoor image-to-image sampling mogelijk is. |
| `filename_prefix` | `STRING` | Het voorvoegsel voor het bestand om op te slaan. Dit kan formatteringsinformatie bevatten zoals %date:yyyy-MM-dd% of %Empty Latent Image.width% om waarden van nodes in te voegen. |

### Uitvoeren

| Naam | Type | Beschrijving |
| --- | --- | --- |
| `image` | `IMAGE` | De gedecodeerde afbeelding. |

