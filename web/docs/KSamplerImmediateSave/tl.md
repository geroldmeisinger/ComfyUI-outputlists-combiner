## KSampler Immediate Save

![KSampler Immediate Save](KSamplerImmediateSave/KSamplerImmediateSave.png)

(ComfyUI workflow included)

Ang pagpapalawak ng node ng default na `CheckpointLoader`, `KSampler`, `VAE Decode` at `Save Image` upang isagawa ang lahat ng isang proseso.
Ginagamit ito kung gusto mong i-save ang mga intermediate na imahe para sa grids agad.

*"Isang custom KSampler lang para i-save ang imahe? Ngayon ako ang naging bagay na sinubukan kong mapawi!"*

### Mga Input

| Pangalan | Uri | Paglalarawan |
| --- | --- | --- |
| `cpkt_name` | `COMBO` | Ang pangalan ng checkpoint (model) na i-load. |
| `positive` | `STRING` | Ang conditioning na naglalarawan ng mga katangian na nais mong isama sa imahe. |
| `negative` | `STRING` | Ang conditioning na naglalarawan ng mga katangian na nais mong i-exclude mula sa imahe. |
| `latent_image` | `LATENT` | Ang latent na imahe na i-denoise. |
| `seed` | `INT` | Ang random seed na ginagamit sa paglikha ng noise. |
| `steps` | `INT` | Ang bilang ng mga hakbang na ginamit sa proseso ng denoising. |
| `cfg` | `FLOAT` | Ang Classifier-Free Guidance scale na nagbabalansya ng kreatibidad at pagsunod sa prompt. Mas mataas na mga value ay magreresulta sa mga imahe na mas nakakatugma sa prompt ngunit ang masyadong mataas na value ay makakasira sa kalidad. |
| `sampler_name` | `COMBO` | Ang algorithm na ginagamit sa pag-sampling, maaaring mag-apekto ito sa kalidad, bilis, at istilo ng nabuong output. |
| `scheduler` | `COMBO` | Ang scheduler ay kontrolin kung paano tinatanggal ang noise upang mabuo ang imahe. |
| `denoise` | `FLOAT` | Ang dami ng denoising na iniiapply, mas mababang mga value ay patuloy na magpapakita ng estructura ng orihinal na imahe, na nagpapahintulot sa image to image sampling. |
| `filename_prefix` | `STRING` | Ang prefix ng file na i-save. Maaari itong maglaman ng impormasyon sa formatting tulad ng %date:yyyy-MM-dd% o %Empty Latent Image.width% upang isama ang mga value mula sa mga node. |

### Mga Output

| Pangalan | Uri | Paglalarawan |
| --- | --- | --- |
| `image` | `IMAGE` | Ang decoded na imahe. |

