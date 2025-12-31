## KSampler Ar Gwblhau

![KSampler Ar Gwblhau](KSamplerImmediateSave/KSamplerImmediateSave.png)

(Cyflun ComfyUI wedi'i gynnwys)

Estyniad nod o'r `CheckpointLoader`, `KSampler`, `VAE Decode` a `Save Image` arferol i brosesu fel un.
Mae hwn yn ddefnyddiol os ydych chi am arbed delweddau canolbwynt ar gyfer gridiau ar unwaith.

*"Nod custom KSampler i arbed delwedd? Nawr rwy'n fod yn y peth a roeddi'n chwilio i'w ddynhau!"*

### Mewnbwn

| Enw | Math | Disgrifiad |
| --- | --- | --- |
| `cpkt_name` | `COMBO` | Enw'r sylfaen (model) i'w llwytho. |
| `positive` | `STRING` | Y condition yn ystyried y priodweddau y dymunwch eu cynnwys yn y delwedd. |
| `negative` | `STRING` | Y condition yn ystyried y priodweddau y dymunwch eu hepgor oddi ar y delwedd. |
| `latent_image` | `LATENT` | Y delwedd llwydd i'w ddynhau. |
| `seed` | `INT` | Y sêr ar hap a ddefnyddir ar gyfer creu'r gwynt. |
| `steps` | `INT` | Nifer y camau a ddefnyddir yn y proses o dynhau. |
| `cfg` | `FLOAT` | Y skala Guidance heb Classifer yn cyfathrebu creu a dilyn y argymhell. Gwerthoedd uchelach yn creu delweddau yn agosach i'r argymhell ond gallai gwerthoedd rhy uchel afalwch ddynhau'r ansawdd. |
| `sampler_name` | `COMBO` | Y algorythm a ddefnyddir wrth samplio, gall hwn a effectu ansawdd, cyflymder a arddull y allbwn a gynhyrchir. |
| `scheduler` | `COMBO` | Y scheduler yn rheoli sut mae'r gwynt yn cael ei dileu yn ymyl i greu'r delwedd. |
| `denoise` | `FLOAT` | Y nifer o dynhau a ddefnyddir, gwerthoedd isled byddai'n cadw strwythur y delwedd gwreiniedig gan ganiatáu samplio delwedd i delwedd. |
| `filename_prefix` | `STRING` | Y rhagddynodiad ar gyfer y ffeil i'w arbed. Gall hwn gynnwys gwybodaeth fformatio fel %date :yyyy-MM-dd% neu %Empty Latent Image.width% i gynnwys gwerthoedd o nodau. |

### Allbwn

| Enw | Math | Disgrifiad |
| --- | --- | --- |
| `image` | `IMAGE` | Y delwedd a ddiffinir. |

