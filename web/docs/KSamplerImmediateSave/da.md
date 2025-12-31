## KSampler øjeblikkelig gem

![KSampler øjeblikkelig gem](KSamplerImmediateSave/KSamplerImmediateSave.png)

(ComfyUI workflow inkluderet)

Node udvidelse af standard `CheckpointLoader`, `KSampler`, `VAE Decode` og `Save Image` til at behandle som en enhed.
Dette er nyttigt, hvis du vil gemme de mellemliggende billeder for gitter øjeblikkeligt.

*"En tilpasset KSampler bare for at gemme et billede? Nu er jeg blevet den ting, jeg søgte at ødelægge!"*

### Input

| Navn | Type | Beskrivelse |
| --- | --- | --- |
| `cpkt_name` | `COMBO` | Navnet på tjekpunktet (model) som skal indlæses. |
| `positive` | `STRENG` | Betingelsen som beskriver attributterne du vil inkludere i billedet. |
| `negative` | `STRENG` | Betingelsen som beskriver attributterne du vil ekskludere fra billedet. |
| `latent_image` | `LATENT` | Det latente billede som skal de-noises. |
| `seed` | `HELTAL` | Det tilfældige seed som bruges til at skabe støj. |
| `steps` | `HELTAL` | Antallet af trin som bruges i de-noising processen. |
| `cfg` | `FLYDENDE TAL` | Classifier-Free Guidance skalaen balancerer kreativitet og efterfølgelse af prompten. Højere værdier resulterer i billeder som matcher prompten tættere, men for høje værdier vil negativt påvirke kvaliteten. |
| `sampler_name` | `COMBO` | Algoritmen som bruges ved sampling, dette kan påvirke kvaliteten, hastigheden og stilen på den genererede output. |
| `scheduler` | `COMBO` | Scheduleren kontrollerer hvordan støj gradvist fjernes for at danne billedet. |
| `denoise` | `FLYDENDE TAL` | Mængden af de-noising anvendt, lavere værdier vil bevare strukturen i det oprindelige billede, hvilket tillader image-to-image sampling. |
| `filename_prefix` | `STRENG` | Prefixet for filen som skal gemmes. Dette kan inkludere formatteringsinformation såsom %date:yyyy-MM-dd% eller %Empty Latent Image.width% for at inkludere værdier fra noder. |

### Output

| Navn | Type | Beskrivelse |
| --- | --- | --- |
| `image` | `BILLEDE` | Det afkodede billede. |

