## KSampler Immediate Save

![KSampler Immediate Save](KSamplerImmediateSave/KSamplerImmediateSave.png)

(ComfyUI workflow d'ofgesech)

Node-Erweidung vum Standard `CheckpointLoader`, `KSampler`, `VAE Decode` an `Save Image`, fir als een ze verarbechten.
Dëst ass nützlech, wann Dir d'Mezzelaubilder fir Grids direkt späichere wëllt.

*"E benotzerdefinéierten KSampler fir e Bild ze späicheren? E loch, ech sinn elo de Sack, dech, deen ech gesicht hunn, ze zerstéieren!"*

### Input

| Numm | Typ | Beschreiwung |
| --- | --- | --- |
| `cpkt_name` | `COMBO` | De Numm vum Checkpoint (Model), deen gelueden gëtt. |
| `positive` | `STRING` | D'Conditioning, déi d'Attributer beschreift, déi Dir an d'Bild wëllt opnehmen. |
| `negative` | `STRING` | D'Conditioning, déi d'Attributer beschreift, déi vum Bild auszehalen sinn. |
| `latent_image` | `LATENT` | D'Latent Bild, deen z'entrauscht gëtt. |
| `seed` | `INT` | De zufalleg Seed, de fir d'Erstellung vun der Rausch benotzt gëtt. |
| `steps` | `INT` | D'Zuel vun den Schrëtt, déi an der Entroeschungsprozess benotzt ginn. |
| `cfg` | `FLOAT` | D'Classifier-Free Guidance-Skala balancéiert Kreativitéit a Eegesinnung mat der Aufforderung. Héchere Wäerter resultéieren an Bild, déi méi d'Prompt entspriechen, awer zu héch Wäerter wärend negativ op d'Qualitéit. |
| `sampler_name` | `COMBO` | D'Algorithmus, de benotzt gëtt, wann esoult, dës ka d'Qualitéit, d'Geschwindegkeet an d'Styl vun der generéierte Ausgab änneren. |
| `scheduler` | `COMBO` | D'Scheduler kontrolléiert, wéi Rausch all moment z'entfernen, fir d'Bild ze forméieren. |
| `denoise` | `FLOAT` | D'Zuel vun der Entroeschung, déi ugesat gëtt, méi niddereg Wäerter wärend d'Struktur vum initialem Bild behalen, wéi fir d'Bild-zu-Bild Sampling erlaaben. |
| `filename_prefix` | `STRING` | De Prefix fir d'Datei, déi gespäichert gëtt. Dës ka Formatéierungsinfo wéi %date:yyyy-MM-dd% oder %Empty Latent Image.width% enthalen, fir Wäerter aus Nodes ze benotzen. |

### Output

| Numm | Typ | Beschreiwung |
| --- | --- | --- |
| `image` | `IMAGE` | D'entcodeert Bild. |

