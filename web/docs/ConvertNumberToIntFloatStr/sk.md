<!-- This file was auto-translated with a local LLM and last updated on 2025-12-28. -->
## Prevedenie na celé číslo, desatinné číslo, reťazec

![Prevedenie na celé číslo, desatinné číslo, reťazec](ConvertNumberToIntFloatStr/ConvertNumberToIntFloatStr.png)

(Inklúzivný pracovný prehľad ComfyUI)

Prevedie ľubovoľné číselné hodnoty na `INT`, `FLOAT`, `STRING`.
Využíva interny `nums_from_string.get_nums`, ktorý je veľmi široký v prijímaní čísel. Prijíma skutočné celé čísla, skutočné desatinné čísla, celé alebo desatinné čísla ako reťazce, reťazce obsahujúce viacero čísel s tisícovými oddelovateľmi.
Použite reťazec `123;234;345` na rýchle vytvorenie zoznamu čísel. Niekedy nevyužívať čiarky ako oddelovateľov, pretože môžu byť interpretované ako tisícové oddelovateľy.
Typy `int`, `float` a `string` používajú `is_output_list=True` (označené symbolom `𝌠`) a budú postupne spracované príslušnými uzlami.

### Vstupy

| Názov | Typ | Popis |
| --- | --- | --- |
| `any` | `*` | ľubovoľné, čo môže byť významne prevedené na reťazec s číslami, ktoré sú možné prečítať |

### Výstupy

| Názov | Typ | Popis |
| --- | --- | --- |
| `int` | `INT 𝌠` | Všetky nájdené čísla v reťazci s odrezanými desatinnými miestami. |
| `float` | `FLOAT 𝌠` | Všetky nájdené čísla v reťazci ako desatinné čísla. |
| `string` | `STRING 𝌠` | Všetky nájdené čísla v reťazci ako desatinné čísla premenené na reťazec. |
| `count` | `INT` | Počet nájdených čísel v hodnote. |

