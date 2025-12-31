## KSampler Immediate Save

![KSampler Immediate Save](KSamplerImmediateSave/KSamplerImmediateSave.png)

(ComfyUI workflow included)

Espansione de su nodu predefinidu `CheckpointLoader`, `KSampler`, `VAE Decode` e `Save Image` pro elaborare comente unu. Custu est útil si cheris sarvare s’immàgines intermedias pro gridas in manera immediata.

*"Unu KSampler personalizadu puru pro sarvare un’immàgine? Ora sunt istadu su thing chi cheria a destruire!"*

### Inputs

| Name | Type | Description |
| --- | --- | --- |
| `cpkt_name` | `COMBO` | Su nàmene de su checkpoint (modelu) de cargare. |
| `positive` | `STRING` | Sa conditzionale chi descrìbit sas attributos chi cheris inclùdere in s’immàgine. |
| `negative` | `STRING` | Sa conditzionale chi descrìbit sas attributos chi cheris iscludere dae s’immàgine. |
| `latent_image` | `LATENT` | S’immàgine latente de disfàghere. |
| `seed` | `INT` | Su seed casuale impreadu pro creare su ruìdu. |
| `steps` | `INT` | Su nùmeru de passos impreados in su protzessu de disfàghere. |
| `cfg` | `FLOAT` | Sa scala de Guida Libbada dae Classificadore (Classifier-Free Guidance) balanza creatività e s’adherèntzia a su prompt. Valores artusos at a prodùere immàgines prus istrintas a su prompt, ma valores tropu artusos ant a àere un’impatu negativu in sa qualità. |
| `sampler_name` | `COMBO` | S’algoritmu impreadu in sa campiòngia, custu podet àere un’impatu in sa qualità, sa velotzidade e s’estìlicu de s’òbbidu generadu. |
| `scheduler` | `COMBO` | Su scheduler controllat comente su ruìdu est retìtidu pro formare s’immàgine. |
| `denoise` | `FLOAT` | Sa quantidade de disfàghere apicada, valores bassos ant a mantènnere sa strutura de s’immàgine iniziale, permitende campiòngias image-to-image. |
| `filename_prefix` | `STRING` | Su prefìtzi de su file de sarvare. Custu podet inclùdere informatziones de formadu comente %date:yyyy-MM-dd% o %Empty Latent Image.width% pro inclùdere balores dae nodos. |

### Outputs

| Name | Type | Description |
| --- | --- | --- |
| `image` | `IMAGE` | S’immàgine decodificada. |

