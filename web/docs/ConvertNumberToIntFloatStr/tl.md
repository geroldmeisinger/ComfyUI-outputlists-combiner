<!-- This file was auto-translated with a local LLM and last updated on 2025-12-28. -->
## I-transforma sa Int, Float, Str

![I-transforma sa Int, Float, Str](ConvertNumberToIntFloatStr/ConvertNumberToIntFloatStr.png)

(Nakabatay sa ComfyUI workflow)

Nagpapalit ng anumang number-like na data sa `INT`, `FLOAT`, at `STRING`.
Ginagamit ang `nums_from_string.get_nums` na nangangailangan ng malawak na pagpapahayag ng mga numero. Maaaring magkakaroon ng mga actual ints, actual floats, ints o floats bilang string, at mga string na may maraming numero na may thousand-separators.
Gamitin ang string `123;234;345` upang mabilis na maghahatid ng isang listahan ng mga numero. Hindi dapat gamitin ang komma bilang separator dahil maaari itong maiinterpretasyon bilang thousand-separators.
Ang `int`, `float`, at `string` ay gumagamit ng `is_output_list=True` (na nagsasalita ng simbolo `𝌠`) at magpapabilis sa pagbabayad ng mga tanging node.

### Input

| Pangalan | Tipo | Paglalaro |
| --- | --- | --- |
| `any` | `*` | Anumang bagay na maaaring palitan sa string na may mga number na maaaring ma-parse |

### Output

| Pangalan | Tipo | Paglalaro |
| --- | --- | --- |
| `int` | `INT 𝌠` | Ang lahat ng mga numero na nakalista sa string na may decimal na pinapababa. |
| `float` | `FLOAT 𝌠` | Ang lahat ng mga numero na nakalista sa string bilang float. |
| `string` | `STRING 𝌠` | Ang lahat ng mga numero na nakalista sa string bilang float na pinapalit sa string. |
| `count` | `INT` | Ang bilang ng mga numero na nakalista sa value. |

