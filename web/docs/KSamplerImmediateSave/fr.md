## KSampler Immediate Save

![KSampler Immediate Save](KSamplerImmediateSave/KSamplerImmediateSave.png)

(Workflow ComfyUI inclus)

Extension du nœud par défaut `CheckpointLoader`, `KSampler`, `VAE Decode` et `Save Image` pour les traiter ensemble.
Cela est utile si vous souhaitez enregistrer les images intermédiaires pour les grilles immédiatement.

*"Un KSampler personnalisé juste pour enregistrer une image ? Maintenant, je suis devenu la chose que j'aspirais à détruire !"*

### Entrées

| Nom | Type | Description |
| --- | --- | --- |
| `cpkt_name` | `COMBO` | Le nom du checkpoint (modèle) à charger. |
| `positive` | `STRING` | La condition d'entrée décrivant les attributs que vous souhaitez inclure dans l'image. |
| `negative` | `STRING` | La condition d'entrée décrivant les attributs que vous souhaitez exclure de l'image. |
| `latent_image` | `LATENT` | L'image latente à débruitée. |
| `seed` | `INT` | La graine aléatoire utilisée pour créer le bruit. |
| `steps` | `INT` | Le nombre d'étapes utilisées dans le processus de débruitage. |
| `cfg` | `FLOAT` | L'échelle de guidance sans classifieur équilibre la créativité et l'adhérence à l'invite. Des valeurs plus élevées donnent des images correspondant davantage à l'invite, mais des valeurs trop élevées affecteront négativement la qualité. |
| `sampler_name` | `COMBO` | L'algorithme utilisé lors de l'échantillonnage, cela peut affecter la qualité, la vitesse et le style de la sortie générée. |
| `scheduler` | `COMBO` | Le planifieur contrôle la façon dont le bruit est progressivement supprimé pour former l'image. |
| `denoise` | `FLOAT` | La quantité de débruitage appliquée, les valeurs plus basses maintiennent la structure de l'image initiale permettant un échantillonnage image à image. |
| `filename_prefix` | `STRING` | Le préfixe du fichier à enregistrer. Cela peut inclure des informations de formatage telles que %date:yyyy-MM-dd% ou %Empty Latent Image.width% pour inclure des valeurs des nœuds. |

### Sorties

| Nom | Type | Description |
| --- | --- | --- |
| `image` | `IMAGE` | L'image décodée. |

