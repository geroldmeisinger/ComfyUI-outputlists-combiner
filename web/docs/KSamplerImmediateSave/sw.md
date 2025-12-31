## KSampler Kusave Kwa Haraka

![KSampler Immediate Save](KSamplerImmediateSave/KSamplerImmediateSave.png)

(ComfyUI workflow imejengwa)

Kuenea kwa node ya chaguo-msingi `CheckpointLoader`, `KSampler`, `VAE Decode` na `Save Image` ili kufanya kazi kama moja.
Hii inapatikana ikiwa unataka kuhifadhi picha za intermedi za gridi mara moja.

*"KSampler chaguo-msingi tu ili kuhifadhi picha? Sasa nimekuwa jinsi nilivyokuwa nikipigana naye!"*

### Ingizo

| Jina | Aina | Maelezo |
| --- | --- | --- |
| `cpkt_name` | `COMBO` | Jina la checkpoint (model) iliyojazwa. |
| `positive` | `STRING` | Maelezo ya maelezo ya mbinu ambayo unataka kuwekwa katika picha. |
| `negative` | `STRING` | Maelezo ya maelezo ya mbinu ambayo unataka kuondoa kutoka kwenye picha. |
| `latent_image` | `LATENT` | Picha ya latent iliyoondolewa. |
| `seed` | `INT` | Seed ya kibinu kinachotumiwa kuzalisha kibinu. |
| `steps` | `INT` | Idadi ya hatua zilizotumiwa katika mchakato wa kusafisha. |
| `cfg` | `FLOAT` | Skeli ya Ushirikiano wa Kujifunza Kwa Mbinu inakubali kwa kujifunza na kufuata maagizo. Thamani za juu zinatoa picha zinazofanana zaidi na maagizo lakini thamani za kubwa zinaweza kuharibu ubora. |
| `sampler_name` | `COMBO` | Algorithmi inayotumiwa wakati wa kusamamba, hii inaweza kubadilisha ubora, kasi na mtindo wa matokeo yaliyozalishwa. |
| `scheduler` | `COMBO` | Mchakato unaoeleza jinsi kibinu kinavyopoteza kwa muda ili kuunda picha. |
| `denoise` | `FLOAT` | Idadi ya kusafisha kinachotumiwa, thamani za chini zinazokubali mtiririko wa picha ya awali ili kufanya kusamamba kwa picha kwa picha. |
| `filename_prefix` | `STRING` | Kichwa cha jina la faili iliyo hifadhiwa. Hii inaweza kuwa na maelezo ya uundaji kama %date:yyyy-MM-dd% au %Empty Latent Image.width% ili kuweka thamani kutoka kwa node. |

### Pato

| Jina | Aina | Maelezo |
| --- | --- | --- |
| `image` | `IMAGE` | Picha iliyosafishwa. |

