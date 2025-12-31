## KSampler Immediate Save

![KSampler Immediate Save](KSamplerImmediateSave/KSamplerImmediateSave.png)

(ComfyUI workflow inclòcha)

Expansión del nòd per defaut `CheckpointLoader`, `KSampler`, `VAE Decode` e `Save Image` per los processar d'un còp.
Aquò es útil se volètz enregistrar las imatges intermediàrias per las grilhas immediatament.

*"Un KSampler personalizat unicament per enregistrar una imatge ? Ara mei son devenut lo que odiava !*

### Entradas

| Nom | Tipe | Descripcion |
| --- | --- | --- |
| `cpkt_name` | `COMBO` | Lo nom del punt de control (modèl) de cargar. |
| `positive` | `STRING` | La condicion que descriu las atributs que volètz inclure dins l'imatge. |
| `negative` | `STRING` | La condicion que descriu las atributs que volètz exclure de l'imatge. |
| `latent_image` | `LATENT` | L'imatge latent de desorinar. |
| `seed` | `INT` | La variabla aleatòria utilizada per crear lo soroll. |
| `steps` | `INT` | Lo nombre d'etas utilizadas dins lo processus de desorinar. |
| `cfg` | `FLOAT` | L'escala de guida lliura de classificador equilibra la creativitat e l'acòrd amb l'indicacion. De valors mai nautas donan d'imatges mai pro a l'indicacion, mas de valors tròp nautas an un impacte negatiu sus la qualitat. |
| `sampler_name` | `COMBO` | L'algoritme utilizat quand s'ensampa, aquò pòt afectar la qualitat, la velocitat e l'estil de la sortida generada. |
| `scheduler` | `COMBO` | Lo programador controla com lo soroll es tirat progressivament per formar l'imatge. |
| `denoise` | `FLOAT` | La quantitat de desorinar aplicada, de valors mai bassas mantenen l'estructura de l'imatge inicial, permetent l'ensampelatge imatge a imatge. |
| `filename_prefix` | `STRING` | Lo prefix pel fichièr de salvar. Aquò pòt inclure d'informacions de formatatge coma %date :yyyy-MM-dd% o %Empty Latent Image.width% per inclure de valors dels nòds. |

### Sortidas

| Nom | Tipe | Descripcion |
| --- | --- | --- |
| `image` | `IMAGE` | L'imatge descrich. |

