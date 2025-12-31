## KSampler Immediate Save

![KSampler Immediate Save](KSamplerImmediateSave/KSamplerImmediateSave.png)

(ComfyUI workflow ap gen yon pwogrè)

Epanwis nòd default `CheckpointLoader`, `KSampler`, `VAE Decode` ak `Save Image` pou pwosese kòm yon sèl.
Sa utile si ou vle sove imaj mwayen pou gril imedyatman.

*"Yon KSampler ki sèlman pou sove yon imaj? Moun m se moun ki m ap chache detwouye!"*

### Antre yo

| Non | Tip | Deskrisyon |
| --- | --- | --- |
| `cpkt_name` | `COMBO` | Non checkpoint (modèl) pou chaje. |
| `positive` | `CHENN` | Kondisyon ki dekri atribi ou vle ajoute nan imaj la. |
| `negative` | `CHENN` | Kondisyon ki dekri atribi ou vle ekskliziv nan imaj la. |
| `latent_image` | `LATENT` | Imaj latent pou denoize. |
| `seed` | `ENTYE` | Seed aléatwa itilize pou kreye nwa a. |
| `steps` | `ENTYE` | Kantite etap itilize nan pwosedi denoize a. |
| `cfg` | `FLOTAN` | Echel Classifier-Free Guidance ki balanse kreativite ak fidèlite a ak prompt la. Valè ki pi enpotan pral fè imaj yo pi klè ki matche ak prompt la toutan, men valè ki twò enpotan pral afekte kalite a negativman. |
| `sampler_name` | `COMBO` | Algorit m itilize nan echantillonaj la, sa ka afekte kalite a, vitès la, ak stil la nan sòti a. |
| `scheduler` | `COMBO` | Scheduler la kontwol kòm nwa a retire progresifman pou fè imaj la. |
| `denoise` | `FLOTAN` | Kantite denoize itilize, valè ki pi ba pral kenbe strykti imaj la, ki pèmèt echantillonaj imaj nan imaj. |
| `filename_prefix` | `CHENN` | Prefiks fichye a pou sove. Sa ka gen enfòmasyon fòmat ki gen %date :yyyy-MM-dd% oswa %Empty Latent Image.width% pou adjwoute valè sòti nan nòd yo. |

### Sòti yo

| Non | Tip | Deskrisyon |
| --- | --- | --- |
| `image` | `IMAGE` | Imaj dekòde a. |

