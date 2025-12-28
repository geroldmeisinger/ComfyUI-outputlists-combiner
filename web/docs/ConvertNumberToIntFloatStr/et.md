<!-- This file was auto-translated with a local LLM and last updated on 2025-12-28. -->
## Teisendamine täisarv, kümnendarv, stringiks

![Teisendamine täisarv, kümnendarv, stringiks](ConvertNumberToIntFloatStr/ConvertNumberToIntFloatStr.png)

(Sisendus töövoolus ComfyUI)

Teisendab kõiki numberlikke väärtusi `INT` `FLOAT` `STRING` vormi.
Kasutab sisemiselt `nums_from_string.get_nums`, mis on väga laiendatud numbrid arvutamiseks. Sellele võib sobida tõelised täisarvud, tõelised kümnendarvud, täisarvud või kümnendarvud kui stringid, stringid, mis sisaldavad mitmeid numbreid miljardisega eraldajatega.
Kasutage stringi `123;234;345` täisarvude hulga kiirest loomiseks. Kõrvaldage komaga eraldajaid, kuna need võivad tõuseda miljardisega eraldajateks.
`int`, `float` ja `string` kasutavad `is_output_list=True` (märgitakse sümboliga `𝌠`) ja on käivitatud vastavate node-ide kaudu järjekorras.

### Sisendid

| Nimi | Tüüp | Kirjeldus |
| --- | --- | --- |
| `any` | `*` | Mis tahes väärtus, mis saab tähendavalt teisendada stringiks, mille sisu sisaldab loetavaid numbreid |

### Väljad

| Nimi | Tüüp | Kirjeldus |
| --- | --- | --- |
| `int` | `INT 𝌠` | Sisendist leidud numbrid, milles kümnendkohad on kõrvaldavad. |
| `float` | `FLOAT 𝌠` | Sisendist leidud numbrid, millel on kümnendkohad. |
| `string` | `STRING 𝌠` | Sisendist leidud numbrid, millel on kümnendkohad, teisendatud stringiks. |
| `count` | `INT` | Leidud numbreid väärtusest. |

