## Cadena formatada

![Cadena formatada](FormattedString/FormattedString.png)

(ComfyUI workflow inclòs)

Crea una cadena que conté variables de marcador de posició i les substitueix amb els seus valors respectius.
Utilitza internament `str.format()` de Python, vegeu [Python - Sintaxi de cadena de format](https://docs.python.org/3/library/string.html#format-string-syntax) .
* Pots utilitzar `{a:.2f}` per arrodonir un decimal a 2 decimals.
* Pots utilitzar `{a:05d}` per omplir fins a 5 zeros principals per ajustar-se al sufix de nom de fitxer de comfys `ComfyUI_00001_.png`.
* Si vols escriure `{ }` dins de les teves cadenes (per exemple, per JSONs) has de duplicar-les: `{{ }}`.

També s'aplica la sintaxi *cerca i reemplaça (C&R)* com ara `%date:yyyy-MM-dd hh:mm:ss%` i `%KSampler.seed%`.
Per tant, també pots utilitzar-lo com un node `GET`.
Tingues en compte que "cerca i reemplaça" es fa en context de JavaScript i s'executa abans de l'execució del node.

### Entrades

| Nom | Tipus | Descripció |
| --- | --- | --- |
| `fstring` | `STRING` | Crea una cadena que conté variables de marcador de posició i les substitueix amb els seus valors respectius.<br>Utilitza internament `str.format()` de Python, vegeu [Python - Sintaxi de cadena de format](https://docs.python.org/3/library/string.html#format-string-syntax) .<br>* Pots utilitzar `{a:.2f}` per arrodonir un decimal a 2 decimals.<br>* Pots utilitzar `{a:05d}` per omplir fins a 5 zeros principals per ajustar-se al sufix de nom de fitxer de comfys `ComfyUI_00001_.png`.<br>* Si vols escriure `{ }` dins de les teves cadenes (per exemple, per JSONs) has de duplicar-les: `{{ }}`.<br><br>També s'aplica la sintaxi *cerca i reemplaça (C&R)* com ara `%date:yyyy-MM-dd hh:mm:ss%` i `%KSampler.seed%`.<br>Per tant, també pots utilitzar-lo com un node `GET`.<br>Tingues en compte que "cerca i reemplaça" es fa en context de JavaScript i s'executa abans de l'execució del node. |
| `a` | `*` | (opcional) valor que es convertirà en cadena al marcador de posició `{a}`. |
| `b` | `*` | (opcional) valor que es convertirà en cadena al marcador de posició `{b}`. |
| `c` | `*` | (opcional) valor que es convertirà en cadena al marcador de posició `{c}`. |
| `d` | `*` | (opcional) valor que es convertirà en cadena al marcador de posició `{d}`. |

### Sortides

| Nom | Tipus | Descripció |
| --- | --- | --- |
| `string` | `STRING` | La cadena formatada amb tots els marcadors de posició substituïts amb els seus valors respectius. |

