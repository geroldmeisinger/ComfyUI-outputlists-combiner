## Konvertálás INT, FLOAT, STR típusba

![Convert To Int Float Str](ConvertNumberToIntFloatStr/ConvertNumberToIntFloatStr.png)

(ComfyUI workflow mellékletként)

Bármilyen számhoz hasonló értéket `INT` `FLOAT` `STRING` típusba konvertál.
Belsőleg a `nums_from_string.get_nums` függvényt használja, amely nagyon engedelmes a fogadott számokkal kapcsolatban. Minden, amit valódi egész szám, valódi lebegőpontos szám, egész vagy lebegőpontos szám sztringként, vagy több számot tartalmazó sztringek, ezres elválasztóval.
Használjon sztringet `123;234;345` formátumban a számok listájának gyors létrehozásához. Ne használjon vesszőt elválasztóként, mivel az ezres elválasztóként lehet értelmezve.
Az `int`, `float` és `string` használja a `is_output_list=True` (a `𝌠` szimbólummal jelölt) paramétert, és szekvenciálisan lesznek feldolgozva a megfelelő csomópontok által.

### Bemenetek

| Név | Típus | Leírás |
| --- | --- | --- |
| `any` | `*` | Bármi, amit értelmezhetően konvertálni lehet sztringgé, parse-olható számokkal bennük |

### Kimenetek

| Név | Típus | Leírás |
| --- | --- | --- |
| `int` | `INT 𝌠` | A sztringben található összes szám, a tizedesjegyek elvágva. |
| `float` | `FLOAT 𝌠` | A sztringben található összes szám lebegőpontosan. |
| `string` | `STRING 𝌠` | A sztringben található összes szám lebegőpontosan konvertálva sztringgé. |
| `count` | `INT` | A számok mennyisége a megadott értékben. |

