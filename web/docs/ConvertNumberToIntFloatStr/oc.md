## Convertir en INT FLOT STR

![Convertir en INT FLOT STR](ConvertNumberToIntFloatStr/ConvertNumberToIntFloatStr.png)

(ComfyUI workflow inclòp)

Convertís tota mena de nombres en `INT` `FLOAT` `STRING`.
Utiliza `nums_from_string.get_nums` internament que's permissiu amb los nombres qu'accepta. Quin nombre que siá, nombres entièrs, nombres reals, nombres entièrs o reals coma cadena, cadenas que contenen mantun nombre amb de separadors de milièrs.
Utilizatz una cadena `123;234;345` per generar rapidament una lista de nombres. Utilizatz pas de virgulas coma separadors que seràn interpretats coma separadors de milièrs.
`int`, `float` e `string` utiliza `is_output_list=True` (indicat per lo simbòl `𝌠`) e seràn tractats sequencialament per los nodes corresponents.

### Entradas

| Nom | Tipe | Descripcion |
| --- | --- | --- |
| `any` | `*` | Tot que pòt èsser convertit de manièra significativa en cadena amb de nombres analisables dins |

### Sortidas

| Nom | Tipe | Descripcion |
| --- | --- | --- |
| `int` | `INT 𝌠` | Totes los nombres trobats dins la cadena amb los decimals truncats. |
| `float` | `FLOAT 𝌠` | Totes los nombres trobats dins la cadena coma nombres reals. |
| `string` | `STRING 𝌠` | Totes los nombres trobats dins la cadena coma nombres reals convertits en cadena. |
| `count` | `INT` | Nombre de nombres trobats dins la valor. |

