## JSON OutputList

![JSON OutputList](JSONOutputList/JSONOutputList.png)

(Workflow ComfyUI inclus)

Crée une OutputList en extrayant des tableaux ou des dictionnaires à partir d'objets JSON.
Utilise la syntaxe JSONPath pour extraire les valeurs, voir [JSONPath sur Wikipedia](https://en.wikipedia.org/wiki/JSONPath) .
Toutes les valeurs correspondantes sont aplanies en une longue liste.
Vous pouvez également utiliser ce nœud pour créer des objets à partir de chaînes littérales comme `[1, 2, 3]`.
`key`, `value`, `int` et `float` utilisent `is_output_list=True` (indiqué par le symbole `𝌠`) et seront traités séquentiellement par les nœuds correspondants.

### Entrées

| Nom | Type | Description |
| --- | --- | --- |
| `jsonpath` | `STRING` | JSONPath utilisé pour extraire les valeurs. |
| `json` | `STRING` | Une chaîne de caractères JSON qui est traduite en objet. |
| `obj` | `*` | (optionnel) objet de tout type qui remplacera la chaîne JSON |

### Sorties

| Nom | Type | Description |
| --- | --- | --- |
| `key` | `STRING 𝌠` | La clé pour les dictionnaires ou l'index pour les tableaux (sous forme de chaîne de caractères). Techniquement, c'est un index global de la liste aplanie pour tous les éléments non-clés. |
| `value` | `STRING 𝌠` | La valeur sous forme de chaîne de caractères. |
| `int` | `INT 𝌠` | La valeur sous forme d'entier (si le nombre ne peut pas être analysé, la valeur par défaut est 0). |
| `float` | `FLOAT 𝌠` | La valeur sous forme de nombre à virgule flottante (si le nombre ne peut pas être analysé, la valeur par défaut est 0). |
| `count` | `INT` | Nombre total d'éléments dans la liste aplanie |
| `debug` | `STRING` | Sortie de débogage de tous les objets correspondants sous forme de chaîne de caractères JSON formatée |

