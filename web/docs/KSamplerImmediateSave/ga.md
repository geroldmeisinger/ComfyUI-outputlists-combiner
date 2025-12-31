## KSampler Sábháil Inmheánach

![KSampler Sábháil Inmheánach](KSamplerImmediateSave/KSamplerImmediateSave.png)

(ComfyUI workflow san áireamh)

Leathnú nód de réamhshocraithe `CheckpointLoader`, `KSampler`, `VAE Decode` agus `Save Image` chun iarratas a dhéanamh mar aon. 
Tá sé seo úsáideach má tá ag teastáil uait imeacht a shábháil i gcuid imeachtaí le haghaidh gridí.

*"An nód KSampler saincheaptha chun íomhá a shábháil? Anois táim in ann an rud a chuardaigh mé a chur i bhfolach!"*

### Ionchuir

| Ainm | Cineál | Cur Síos |
| --- | --- | --- |
| `cpkt_name` | `COMBO` | Ainm an checkpoint (módail) le lódáil. |
| `positive` | `STRING` | An t-eolas a chomhroinnte a thagann leis na tréithe atá le cur isteach sa híomhá. |
| `negative` | `STRING` | An t-eolas a chomhroinnte a thagann leis na tréithe atá le cur amach as an íomhá. |
| `latent_image` | `LATENT` | An íomhá latenta le dí-athrú. |
| `seed` | `INT` | An sionad randamach a úsáidtear chun an nua-acht a chruthú. |
| `steps` | `INT` | An t-uimhir de chéimeanna a úsáidtear i gcónaíocht an dí-athrú. |
| `cfg` | `FLOAT` | An scála a chomhroinnte ag an bhFoghlaim Gan Chlasair, balansaíonn sé idir cruthaitheacht agus comhoiriúnacht leis an gceist. Níos airde na luachanna, níos gaire an íomhá a chomhroinnte leis an gceist, ach níos airde ná go maith will impeactáil de ghnáth. |
| `sampler_name` | `COMBO` | An algartim a úsáidtear nuair a bhailíonn, is féidir leis an gceann a thiontú ar chualaithe, gasta agus stíl an t-aschuir a chruthú. |
| `scheduler` | `COMBO` | An t-earrachaire a rialaíonn conas a bhaintear nua-acht go díreach chun an íomhá a chruthú. |
| `denoise` | `FLOAT` | An t-amount dí-athruithe a chuirtear i bhfeidhm, níos ísle na luachanna, níos mó struchtúr an íomhá tosaigh a choinneáil, ceadaíonn seo sampla íomhá go íomhá. |
| `filename_prefix` | `STRING` | An réimír don chomhad a shábháil. Is féidir leis an réimír sonraí formáidithe a bheith ann cosúil le %date :yyyy-MM-dd% nó %Empty Latent Image.width% chun luachanna a chur isteach ó nód. |

### Aschuir

| Ainm | Cineál | Cur Síos |
| --- | --- | --- |
| `image` | `IMAGE` | An íomhá dí-ghlasaithe. |

