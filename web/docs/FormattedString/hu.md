## Formázott sztring

![Formatted String](FormattedString/FormattedString.png)

(ComfyUI workflow mellékletként)

Létrehoz egy sztringet, amely helyőrző változókat tartalmaz, és lecseréli őket a megfelelő értékekre.
Belsőleg a python `str.format()` függvényt használja, lásd [Python - Format String Syntax](https://docs.python.org/3/library/string.html#format-string-syntax) .
* Használhatod a `{a:.2f}` formátumot, hogy lekerekítse a lebegőpontos számot 2 tizedesjegyre.
* Használhatod a `{a:05d}` formátumot, hogy 5 nullával feltöltse a számot, hogy illeszkedjen a comfys fájlnév utótaghoz `ComfyUI_00001_.png`.
* Ha `{ }` karaktereket szeretnél használni a sztringekben (pl. JSON esetén), duplán kell írni: `{{ }}`.

Ugyanúgy alkalmazza a *keresés és csere (S&R)* szintaxist is, mint például `%date:yyyy-MM-dd hh:mm:ss%` és `%KSampler.seed%`.
Így használhatod egy `GET-node`-ként is.
Megjegyzés: a "keresés és csere" JavaScript kontextusban történik, és a csomópont végrehajtása előtt fut le.

### Bemenetek

| Név | Típus | Leírás |
| --- | --- | --- |
| `fstring` | `STRING` | Létrehoz egy sztringet, amely helyőrző változókat tartalmaz, és lecseréli őket a megfelelő értékekre.<br>Belsőleg a python `str.format()` függvényt használja, lásd [Python - Format String Syntax](https://docs.python.org/3/library/string.html#format-string-syntax) .<br>* Használhatod a `{a:.2f}` formátumot, hogy lekerekítse a lebegőpontos számot 2 tizedesjegyre.<br>* Használhatod a `{a:05d}` formátumot, hogy 5 nullával feltöltse a számot, hogy illeszkedjen a comfys fájlnév utótaghoz `ComfyUI_00001_.png`.<br>* Ha `{ }` karaktereket szeretnél használni a sztringekben (pl. JSON esetén), duplán kell írni: `{{ }}`.<br><br>Ugyanúgy alkalmazza a *keresés és csere (S&R)* szintaxist is, mint például `%date:yyyy-MM-dd hh:mm:ss%` és `%KSampler.seed%`.<br>Így használhatod egy `GET-node`-ként is.<br>Megjegyzés: a "keresés és csere" JavaScript kontextusban történik, és a csomópont végrehajtása előtt fut le. |
| `a` | `*` | (opcionális) érték, amely a `{a}` helyőrző helyére kerül sztringként. |
| `b` | `*` | (opcionális) érték, amely a `{b}` helyőrző helyére kerül sztringként. |
| `c` | `*` | (opcionális) érték, amely a `{c}` helyőrző helyére kerül sztringként. |
| `d` | `*` | (opcionális) érték, amely a `{d}` helyőrző helyére kerül sztringként. |

### Kimenetek

| Név | Típus | Leírás |
| --- | --- | --- |
| `string` | `STRING` | A formázott sztring, ahol minden helyőrző lecserélve van a megfelelő értékre. |

