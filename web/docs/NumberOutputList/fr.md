## Number OutputList

![Number OutputList](NumberOutputList/NumberOutputList.png)

(Workflow ComfyUI inclus)

Crée une OutputList avec une plage de valeurs numériques.
Utilise interne [numpy.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html), car cela fonctionne plus fiablement avec les valeurs à virgule flottante.
Si vous souhaitez définir des listes de nombres avec des pas arbitraires, consultez JSON OutputList et définissez un tableau, par exemple `[1, 42, 123]`.
`int`, `float`, `string` et `index` utilisent `is_output_list=True` (indiqué par le symbole `𝌠`) et seront traités séquentiellement par les nœuds correspondants.

### Entrées

| Nom | Type | Description |
| --- | --- | --- |
| `start` | `FLOAT` | Valeur de départ pour générer la plage. |
| `stop` | `FLOAT` | Valeur de fin. Si `endpoint=include` alors ce nombre est inclus dans la liste. |
| `num` | `INT` | Le nombre d'éléments dans la liste (ne pas le confondre avec un `step`). |
| `endpoint` | `BOOLEAN` | Détermine si la valeur `stop` doit être incluse ou exclue dans les éléments. |

### Sorties

| Nom | Type | Description |
| --- | --- | --- |
| `int` | `INT 𝌠` | La valeur convertie en entier (arrondie vers le bas). |
| `float` | `FLOAT 𝌠` | La valeur sous forme de nombre à virgule flottante. |
| `string` | `STRING 𝌠` | La valeur sous forme de nombre à virgule flottante convertie en chaîne de caractères. |
| `index` | `INT 𝌠` | Plage de 0..count qui peut être utilisée comme index. |
| `count` | `INT` | Identique à `num`. |

