## KSampler Immediate Save

![KSampler Immediate Save](KSamplerImmediateSave/KSamplerImmediateSave.png)

(ComfyUI vinnusvæði included)

Node útvíkking standar `CheckpointLoader`, `KSampler`, `VAE Decode` og `Save Image` til að vinna sem eitt.
Þetta er gagnlegt ef þú vilt vista millibil myndirnar fyrir röðir strax.

*"Sérsniðinn KSampler bara til að vista mynd? Nú hef ég verið að verða það sem ég reyndi að eyða!"*

### Inntök

| Nafn | Gerð | Lýsing |
| --- | --- | --- |
| `cpkt_name` | `COMBO` | Nafn á checkpoint (model) sem á að hlaða inn. |
| `positive` | `STRING` | Skilyrðið sem lýsir eiginleikum sem þú vilt hafa í myndinni. |
| `negative` | `STRING` | Skilyrðið sem lýsir eiginleikum sem þú vilt sleppa í myndinni. |
| `latent_image` | `LATENT` | Latent myndin sem á að afhreinsa. |
| `seed` | `INT` | Slembitala sem notuð er til að búa til hörðu. |
| `steps` | `INT` | Fjöldi skrefa sem notaðir eru í afhreinsunarefni. |
| `cfg` | `FLOAT` | Classifier-Free Guidance skali sem jafnar sköpun og fylgiski við prompt. Hærri gildi leiða til mynda sem eru nálægt prompt en of hár gildi mun hafa negatíva áhrif á gæði. |
| `sampler_name` | `COMBO` | Algorithmi sem notaður er við sýnd, þetta getur áhrif á gæði, hraða og stíl á úttaki. |
| `scheduler` | `COMBO` | Skedulernur stýrir því hvernig hörð er að draga út til að búa til myndina. |
| `denoise` | `FLOAT` | Magn afhreinsunar sem notuð er, lægri gildi vilja halda uppbyggingu upphaflegrar myndar og leyfir mynd-til-mynd sýnd. |
| `filename_prefix` | `STRING` | Forskeytið fyrir skrána sem á að vista. Þetta getur innihaldið formunargögn eins og %date :yyyy-MM-dd% eða %Empty Latent Image.width% til að hafa með gildi frá node. |

### Úttök

| Nafn | Gerð | Lýsing |
| --- | --- | --- |
| `image` | `IMAGE` | Afkóðuð mynd. |

