## String OutputList

![String OutputList](StringOutputList/StringOutputList.png)

(Workflow ComfyUI inclus)

Crée une OutputList en divisant la chaîne de caractères dans le champ texte avec un séparateur.
`value` et `index` utilisent `is_output_list=True` (indiqué par le symbole `𝌠`) et seront traités séquentiellement par les nœuds correspondants.

### Entrées

| Nom | Type | Description |
| --- | --- | --- |
| `separator` | `STRING` | La chaîne de caractères utilisée pour diviser les valeurs du champ texte. |
| `values` | `STRING` | Le texte que vous souhaitez diviser en une liste. Notez que la chaîne est tronquée des sauts de ligne de fin avant la division, et chaque élément est à nouveau tronqué des espaces blancs. |

### Sorties

| Nom | Type | Description |
| --- | --- | --- |
| `value` | `* 𝌠` | Les valeurs de la liste. |
| `index` | `INT 𝌠` | Plage de 0..count. Vous pouvez l'utiliser comme index. |
| `count` | `INT` | Le nombre d'éléments dans la liste. |
| `inspect_combo` | `COMBO` | Une sortie factice que vous pouvez utiliser pour lier à un `COMBO` et la pré-remplir avec ses valeurs. La connexion sera alors automatiquement re-liée à la sortie `value`. |

