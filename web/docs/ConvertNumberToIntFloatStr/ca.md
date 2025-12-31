## Convertir a Int Float Str

![Convertir a Int Float Str](ConvertNumberToIntFloatStr/ConvertNumberToIntFloatStr.png)

(ComfyUI workflow inclòs)

Converteix qualsevol cosa semblant a un número a `INT` `FLOAT` `STRING`.
Utilitza internament `nums_from_string.get_nums` que és molt permisivo amb els números que accepta. Qualsevol cosa des d'enters reals, decimals reals, enters o decimals com a cadenes, cadenes que contenen múltiples números amb separadors de milers.
Utilitza una cadena `123;234;345` per generar ràpidament una llista de números. No utilitzis comes com a separadors ja que poden ser interpretades com a separadors de milers.
`int`, `float` i `string` utilitzen `is_output_list=True` (indicat pel símbol `𝌠`) i seran processats seqüencialment per els nodes corresponents.

### Entrades

| Nom | Tipus | Descripció |
| --- | --- | --- |
| `any` | `*` | Qualsevol cosa que es pugui convertir significativament a una cadena amb números analitzables dins |

### Sortides

| Nom | Tipus | Descripció |
| --- | --- | --- |
| `int` | `INT 𝌠` | Tots els números trobats a la cadena amb els decimals truncats. |
| `float` | `FLOAT 𝌠` | Tots els números trobats a la cadena com a decimals. |
| `string` | `STRING 𝌠` | Tots els números trobats a la cadena com a decimals convertits a cadena. |
| `count` | `INT` | Quantitat de números trobats al valor. |

