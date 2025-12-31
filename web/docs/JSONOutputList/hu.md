## JSON OutputList

![JSON OutputList](JSONOutputList/JSONOutputList.png)

(ComfyUI workflow mellékletként)

Létrehoz egy OutputList-et JSON objektumokból származó tömbök vagy szótárak kinyerésével.
JSONPath szintaxist használ az értékek kinyerésére, lásd [JSONPath a Wikipédián](https://en.wikipedia.org/wiki/JSONPath) .
Minden egyező érték egy hosszú listába kerül leképezésre.
Ez a csomópont használható objektumok létrehozására is szöveges literálok alapján, például `[1, 2, 3]`.
A `key`, `value`, `int` és `float` használja a `is_output_list=True` (a `𝌠` szimbólummal jelölt) paramétert, és szekvenciálisan lesznek feldolgozva a megfelelő csomópontok által.

### Bemenetek

| Név | Típus | Leírás |
| --- | --- | --- |
| `jsonpath` | `STRING` | A JSONPath, amelyet az értékek kinyerésére használnak. |
| `json` | `STRING` | Egy JSON sztring, amely objektummá alakítva lesz. |
| `obj` | `*` | (opcionális) bármilyen típusú objektum, amely lecseréli a JSON sztringet |

### Kimenetek

| Név | Típus | Leírás |
| --- | --- | --- |
| `key` | `STRING 𝌠` | A szótárak kulcsa vagy a tömbök indexe (sztringként). Technikailag ez az összes nem kulcs érték globális indexe a leképezett listában. |
| `value` | `STRING 𝌠` | Az érték sztringként. |
| `int` | `INT 𝌠` | Az érték egész számként (ha nem sikerül a számot feldolgozni, alapértelmezetten 0). |
| `float` | `FLOAT 𝌠` | Az érték lebegőpontos számként (ha nem sikerül a számot feldolgozni, alapértelmezetten 0). |
| `count` | `INT` | Az összes elem száma a leképezett listában |
| `debug` | `STRING` | A megegyező objektumok hibakeresési kimenete formázott JSON sztringként |

