## Chaîne formatée

![Formatted String](FormattedString/FormattedString.png)

(Workflow ComfyUI inclus)

Crée une chaîne de caractères contenant des variables de substitution et les remplace par leurs valeurs respectives.
Utilise interne `str.format()` de Python, voir [Python - Syntaxe des chaînes de caractères formatées](https://docs.python.org/3/library/string.html#format-string-syntax) .
* Vous pouvez utiliser `{a:.2f}` pour arrondir un nombre à virgule flottante à 2 décimales.
* Vous pouvez utiliser `{a:05d}` pour compléter avec jusqu'à 5 zéros en tête pour s'adapter au suffixe de nom de fichier de Comfy `ComfyUI_00001_.png`.
* Si vous souhaitez écrire `{ }` dans vos chaînes de caractères (par exemple pour les JSON), vous devez les doubler : `{{ }}`.

Applique également la *syntaxe de recherche et remplacement (S&R)* telle que `%date:yyyy-MM-dd hh:mm:ss%` et `%KSampler.seed%`.
Vous pouvez donc également l'utiliser comme un nœud `GET`.
Notez que le "remplacement de recherche" se produit dans le contexte JavaScript et s'exécute avant l'exécution du nœud.

### Entrées

| Nom | Type | Description |
| --- | --- | --- |
| `fstring` | `STRING` | Crée une chaîne de caractères contenant des variables de substitution et les remplace par leurs valeurs respectives.<br>Utilise interne `str.format()` de Python, voir [Python - Syntaxe des chaînes de caractères formatées](https://docs.python.org/3/library/string.html#format-string-syntax) .<br>* Vous pouvez utiliser `{a:.2f}` pour arrondir un nombre à virgule flottante à 2 décimales.<br>* Vous pouvez utiliser `{a:05d}` pour compléter avec jusqu'à 5 zéros en tête pour s'adapter au suffixe de nom de fichier de Comfy `ComfyUI_00001_.png`.<br>* Si vous souhaitez écrire `{ }` dans vos chaînes de caractères (par exemple pour les JSON), vous devez les doubler : `{{ }}`.<br><br>Applique également la *syntaxe de recherche et remplacement (S&R)* telle que `%date:yyyy-MM-dd hh:mm:ss%` et `%KSampler.seed%`.<br>Vous pouvez donc également l'utiliser comme un nœud `GET`.<br>Notez que le "remplacement de recherche" se produit dans le contexte JavaScript et s'exécute avant l'exécution du nœud. |
| `a` | `*` | (optionnel) valeur qui sera convertie en chaîne de caractères au niveau du substitut `{a}`. |
| `b` | `*` | (optionnel) valeur qui sera convertie en chaîne de caractères au niveau du substitut `{b}`. |
| `c` | `*` | (optionnel) valeur qui sera convertie en chaîne de caractères au niveau du substitut `{c}`. |
| `d` | `*` | (optionnel) valeur qui sera convertie en chaîne de caractères au niveau du substitut `{d}`. |

### Sorties

| Nom | Type | Description |
| --- | --- | --- |
| `string` | `STRING` | La chaîne de caractères formatée avec tous les substituts remplacés par leurs valeurs respectives. |

