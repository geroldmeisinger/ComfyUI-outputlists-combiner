<!-- This file was auto-translated with a local LLM and last updated on 2025-12-28. -->
## Badilisha Kwa Int Float Str

![Badilisha Kwa Int Float Str](ConvertNumberToIntFloatStr/ConvertNumberToIntFloatStr.png)

(Workflow wa ComfyUI unayotumika)

Badilisha kila kitu cha kiasi cha namba kwa `INT` `FLOAT` `STRING`.
Inatumia `nums_from_string.get_nums` kwa kati ambacho ni kikamilifu sana katika namba zinazokubaliwa. Kila kitu kutoka kwa namba halisi, namba halisi, namba au namba kama string, string ambayo ina namba mbili au zaidi na kipimo cha milioni.
Tumia string `123;234;345` kusanya kama kila kipimo cha namba. Usitumie koma kama kipimo cha kipimo cha milioni kwa sababu zinaweza kuchukuliwa kama kipimo cha milioni.
`int`, `float` na `string` zinatumia `is_output_list=True` (inashirikisha simu `𝌠`) na zinatamkwa kwa mpango wa kila kipimo cha kila node.

### Miongozo

| Jina | Aina | Maelezo |
| --- | --- | --- |
| `any` | `*` | Kila kitu ambacho kinaweza kubadilishwa kwa string na kina namba zinazokubaliwa kwenye string |

### Matokeo

| Jina | Aina | Maelezo |
| --- | --- | --- |
| `int` | `INT 𝌠` | Namba zote zilizopatikana katika string kwa kuchukua kipimo cha miongo. |
| `float` | `FLOAT 𝌠` | Namba zote zilizopatikana katika string kama floats. |
| `string` | `STRING 𝌠` | Namba zote zilizopatikana katika string kama floats zilizobadilishwa kwa string. |
| `count` | `INT` | Idadi ya namba zilizopatikana katika thamani. |

