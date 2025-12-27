## KSampler Immediate Save

![KSampler Immediate Save](KSamplerImmediateSave/KSamplerImmediateSave.png)

(ComfyUI workflow included)

Node expansion of default `CheckpointLoader`, `KSampler`, `VAE Decode` and `Save Image` to process as one.
This is useful if you want to save the intermediate images for grids immediately.

*"A custom KSampler just to save an image? Now I have become the very thing I sought to destroy!"*

### Inputs

| Name | Type | Description |
| --- | --- | --- |
| `cpkt_name` | `COMBO` | The name of the checkpoint (model) to load. |
| `positive` | `STRING` | The conditioning describing the attributes you want to include in the image. |
| `negative` | `STRING` | The conditioning describing the attributes you want to exclude from the image. |
| `latent_image` | `LATENT` | The latent image to denoise. |
| `seed` | `INT` | The random seed used for creating the noise. |
| `steps` | `INT` | The number of steps used in the denoising process. |
| `cfg` | `FLOAT` | The Classifier-Free Guidance scale balances creativity and adherence to the prompt. Higher values result in images more closely matching the prompt however too high values will negatively impact quality. |
| `sampler_name` | `COMBO` | The algorithm used when sampling , this can affect the quality , speed , and style of the generated output. |
| `scheduler` | `COMBO` | The scheduler controls how noise is gradually removed to form the image. |
| `denoise` | `FLOAT` | The amount of denoising applied , lower values will maintain the structure of the initial image allowing for image to image sampling. |
| `filename_prefix` | `STRING` | The prefix for the file to save. This may include formatting information such as %date :yyyy-MM-dd% or %Empty Latent Image.width% to include values from nodes. |

### Outputs

| Name | Type | Description |
| --- | --- | --- |
| `image` | `IMAGE` | The decoded image. |
