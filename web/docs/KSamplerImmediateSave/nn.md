## KSampler umiddelbar lagring

![KSampler Immediate Save](KSamplerImmediateSave/KSamplerImmediateSave.png)

(ComfyUI workflow inkludert)

Node-utvidelse av standard `CheckpointLoader`, `KSampler`, `VAE Decode` og `Save Image` for å prosessere som ein.
Dette er nyttig dersom du vil lagre mellomliggjande bilete for rutenett umiddelbart.

*"Ein tilpassa KSampler berre for å lagre eit bilete? No har eg blitt det same som eg søkte å ødelegge!"*

### Input

| Namn | Type | Skildring |
| --- | --- | --- |
| `cpkt_name` | `COMBO` | Namnet på sjekkpunktmålet (modellen) som skal lastas. |
| `positive` | `STRING` | Vilkåret som skildrar eigenskapane du vil inkludere i biletet. |
| `negative` | `STRING` | Vilkåret som skildrar eigenskapane du vil ekskludere frå biletet. |
| `latent_image` | `LATENT` | Det latente biletet som skal de-noises. |
| `seed` | `INT` | Det tilfeldige sema som vert brukt for å lage støy. |
| `steps` | `INT` | Talet på steg som vert brukt i de-noising prosessen. |
| `cfg` | `FLOAT` | Classifier-Free Guidance skala balanserer kreativitet og tilhøve til prompten. Høyare verdiar fører til bilete som er meir tilpassa prompten, men for høge verdiar vil negativt påverke kvaliteten. |
| `sampler_name` | `COMBO` | Algoritmen som vert brukt ved sampling, dette kan påvirke kvaliteten, farta og stilen til den genererte outputen. |
| `scheduler` | `COMBO` | Scheduleren kontrollerer korleis støy gradvis fjernast for å danne biletet. |
| `denoise` | `FLOAT` | Mengda av de-noising som vert brukt, lågare verdiar vil halde strukturen til det opphavlege biletet og tillèt for image-to-image sampling. |
| `filename_prefix` | `STRING` | Prefikset for fila som skal lagrast. Dette kan inkludere formateringsinformasjon som %date:yyyy-MM-dd% eller %Empty Latent Image.width% for å inkludere verdiane frå noder. |

### Output

| Namn | Type | Skildring |
| --- | --- | --- |
| `image` | `IMAGE` | Det dekodete biletet. |

