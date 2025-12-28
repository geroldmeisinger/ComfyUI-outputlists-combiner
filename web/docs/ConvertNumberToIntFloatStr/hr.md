<!-- This file was auto-translated with a local LLM and last updated on 2025-12-28. -->
## Pretvori u cjelobroj, decimalni broj, string

![Pretvori u cjelobroj, decimalni broj, string](ConvertNumberToIntFloatStr/ConvertNumberToIntFloatStr.png)

(Uključen je ComfyUI workflow)

Pretvara bilo koji broj-like podatak u `INT`, `FLOAT`, `STRING`.
Koristi unutrašnje `nums_from_string.get_nums` koji je vrlo otkriven u brojevima koje prihvaća. Bilo koji broj, stvarni cijeli broj, stvarni decimalni broj, cijeli ili decimalni broj kao string, string koji sadrži više brojeva s razdvojnicama za tisuće.
Koristite string `123;234;345` da bi brzo generirali listu brojeva. Ne koristite zarez kao razdvojnik jer se mogu shvatiti kao razdvojnici za tisuće.
`int`, `float` i `string` koriste `is_output_list=True` (označeno simbolom `𝌠`) i će biti obradjeni redom odgovarajućim čvorovima.

### Ulazi

| Ime | Tip | Opis |
| --- | --- | --- |
| `any` | `*` | Bilo šta što može biti značajno pretvoren u string s brojevima koji su mogući za analizu |

### Izlazi

| Ime | Tip | Opis |
| --- | --- | --- |
| `int` | `INT 𝌠` | Svi brojevi pronađeni u stringu s odbacivanjem decimalnih znamenki. |
| `float` | `FLOAT 𝌠` | Svi brojevi pronađeni u stringu kao decimalni brojevi. |
| `string` | `STRING 𝌠` | Svi brojevi pronađeni u stringu kao decimalni brojevi pretvorenih u string. |
| `count` | `INT` | Broj brojeva pronađenih u vrijednosti. |

