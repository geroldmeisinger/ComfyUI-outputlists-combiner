<!-- This file was auto-translated with a local LLM and last updated on 2025-12-28. -->
## Convertir en entier, float, chaîne

![Convertir en entier, float, chaîne](ConvertNumberToIntFloatStr/ConvertNumberToIntFloatStr.png)

(Workflow ComfyUI inclus)

Convertit tout ce qui ressemble à un nombre en `INT`, `FLOAT` ou `STRING`.
Utilise internement `nums_from_string.get_nums`, qui est très tolérant vis-à-vis des nombres qu'il accepte. Toute valeur, qu'elle soit un entier réel, un flottant réel, une chaîne contenant des entiers ou des flottants, ou une chaîne contenant plusieurs nombres séparés par des milliers.
Utilisez une chaîne comme `123;234;345` pour générer rapidement une liste de nombres. N'utilisez pas de virgules comme séparateurs, car elles pourraient être interprétées comme des séparateurs de milliers.
Les sorties `int`, `float` et `string` utilisent `is_output_list=True` (indiqué par le symbole `𝌠`) et seront traitées séquentiellement par les nœuds correspondants.

### Entrées

| Nom | Type | Description |
| --- | --- | --- |
| `any` | `*` | Tout ce qui peut être converti de manière significative en chaîne contenant des nombres lisibles |

### Sorties

| Nom | Type | Description |
| --- | --- | --- |
| `int` | `INT 𝌠` | Tous les nombres trouvés dans la chaîne, avec les décimales tronquées. |
| `float` | `FLOAT 𝌠` | Tous les nombres trouvés dans la chaîne sous forme de flottants. |
| `string` | `STRING 𝌠` | Tous les nombres trouvés dans la chaîne sous forme de flottants convertis en chaîne. |
| `count` | `INT` | Nombre total de nombres trouvés dans la valeur. |

