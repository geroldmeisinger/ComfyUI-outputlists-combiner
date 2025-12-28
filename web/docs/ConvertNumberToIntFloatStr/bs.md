<!-- This file was auto-translated with a local LLM and last updated on 2025-12-28. -->
## Pretvori u Cijeli broj, Decimalni broj, String

![Pretvori u Cijeli broj, Decimalni broj, String](ConvertNumberToIntFloatStr/ConvertNumberToIntFloatStr.png)

(Uključen je ComfyUI workflow)

Pretvara sve što izgleda kao broj u `INT`, `FLOAT`, `STRING`.
Koristi unutrašnje `nums_from_string.get_nums` koji je vrlo otporan prema brojevima koje prihvata. Brojeve iz stvarnih cijelih brojeva, stvarnih decimalnih brojeva, cijelih ili decimalnih brojeva kao stringova, stringova koji sadrže više brojeva s razdvojnicama za tisuće.
Koristite string `123;234;345` da bi brzo generirali listu brojeva. Ne koristite zarez kao razdvojnik jer se mogu interpretirati kao razdvojnici za tisuće.
`int`, `float` i `string` koriste `is_output_list=True` (označeno simbolom `𝌠`) i će biti obradjeni redom odgovarajućim čvorovima.

### Ulazni podaci

| Ime | Tip | Opis |
| --- | --- | --- |
| `any` | `*` | Bilo šta što može biti značajno pretvoren u string sa brojevima koji mogu biti parsirani unutar |

### Iznosi

| Ime | Tip | Opis |
| --- | --- | --- |
| `int` | `INT 𝌠` | Svi brojevi pronađeni u stringu s decimalkama izrezane. |
| `float` | `FLOAT 𝌠` | Svi brojevi pronađeni u stringu kao decimalni brojevi. |
| `string` | `STRING 𝌠` | Svi brojevi pronađeni u stringu kao decimalni brojevi pretvorenih u string. |
| `count` | `INT` | Broj brojeva pronađenih u vrijednosti. |

