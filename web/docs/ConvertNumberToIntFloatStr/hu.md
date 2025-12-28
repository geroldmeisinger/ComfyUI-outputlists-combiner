<!-- This file was auto-translated with a local LLM and last updated on 2025-12-28. -->
## Számok átalakítása egészre, tizedesre, szövegre

![Számok átalakítása egészre, tizedesre, szövegre](ConvertNumberToIntFloatStr/ConvertNumberToIntFloatStr.png)

(ComfyUI munkafolyamat beépítve)

Bármilyen számhoz hasonló értéket egész, tizedes vagy szövegként alakít át.
Belsőleg a `nums_from_string.get_nums` függvényt használja, amely nagyon széles körben elfogadja a számokat. Valódi egészek, valódi tizedesek, egészek vagy tizedesek szövegként, szövegek, amelyek több számot tartalmaznak százasválasztókkel.
Használj egy szöveget, például `123;234;345`, hogy gyorsan számok listáját hozhatsz létre. Ne használj vesszőket elválasztóként, mert ezek százasválasztóként is értelmezhetők.
Az `int`, `float` és `string` kimenetek `is_output_list=True` (a `𝌠` szimbólum által jelölve) használják, és soronként feldolgozódnak megfelelő csomópontok által.

### Bemenetek

| Név | Típus | Leírás |
| --- | --- | --- |
| `any` | `*` | Bármilyen érték, amit értelmezhetően szöveggé alakíthatunk, amelyben értelmezhető számok vannak |

### Kimenetek

| Név | Típus | Leírás |
| --- | --- | --- |
| `int` | `INT 𝌠` | A szövegben található számok, amelyek tizedeseket kiválasztottak. |
| `float` | `FLOAT 𝌠` | A szövegben található számok tizedesekként. |
| `string` | `STRING 𝌠` | A szövegben található számok tizedesekként, majd szöveggé alakítva. |
| `count` | `INT` | A megadott értékben található számok száma. |

