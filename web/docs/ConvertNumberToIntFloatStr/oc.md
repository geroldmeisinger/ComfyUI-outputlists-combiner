<!-- This file was auto-translated with a local LLM and last updated on 2025-12-28. -->
## Convertir a Int Float Str

![Convertir a Int Float Str](ConvertNumberToIntFloatStr/ConvertNumberToIntFloatStr.png)

(Workflow de ComfyUI inclòs)

Convertèt tota cosa numerica a `INT` `FLOAT` `STRING`.
Utiliza internament `nums_from_string.get_nums` que es molt permès en las numeros qu'accepta. Tòtes las formes: numeros reals, numeros flotants, numeros o flotants coma cadena, cadenas que contèn divers numeros amb separadors de milhar.
Utiliza una cadena `123;234;345` per generèt una lista de numeros ràpidament. Pas utilisar las virgules coma separadors perquè podèn ser interpretadas coma separadors de milhar.
`int`, `float` e `string` utilizan `is_output_list=True` (indicat per lo símbol `𝌠`) e son processats sequencialment per los nòds corresponents.

### Entradas

| Nom | Tipus | Descripció |
| --- | --- | --- |
| `any` | `*` | Cualquier cosa que pòt ser convertida significativament a una cadena amb numeros interpretables dins |

### Sortides

| Nom | Tipus | Descripció |
| --- | --- | --- |
| `int` | `INT 𝌠` | Tots los numeros trobats dins la cadena amb las decimales troncadas. |
| `float` | `FLOAT 𝌠` | Tots los numeros trobats dins la cadena coma flotants. |
| `string` | `STRING 𝌠` | Tots los numeros trobats dins la cadena coma flotants convertits a cadena. |
| `count` | `INT` | Quantitat de numeros trobats dins lo valor. |

