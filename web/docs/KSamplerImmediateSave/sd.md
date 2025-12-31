## KSampler Immediate Save

![KSampler Immediate Save](KSamplerImmediateSave/KSamplerImmediateSave.png)

(ComfyUI workflow شامل آهي)

默认 `CheckpointLoader`، `KSampler`، `VAE Decode` تے `Save Image` جو نوڊون جو ڳنڍو ۾ چلائي ٿي ٿي. اهو چڱو ٿي ٿو جيڪڏانهن توهان گرڊ لاءِ مداخلت چاھيو ٿا.

*"اِس چار چوٽ ۾ تصوِر ڍاٽي چاھيو ٿا؟ اهڙو ٿي ويا چاھيو ٿا!"*

### ان پوٽس

| نالو | قسم | وضاحت |
| --- | --- | --- |
| `cpkt_name` | `COMBO` | چاک ڤوائنٽ ( môdel ) جو نالو جو لوڊ ٿي ٿو. |
| `positive` | `STRING` | چونڊ جو وضاحت ڪري ٿو جيڪي خاصيتون توهان تصوِر ۾ شامل ڪرڻ چاھيو ٿا. |
| `negative` | `STRING` | چونڊ جو وضاحت ڪري ٿو جيڪي خاصيتون توهان تصوِر مان ٻاهر ڪرڻ چاھيو ٿا. |
| `latent_image` | `LATENT` | چوٽ چاھي ٿا. |
| `seed` | `INT` | گھٽ چوٽ چاھي ٿا. |
| `steps` | `INT` | چوٽ چاھي ٿا. |
| `cfg` | `FLOAT` | چوٽ چاھي ٿا. |
| `sampler_name` | `COMBO` | چوٽ چاھي ٿا. |
| `scheduler` | `COMBO` | چوٽ چاھي ٿا. |
| `denoise` | `FLOAT` | چوٽ چاھي ٿا. |
| `filename_prefix` | `STRING` | چوٽ چاھي ٿا. |

### آوٽ پوٽس

| نالو | قسم | وضاحت |
| --- | --- | --- |
| `image` | `IMAGE` | چوٽ چاھي ٿا. |

