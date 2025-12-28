<!-- This file was auto-translated with a local LLM and last updated on 2025-12-28. -->
## Převést na celé číslo, desetinné číslo, řetězec

![Převést na celé číslo, desetinné číslo, řetězec](ConvertNumberToIntFloatStr/ConvertNumberToIntFloatStr.png)

(Zahrnuto do pracovního postupu ComfyUI)

Převádí všechny číselné hodnoty na `INT`, `FLOAT`, `STRING`.
Vnitřně používá `nums_from_string.get_nums`, který je velmi široce přijímající v číselných hodnotách. Přijímá všechny skutečné celá čísla, skutečné desetinná čísla, celá čísla nebo desetinná čísla jako řetězce, řetězce obsahující více čísel s oddělovači tisíců.
Použijte řetězec `123;234;345`, abyste rychle vytvořili seznam čísel. Nenechávejte používat čárky jako oddělovače, protože mohou být interpretovány jako oddělovače tisíců.
Typy `int`, `float` a `string` používají `is_output_list=True` (označené symbolem `𝌠`) a budou postupně zpracovávány odpovídajícími uzly.

### Vstupy

| Název | Typ | Popis |
| --- | --- | --- |
| `any` | `*` | Libovolné, co lze převést na řetězec s číselnými hodnotami, které lze analyzovat |

### Výstupy

| Název | Typ | Popis |
| --- | --- | --- |
| `int` | `INT 𝌠` | Všechna nalezená čísla v řetězci s odřezáním desetinných míst. |
| `float` | `FLOAT 𝌠` | Všechna nalezená čísla v řetězci jako desetinná čísla. |
| `string` | `STRING 𝌠` | Všechna nalezená čísla v řetězci jako desetinná čísla převedená na řetězec. |
| `count` | `INT` | Počet nalezených čísel v hodnotě. |

