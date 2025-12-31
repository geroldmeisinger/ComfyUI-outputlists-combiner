## KSampler nedelsiant išsaugoti

![KSampler nedelsiant išsaugoti](KSamplerImmediateSave/KSamplerImmediateSave.png)

(ComfyUI darbo eiga įtraukta)

Numatytojo `CheckpointLoader`, `KSampler`, `VAE Decode` ir `Save Image` mazgų plėtra, kad apdorotumėte kaip vieną.
Tai naudinga, jei norite nedelsiant išsaugoti tarpines vaizdų tinkleliams.

*"Papildomas KSampler tik vaizdui išsaugoti? Dabar tapau tiksliąsia, kurią siekiau sunaikinti!"*

### Įvestys

| Pavadinimas | Tipas | Aprašymas |
| --- | --- | --- |
| `cpkt_name` | `COMBO` | Įkeliamo atsarginio (modelio) pavadinimas. |
| `positive` | `EILUTĖ` | Sąlyga, apibūdinanti atributus, kuriuos norite įtraukti į vaizdą. |
| `negative` | `EILUTĖ` | Sąlyga, apibūdinanti atributus, kuriuos norite išskirti iš vaizdo. |
| `latent_image` | `LATENT` | Latentinis vaizdas, kurį reikia išvalyti. |
| `seed` | `SVEIKAS` | Atsitiktinis pasėklas, naudojamas triukšmo kūrimui. |
| `steps` | `SVEIKAS` | Žingsnių skaičius, naudojamas išvalymo procese. |
| `cfg` | `DEŠIMTAINIS` | Classifier-Free Guidance skalė balansuoja kūrybiškumą ir vadovavimą promptui. Didesnės reikšmės leidžia gauti vaizdus, labiau atitinkančius promptą, tačiau per didelės reikšmės neigiamai paveiks kokybę. |
| `sampler_name` | `COMBO` | Algoritmas, naudojamas priešpakeitimo metu, gali paveikti generuoto išvesties kokybę, greitį ir stilių. |
| `scheduler` | `COMBO` | Planuotojas kontroliuoja, kaip lėtai pašalinamas triukšmas, kad sudarytų vaizdą. |
| `denoise` | `DEŠIMTAINIS` | Taikomas išvalymo kiekis, mažesnės reikšmės išlaiko pradinio vaizdo struktūrą, leidžiant vaizdų iš vaizdo priešpakeitimo. |
| `filename_prefix` | `EILUTĖ` | Failo priešdėlis, kurį išsaugoti. Gali įtraukti formatavimo informaciją, tokia kaip %date :yyyy-MM-dd% arba %Empty Latent Image.width%, kad įtrauktumėte reikšmes iš mazgų. |

### Išvestys

| Pavadinimas | Tipas | Aprašymas |
| --- | --- | --- |
| `vaizdas` | `VAIZDAS` | Iškoduotas vaizdas. |

