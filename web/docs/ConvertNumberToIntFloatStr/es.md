<!-- This file was auto-translated with a local LLM and last updated on 2025-12-28. -->
## Convertir a Entero, Flotante, Cadena

![Convertir a Entero, Flotante, Cadena](ConvertNumberToIntFloatStr/ConvertNumberToIntFloatStr.png)

(Flujo de trabajo de ComfyUI incluido)

Convierte cualquier cosa numérica en `INT`, `FLOAT` o `STRING`.
Utiliza `nums_from_string.get_nums` internamente, que es muy perdonador con los números que acepta. Cualquier cosa desde enteros reales, flotantes reales, enteros o flotantes como cadenas, cadenas que contengan múltiples números con separadores de mil.
Utiliza una cadena como `123;234;345` para generar rápidamente una lista de números. No utilices comas como separadores, ya que podrían interpretarse como separadores de mil.
`int`, `float` y `string` usan `is_output_list=True` (indicado por el símbolo `𝌠`) y serán procesados secuencialmente por los nodos correspondientes.

### Entradas

| Nombre | Tipo | Descripción |
| --- | --- | --- |
| `any` | `*` | Cualquier cosa que pueda convertirse significativamente a cadena con números legibles dentro |

### Salidas

| Nombre | Tipo | Descripción |
| --- | --- | --- |
| `int` | `INT 𝌠` | Todos los números encontrados en la cadena con decimales truncados. |
| `float` | `FLOAT 𝌠` | Todos los números encontrados en la cadena como flotantes. |
| `string` | `STRING 𝌠` | Todos los números encontrados en la cadena convertidos a cadena como flotantes. |
| `count` | `INT` | Cantidad de números encontrados en el valor. |

