## KSampler Takojšnje Shrani

![KSampler Takojšnje Shrani](KSamplerImmediateSave/KSamplerImmediateSave.png)

(Vključen je ComfyUI workflow)

Razširitev privzetega `CheckpointLoader`, `KSampler`, `VAE Decode` in `Save Image` za obdelavo kot eno.
To je uporabno, če želite takoj shraniti vmesne slike za mreže.

*"Pritrdni KSampler samo za shranjevanje slike? Sedaj sem postal to, kar sem hotel uničiti!"*

### Vhodi

| Ime | Vrsta | Opis |
| --- | --- | --- |
| `cpkt_name` | `COMBO` | Ime preverjalne točke (modela) za nalaganje. |
| `positive` | `STRING` | Pogoj, ki opisuje lastnosti, ki jih želite vključiti v sliko. |
| `negative` | `STRING` | Pogoj, ki opisuje lastnosti, ki jih želite izključiti iz slike. |
| `latent_image` | `LATENT` | Latentna slika za odščetljanje. |
| `seed` | `INT` | Naključni semeni, uporabljeno za ustvarjanje šuma. |
| `steps` | `INT` | Število korakov, uporabljenih v postopku odščetljanja. |
| `cfg` | `FLOAT` | Merilo Classifier-Free Guidance uravnava ustvarjalnost in spoštovanje do vprašanja. Višje vrednosti povzročijo slike, ki se bolj ujemajo z vprašanjem, vendar previsoke vrednosti negativno vplivajo na kakovost. |
| `sampler_name` | `COMBO` | Algoritem, uporabljen pri vzorčenju, to lahko vpliva na kakovost, hitrost in slog generiranega izhoda. |
| `scheduler` | `COMBO` | Planer nadzira, kako se šum postopoma odstranjuje za oblikovanje slike. |
| `denoise` | `FLOAT` | Količina odščetljanja, ki se uporablja, nižje vrednosti ohranijo strukturo začetne slike, kar omogoča vzorčenje slike v sliko. |
| `filename_prefix` | `STRING` | Predpona datoteke za shranjevanje. To lahko vključuje informacije o formatiranju, kot so %date:yyyy-MM-dd% ali %Empty Latent Image.width%, da vključi vrednosti iz vozlišč. |

### Izpisi

| Ime | Vrsta | Opis |
| --- | --- | --- |
| `image` | `IMAGE` | Dekodirana slika. |

