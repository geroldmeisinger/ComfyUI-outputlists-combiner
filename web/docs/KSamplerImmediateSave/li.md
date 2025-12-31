## KSampler Immediate Save

![KSampler Immediate Save](KSamplerImmediateSave/KSamplerImmediateSave.png)

(ComfyUI workflow bijgevoegd)

Node uitbreiding um de standaard `CheckpointLoader`, `KSampler`, `VAE Decode` en `Save Image` te verwerke um ‘n keer.
Dit is nuttig es ge de tussentijdse beelde um grids wil opslèr.

*"E custom KSampler um e beelde te opslèr? Nu ben ik de zeef wat ik wilde verniel!"*

### Invoere

| Naom | Type | Beschrèving |
| --- | --- | --- |
| `cpkt_name` | `COMBO` | De naam um ‘t checkpoint (model) te laod. |
| `positive` | `STRING` | De conditioning wat de eigeschap beschrieft wat ge wil opnèl in ‘t beelde. |
| `negative` | `STRING` | De conditioning wat de eigeschap beschrieft wat ge wil uutnèl um ‘t beelde. |
| `latent_image` | `LATENT` | ‘t Latent beelde um te denoise. |
| `seed` | `INT` | De random seed gebrukt um ‘t noise te make. |
| `steps` | `INT` | ‘t Aantal stappe um ‘t denoising proces te doen. |
| `cfg` | `FLOAT` | De Classifier-Free Guidance schaal balanseert creativiteit en adherentie um ‘t prompt. Hogere waardes geven beelde wat dichter bij ‘t prompt ligge however te hoge waardes zulle de kwaliteit negatief beinvloed. |
| `sampler_name` | `COMBO` | ‘t Algoritme gebrukt um te sample, dit kan de kwaliteit, snelheid en stijl um ‘t gegenereerde resultaat beinvloed. |
| `scheduler` | `COMBO` | ‘t Scheduler beheurt hoe ‘t noise geleidelijk weggene um ‘t beelde te make. |
| `denoise` | `FLOAT` | ‘t Aantal denoising gebrukt, lagere waardes behoude de structuur um ‘t oorsprunkeleke beelde um image to image sampling toe te late. |
| `filename_prefix` | `STRING` | ‘t Prefix um ‘t bestand te opslèr. Dit kan formatteringsinformatie es %date:yyyy-MM-dd% of %Empty Latent Image.width% bevatte um waardes um nodes op te nèl. |

### Uitvoere

| Naom | Type | Beschrèving |
| --- | --- | --- |
| `image` | `IMAGE` | ‘t Gecodeerde beelde. |

