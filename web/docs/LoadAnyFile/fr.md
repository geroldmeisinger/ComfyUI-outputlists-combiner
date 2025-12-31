## Load Any File

![Load Any File](LoadAnyFile/LoadAnyFile.png)

(Workflow ComfyUI inclus)

Charge n'importe quel fichier texte ou binaire et fournit le contenu du fichier sous forme de chaîne ou de chaîne base64. De plus, essaie de le charger comme `IMAGE`. Et aussi, essaie de charger les métadonnées.

`filepath` prend en charge les chemins de fichiers annotés de ComfyUI `[input]` `[output]` ou `[temp]`.
`filepath` prend également en charge les expansions de motifs glob `sous_repertoire/**/*.png`.
Utilise internement python [glob.iglob](https://docs.python.org/3/library/glob.html#glob.iglob).

`metadata` appelle `exiftool`, s'il est installé et disponible dans `PATH`, sinon utilise `PIL.Image.info` comme solution de repli.

Pour des raisons de sécurité, seuls les répertoires suivants sont pris en charge : `[input] [output] [temp]`.
Pour des raisons de performance, le nombre de fichiers est limité à : 1024.

### Entrées

| Nom | Type | Description |
| --- | --- | --- |
| `filepath` | `STRING` | Le répertoire de base par défaut est le répertoire utilisateur `[input]`. Prend en charge l'expansion de motifs glob `sous_repertoire/**/*.png`. Utilise le suffixe ` [input]` ` [output]` ou ` [temp]` (attention à l'espace initial !) pour spécifier un répertoire utilisateur ComfyUI différent. |

### Sorties

| Nom | Type | Description |
| --- | --- | --- |
| `content` | `STRING 𝌠` | Contenu du fichier pour les fichiers texte, base64 pour les fichiers binaires. |
| `image` | `IMAGE 𝌠` | Tensor de lot d'images. |
| `mask` | `MASK 𝌠` | Tensor de lot de masques. |
| `metadata` | `STRING 𝌠` | Données Exif d'ExifTool. Nécessite que la commande `exiftool` soit disponible dans `PATH`. |

