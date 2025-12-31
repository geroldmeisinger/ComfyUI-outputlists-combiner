## XYZ-GridPlot

![XYZ-GridPlot](XyzGridPlot/XyzGridPlot.png)

(Workflow ComfyUI inclus)

Génère un XYZ-Gridplot à partir d'une liste d'images.
Il prend une liste d'images (y compris les lots) et les aplatit d'abord en une longue liste (ainsi `batch_size=1`).

**Forme de la grille**
Détermine la forme de la grille par :
1. le nombre d'étiquettes de lignes
2. le nombre d'étiquettes de colonnes
3. les sous-images restants.
Vous pouvez utiliser `order=inside_out` pour inverser la sélection d'images (utile si `batch_size>1` et que vous souhaitez étiqueter les lots).

**Alignement**
* Si une étiquette est renvoyée à la ligne suivante, l'ensemble de l'axe est considéré comme "multiligne" et les aligne en haut avec un espacement justifié.
* Si toutes les étiquettes sont des nombres ou se terminent toutes par des nombres (par exemple `strength: 1.`), l'ensemble de l'axe est considéré comme "numérique" et les aligne à droite.
* Tout autre texte est considéré comme "monoligne" et les aligne au centre.
* Aligne les étiquettes monolignes et numériques pour les colonnes en bas, et pour les lignes les aligne verticalement au milieu.

**Taille de la police**
* La hauteur de la zone des étiquettes de colonne est déterminée par `font_size` ou `la moitié de la hauteur de l'empaquetage des sous-images les plus grands dans n'importe quelle ligne` (selon le plus grand).
* La largeur de la zone des étiquettes de ligne est déterminée par la largeur maximale de l'empaquetage des sous-images (avec un minimum de 256px).
* Le texte est réduit jusqu'à ce qu'il tienne (jusqu'à `font_size_min=6`) et utilise la même taille de police pour l'ensemble de l'axe (étiquettes de lignes ou de colonnes).
Si la taille de police est déjà au minimum, les textes restants sont tronqués.

**Empaquetage des sous-images**
Forme les sous-images (généralement des lots) dans la zone la plus carrée (l'"empaquetage des sous-images"), sauf si `output_is_list=True`, auquel cas utilise une seule image par cellule et crée une liste de grilles d'images entières au lieu.
Vous pouvez utiliser cette liste de grilles d'images pour connecter un autre nœud XyzGridPlot afin créer des super-grilles.
Si les sous-images consistent en des lots de tailles différentes, remplit les cellules manquantes avec des images vides.
Le nombre d'images par cellules (y compris les images en lots) doit être un multiple de `rows * columns`.

### Entrées

| Nom | Type | Description |
| --- | --- | --- |
| `images` | `IMAGE` | Une liste d'images (y compris les lots) |
| `row_labels` | `*` | Textes des étiquettes de lignes sur le côté gauche |
| `col_labels` | `*` | Textes des étiquettes de colonnes en haut |
| `gap` | `INT` | Espacement entre les empaquetages des sous-images. Notez que l'intérieur des sous-images n'utilise aucun espacement. Si vous souhaitez un espacement entre les sous-images, connectez un autre nœud XyzGridPlot. |
| `font_size` | `FLOAT` | Taille de police cible. Le texte sera réduit jusqu'à ce qu'il tienne (jusqu'à `font_size_min=6`). |
| `row_label_orientation` | `COMBO` | Orientation du texte des étiquettes de lignes. Utile si vous souhaitez économiser de l'espace. |
| `order` | `BOOLEAN` | Définit l'ordre dans lequel les images doivent être traitées. Cela n'est pertinent que si vous avez des sous-images. Utile si `batch_size>1` et que vous souhaitez tracer les lots. |
| `output_is_list` | `BOOLEAN` | Cela n'est pertinent que si vous avez des sous-images ou si vous souhaitez créer des super-grilles. |

### Sorties

| Nom | Type | Description |
| --- | --- | --- |
| `image` | `IMAGE 𝌠` | L'image XYZ-GridPlot. Si `output_is_list=True`, crée une liste d'images que vous pouvez connecter à un autre nœud XYZ-GridPlot pour créer des super-grilles. |

