## Convertir en Int, Float, Str

![Convert To Int Float Str](ConvertNumberToIntFloatStr/ConvertNumberToIntFloatStr.png)

(Workflow ComfyUI inclus)

Convertit n'importe quoi de ressemblant à un nombre en `INT` `FLOAT` `STRING`.
Utilise interne `nums_from_string.get_nums` qui est très permissif quant aux nombres qu'il accepte. Tout, de nombres entiers réels, de nombres à virgule flottante réels, de nombres entiers ou à virgule flottante sous forme de chaîne de caractères, de chaînes contenant plusieurs nombres avec des séparateurs de milliers.
Utilisez une chaîne de caractères `123;234;345` pour générer rapidement une liste de nombres. N'utilisez pas de virgules comme séparateurs car elles peuvent être interprétées comme des séparateurs de milliers.
`int`, `float` et `string` utilisent `is_output_list=True` (indiqué par le symbole `𝌠`) et seront traités séquentiellement par les nœuds correspondants.

### Entrées

| Nom | Type | Description |
| --- | --- | --- |
| `any` | `*` | Tout ce qui peut être converti de manière significative en chaîne de caractères contenant des nombres lisibles |

### Sorties

| Nom | Type | Description |
| --- | --- | --- |
| `int` | `INT 𝌠` | Tous les nombres trouvés dans la chaîne de caractères avec les décimales tronquées. |
| `float` | `FLOAT 𝌠` | Tous les nombres trouvés dans la chaîne de caractères sous forme de nombres à virgule flottante. |
| `string` | `STRING 𝌠` | Tous les nombres trouvés dans la chaîne de caractères sous forme de nombres à virgule flottante convertis en chaîne de caractères. |
| `count` | `INT` | Nombre de nombres trouvés dans la valeur. |

