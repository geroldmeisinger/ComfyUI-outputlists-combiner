## KSampler strax goym

![KSampler strax goym](KSamplerImmediateSave/KSamplerImmediateSave.png)

(ComfyUI workflow íðgu)

Node útvíkkjan av standard `CheckpointLoader`, `KSampler`, `VAE Decode` og `Save Image` til at vinna sum ein.
Hetta er nýtugt um tú ynskir at goyma millumbilarsmyglingar fyri gridsum strax.

*"Ein sertila KSampler bara til at goyma einn mynd? Nú er eg orðinn til, ið eg var at leita at øðla!"*

### Inntak

| Navn | Slag | Lýsing |
| --- | --- | --- |
| `cpkt_name` | `COMBO` | Navn á checkpoint (model) at henda. |
| `positive` | `STRING` | Vilkurin, ið lýsir eigindi, ið tú ynskir at inklúdera í myndini. |
| `negative` | `STRING` | Vilkurin, ið lýsir eigindi, ið tú ynskir at útsløða frá myndini. |
| `latent_image` | `LATENT` | Latent myndin at tøkna. |
| `seed` | `INT` | Sleppt talan brúkt til at gerða støddina. |
| `steps` | `INT` | Tal av skrefum brúkt í tøkningin. |
| `cfg` | `FLOAT` | Classifier-Free Guidance skala, ið balansirir skapleiki og fasthald við prompt. Høgri víldi gefa myndir, ið passa nær prompt, umtú høgri víldi verður negativt ávirkandi á gøgn. |
| `sampler_name` | `COMBO` | Algoritman brúkt við sampling, hetta kann hava ávirkning á gøgn, hastir og tíð. |
| `scheduler` | `COMBO` | Schedulerin kontrollerar hvussu støddin gradvíslega tekur burtur til at mynda myndina. |
| `denoise` | `FLOAT` | Mengi av tøkningin, lægri víldi vil halda strukturini í upphavleika myndini, sum létur fyri image to image sampling. |
| `filename_prefix` | `STRING` | Prefix fyri filin at goyma. Hetta kann inklúdera formateringsupplýsingar sum %date :yyyy-MM-dd% ella %Empty Latent Image.width% til at inklúdera víldi frá nodes. |

### Úttak

| Navn | Slag | Lýsing |
| --- | --- | --- |
| `image` | `IMAGE` | Dýpt myndin. |

