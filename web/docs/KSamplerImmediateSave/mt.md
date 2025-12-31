## KSampler Immediate Save

![KSampler Immediate Save](KSamplerImmediateSave/KSamplerImmediateSave.png)

(ComfyUI workflow included)

Espansjoni tal-node ta’ default `CheckpointLoader`, `KSampler`, `VAE Decode` u `Save Image` biex jipproċessaw bħala waħda.
Din tista’ tkun utili jekk inti trid tissejvja l-images intermedji għal grids immedjatament.

*"KSampler custom biex tissejvja image? Issa nisa kien il-ħaġa li nisib biex nħassarha!"*

### Inputs

| Isem | Tip | Deskrizzjoni |
| --- | --- | --- |
| `cpkt_name` | `COMBO` | L-isem tal-checkpoint (model) li jibbraw. |
| `positive` | `STRING` | Il-conditioning li jiddeskrivi l-attributi li trid tinkludi f’l-image. |
| `negative` | `STRING` | Il-conditioning li jiddeskrivi l-attributi li trid tibdil minn l-image. |
| `latent_image` | `LATENT` | L-image latent li jibdul. |
| `seed` | `INT` | Il-seed random użat biex jibbraw il-noise. |
| `steps` | `INT` | In-numru ta’ passi użati f’l-proċess ta’ denoising. |
| `cfg` | `FLOAT` | L-scale ta’ Classifier-Free Guidance jbala kreattività u attiżjoni għall-prompt. Valori iktar kbir jirriżultaw f’images iktar qribi mal-prompt, iżda valori eżessivi jinħarġu l-ħal ta’ kwalità. |
| `sampler_name` | `COMBO` | L-algoritmu użat waħda t-taħżiż, din tista’ taffettwa l-ħal, il-velocità u l-istilu tal-output igenerat. |
| `scheduler` | `COMBO` | Is-scheduler jikkontrolla kif il-noise jinħarġu biex jibnu l-image. |
| `denoise` | `FLOAT` | L-ammont ta’ denoising applikat, valori iktar billi jibqgħu l-struktur tal-image inizjali li jippermettu t-taħżiż image to image. |
| `filename_prefix` | `STRING` | Il-prefix tal-fajl biex tissejvja. Din tista’ tinkludi informazzjoni ta’ formatting bħall-%date:yyyy-MM-dd% jew %Empty Latent Image.width% biex tinkludi valori minn nodi. |

### Outputs

| Isem | Tip | Deskrizzjoni |
| --- | --- | --- |
| `image` | `IMAGE` | L-image decode. |

