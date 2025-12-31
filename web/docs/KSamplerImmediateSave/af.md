## KSampler Onmiddellik Stoor

![KSampler Onmiddellik Stoor](KSamplerImmediateSave/KSamplerImmediateSave.png)

(ComfyUI workflow ingesluit)

Node uitbreiding van verstek `CheckpointLoader`, `KSampler`, `VAE Decode` en `Save Image` om as een te verwerk.
Dit is nuttig as jy wil om die tussenbeeld te stoor vir roosters onmiddellik.

*"'n Aangepaste KSampler net om 'n beeld te stoor? Nou het ek die very thing geword wat ek probeer vernietig!"*

### Invoere

| Naam | Tipe | Beskrywing |
| --- | --- | --- |
| `cpkt_name` | `COMBO` | Die naam van die checkpoint (model) om te laai. |
| `positive` | `STRING` | Die voorwaarde wat die eienskappe beskryf wat jy in die beeld wil insluit. |
| `negative` | `STRING` | Die voorwaarde wat die eienskappe beskryf wat jy uit die beeld wil uitsluit. |
| `latent_image` | `LATENT` | Die latent beeld om te de-noise. |
| `seed` | `INT` | Die ewekansige zaad wat gebruik word vir die skep van die geraas. |
| `steps` | `INT` | Die aantal stappe wat gebruik word in die de-noising proses. |
| `cfg` | `FLOAT` | Die Classifier-Free Guidance skaal balanseer kreatiwiteit en gehoorsaamheid aan die prompt. Hoër waardes resulteer in beelde wat meer naby die prompt pas, maar te hoge waardes sal negatief die kwaliteit beïnvloed. |
| `sampler_name` | `COMBO` | Die algoritme wat gebruik word tydens steekproeving, dit kan die kwaliteit, spoed en styl van die gegenereerde uitvoer beïnvloed. |
| `scheduler` | `COMBO` | Die scheduler beheer hoe geraas geleidelik verwyder word om die beeld te vorm. |
| `denoise` | `FLOAT` | Die hoeveelheid de-noising wat toegepas word, lagere waardes sal die struktuur van die oorspronklike beeld behou wat toelaat vir beeld-tot-beeld steekproeving. |
| `filename_prefix` | `STRING` | Die voorvoegsel vir die lêer om te stoor. Hierdie mag formatteringsinligting insluit soos %date:yyyy-MM-dd% of %Empty Latent Image.width% om waardes van nodes in te sluit. |

### Uitvoere

| Naam | Tipe | Beskrywing |
| --- | --- | --- |
| `image` | `IMAGE` | Die gedekodeerde beeld. |

