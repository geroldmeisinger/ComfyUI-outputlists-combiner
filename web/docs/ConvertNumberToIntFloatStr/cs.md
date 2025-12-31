## Převést na celé číslo, desetinné číslo, řetězec

![Převést na celé číslo, desetinné číslo, řetězec](ConvertNumberToIntFloatStr/ConvertNumberToIntFloatStr.png)

(ComfyUI workflow zahrnut)

Převede cokoli číselného na `CELÉ ČÍSLO` `DESETINNÉ ČÍSLO` `ŘETĚZEC`.
Interně používá `nums_from_string.get_nums`, který je velmi permissivní v číslech, která přijímá. Cokoli od skutečných celých čísel, skutečných desetinných čísel, celých čísel nebo desetinných čísel jako řetězců, řetězců obsahujících více čísel se separátory tisíců.
Použijte řetězec `123;234;345` pro rychlé vygenerování seznamu čísel. Nepoužívejte čárky jako separátory, protože mohou být interpretovány jako separátory tisíců.
`int`, `float` a `string` používají `is_output_list=True` (označeno symbolem `𝌠`) a budou zpracovány sekvenčně odpovídajícími uzly.

### Vstupy

| Název | Typ | Popis |
| --- | --- | --- |
| `any` | `*` | Cokoli, co lze smysluplně převést na řetězec s čitelnými čísly uvnitř |

### Výstupy

| Název | Typ | Popis |
| --- | --- | --- |
| `int` | `CELÉ ČÍSLO 𝌠` | Všechna čísla nalezená v řetězci s odříznutými desetinnými místy. |
| `float` | `DESETINNÉ ČÍSLO 𝌠` | Všechna čísla nalezená v řetězci jako desetinná čísla. |
| `string` | `ŘETĚZEC 𝌠` | Všechna čísla nalezená v řetězci jako desetinná čísla převedená na řetězec. |
| `count` | `CELÉ ČÍSLO` | Počet čísel nalezených ve vstupu. |

