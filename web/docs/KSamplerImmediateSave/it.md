## KSampler Salvataggio Immediato

![KSampler Salvataggio Immediato](KSamplerImmediateSave/KSamplerImmediateSave.png)

(ComfyUI workflow incluso)

Espansione del nodo predefinito `CheckpointLoader`, `KSampler`, `VAE Decode` e `Save Image` per elaborarli come uno solo.
Questo è utile se vuoi salvare immediatamente le immagini intermedie per le griglie.

*"Un KSampler personalizzato solo per salvare un'immagine? Ora sono diventato la cosa che cercavo di distruggere!"*

### Input

| Nome | Tipo | Descrizione |
| --- | --- | --- |
| `cpkt_name` | `COMBO` | Il nome del checkpoint (modello) da caricare. |
| `positive` | `STRINGA` | La condizione che descrive gli attributi che vuoi includere nell'immagine. |
| `negative` | `STRINGA` | La condizione che descrive gli attributi che vuoi escludere dall'immagine. |
| `latent_image` | `LATENT` | L'immagine latente da disfare. |
| `seed` | `INTERO` | Il seme casuale utilizzato per creare il rumore. |
| `steps` | `INTERO` | Il numero di passi utilizzati nel processo di disfacimento. |
| `cfg` | `VIRGOLA_MOBILE` | La scala di Guida Senza Classificatore bilancia creatività e aderenza al prompt. Valori più alti producono immagini più fedeli al prompt, ma valori troppo alti possono influire negativamente sulla qualità. |
| `sampler_name` | `COMBO` | L'algoritmo utilizzato durante il campionamento, questo può influenzare la qualità, la velocità e lo stile dell'output generato. |
| `scheduler` | `COMBO` | Il pianificatore controlla come il rumore viene gradualmente rimosso per formare l'immagine. |
| `denoise` | `VIRGOLA_MOBILE` | L'ammontare di disfacimento applicato, valori più bassi manterranno la struttura dell'immagine iniziale consentendo il campionamento da immagine a immagine. |
| `filename_prefix` | `STRINGA` | Il prefisso per il file da salvare. Questo può includere informazioni di formattazione come %date:yyyy-MM-dd% o %Empty Latent Image.width% per includere valori dai nodi. |

### Output

| Nome | Tipo | Descrizione |
| --- | --- | --- |
| `image` | `IMAGE` | L'immagine decodificata. |

