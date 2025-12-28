<!-- This file was auto-translated with a local LLM and last updated on 2025-12-28. -->
## Convertir a enter, float, string

![Convertir a enter, float, string](ConvertNumberToIntFloatStr/ConvertNumberToIntFloatStr.png)

(Workflow de ComfyUI inclòs)

Converteix qualsevol cosa que tingui un valor numèric a `INT`, `FLOAT` o `STRING`.
Utilitza `nums_from_string.get_nums` internament, que és molt permisiv en els números que accepta. Tots els valors, des de nombres reals, nombres decimals, strings amb nombres enters o decimals, fins a strings que continguin diversos nombres amb separadors de milers.
Utilitza una cadena com `123;234;345` per generar ràpidament una llista de nombres. No utilitzi coma com a separador, ja que pot ser interpretada com a separador de milers.
`int`, `float` i `string` utilitzen `is_output_list=True` (indicat per el símbol `𝌠`) i seran processats seqüencialment per nodes corresponents.

### Entrades

| Nom | Tipus | Descripció |
| --- | --- | --- |
| `any` | `*` | Qualsevol cosa que pugui convertir-se significativament a una cadena amb nombres interpretables dins |

### Sortides

| Nom | Tipus | Descripció |
| --- | --- | --- |
| `int` | `INT 𝌠` | Tots els nombres trobats a la cadena amb decimals truncats. |
| `float` | `FLOAT 𝌠` | Tots els nombres trobats a la cadena com a flotants. |
| `string` | `STRING 𝌠` | Tots els nombres trobats a la cadena com a flotants convertits a cadena. |
| `count` | `INT` | Quantitat de nombres trobats a la valor. |

