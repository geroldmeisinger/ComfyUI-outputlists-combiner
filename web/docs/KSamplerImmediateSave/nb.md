## KSampler Umiddelbar Lagring

![KSampler Umiddelbar Lagring](KSamplerImmediateSave/KSamplerImmediateSave.png)

(ComfyUI workflow inkludert)

Node-utvidelse av standard `CheckpointLoader`, `KSampler`, `VAE Decode` og `Save Image` for å behandle som en enhet.
Dette er nyttig hvis du ønsker å lagre mellomliggende bilder for ruter umiddelbart.

*"En tilpasset KSampler bare for å lagre et bilde? Nå har jeg blitt den ting jeg søkte å ødelegge!"*

### Innputter

| Navn | Type | Beskrivelse |
| --- | --- | --- |
| `cpkt_name` | `COMBO` | Navnet på sjekkpunktmeldingen (modellen) som skal lastes. |
| `positive` | `STRING` | Betingelsen som beskriver attributtene du ønsker å inkludere i bildet. |
| `negative` | `STRING` | Betingelsen som beskriver attributtene du ønsker å ekskludere fra bildet. |
| `latent_image` | `LATENT` | Det latente bildet som skal de-noises. |
| `seed` | `INT` | Det tilfeldige fr sem brukes for å skape støy. |
| `steps` | `INT` | Antall trinn som brukes i de-noising prosessen. |
| `cfg` | `FLOAT` | Classifier-Free Guidance skala balanserer kreativitet og tilhengelighet til prompten. Høyere verdier resulterer i bilder som er mer lik prompten, men for høye verdier vil negativt påvirke kvaliteten. |
| `sampler_name` | `COMBO` | Algoritmen som brukes ved sampling, dette kan påvirke kvaliteten, hastigheten og stilen på den genererte outputen. |
| `scheduler` | `COMBO` | Scheduleren kontrollerer hvordan støy gradvis fjernes for å forme bildet. |
| `denoise` | `FLOAT` | Mengden de-noising som anvendes, lavere verdier vil bevare strukturen til det opprinnelige bildet og tillate image-to-image sampling. |
| `filename_prefix` | `STRING` | Prefikset for filen som skal lagres. Dette kan inkludere formatteringsinformasjon som %date:yyyy-MM-dd% eller %Empty Latent Image.width% for å inkludere verdier fra noder. |

### Utputter

| Navn | Type | Beskrivelse |
| --- | --- | --- |
| `image` | `IMAGE` | Det dekodete bildet. |

