## Convertir a Int Float Str

![Convert To Int Float Str](ConvertNumberToIntFloatStr/ConvertNumberToIntFloatStr.png)

(ComfyUI workflow incluido)

Convierte cualquier cosa parecida a un número a `INT` `FLOAT` `STRING`.
Utiliza internamente `nums_from_string.get_nums` que es muy permisivo con los números que acepta. Cualquier cosa desde enteros reales, flotantes reales, enteros o flotantes como cadenas, cadenas que contienen múltiples números con separadores de miles.
Utilice una cadena `123;234;345` para generar rápidamente una lista de números. No use comas como separadores ya que pueden ser interpretadas como separadores de miles.
`int`, `float` y `string` usan `is_output_list=True` (indicado por el símbolo `𝌠`) y serán procesados secuencialmente por los nodos correspondientes.

### Entradas

| Nombre | Tipo | Descripción |
| --- | --- | --- |
| `any` | `*` | Cualquier cosa que se pueda convertir significativamente a una cadena con números interpretables dentro |

### Salidas

| Nombre | Tipo | Descripción |
| --- | --- | --- |
| `int` | `INT 𝌠` | Todos los números encontrados en la cadena con los decimales truncados. |
| `float` | `FLOAT 𝌠` | Todos los números encontrados en la cadena como flotantes. |
| `string` | `STRING 𝌠` | Todos los números encontrados en la cadena como flotantes convertidos a cadena. |
| `count` | `INT` | Cantidad de números encontrados en el valor. |

