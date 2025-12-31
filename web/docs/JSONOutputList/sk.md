## JSON OutputList

![JSON OutputList](JSONOutputList/JSONOutputList.png)

(ComfyUI workflow je zahrnutý)

Vytvorí OutputList extrahovaním polí alebo slovníkov z JSON objektov.
Používa syntax JSONPath na extrakciu hodnôt, pozri [JSONPath na Wikipédii](https://en.wikipedia.org/wiki/JSONPath) .
Všetky zhodné hodnoty sú zrovnania do jedného dlhého zoznamu.
Tento uzol môžete tiež použiť na vytvorenie objektov z literálnych reťazcov ako `[1, 2, 3]`.
`key`, `value`, `int` a `float` používajú `is_output_list=True` (označené symbolom `𝌠`) a budú spracované postupne príslušnými uzlami.

### Vstupy

| Názov | Typ | Popis |
| --- | --- | --- |
| `jsonpath` | `STRING` | JSONPath použitý na extrakciu hodnôt. |
| `json` | `STRING` | JSON reťazec, ktorý sa preloží na objekt. |
| `obj` | `*` | (voliteľné) objekt ľubovoľného typu, ktorý nahradí JSON reťazec |

### Výstupy

| Názov | Typ | Popis |
| --- | --- | --- |
| `key` | `STRING 𝌠` | Kľúč pre slovníky alebo index pre poľa (ako reťazec). Technicky ide o globálny index zrovnania zoznamu pre všetky nekľúče. |
| `value` | `STRING 𝌠` | Hodnota ako reťazec. |
| `int` | `INT 𝌠` | Hodnota ako celé číslo (ak sa nedá číslo spracovať, použije sa predvolená hodnota 0). |
| `float` | `FLOAT 𝌠` | Hodnota ako desatinné číslo (ak sa nedá číslo spracovať, použije sa predvolená hodnota 0). |
| `count` | `INT` | Celkový počet položiek v zrovnanej liste |
| `debug` | `STRING` | Ladiaci výstup všetkých zhodných objektov ako formátovaný JSON reťazec |

