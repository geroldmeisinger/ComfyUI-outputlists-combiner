<!-- This file was auto-translated with a local LLM and last updated on 2025-12-28. -->
## Cunvertire in Int, Float, Str

![Cunvertire in Int, Float, Str](ConvertNumberToIntFloatStr/ConvertNumberToIntFloatStr.png)

(Workflow de ComfyUI inclusu)

Cunverte cunte de numeru in `INT` `FLOAT` `STRING`.
A s’usat `nums_from_string.get_nums` internamente, che estende in maniera molto permissiva in sa numeru che accetta. Cunte de numeri reales, numeri reales, numeri o numeri reales in forma de stringa, stringas che contengen numeru in forma de numeru con separadores de migghi.
S’usat una stringa `123;234;345` pro cunvertire in forma de lista de numeru. No s’usat comas come separadores, ca podentessere interpretados come separadores de migghi.
`int`, `float` e `string` usan `is_output_list=True` (indicadu cun o simbolo `𝌠`) e s’arrobànnu sequenzialmente pro nodos corrispondentes.

### S’entradas

| S’istru | Tipu | Descrizione |
| --- | --- | --- |
| `any` | `*` | Cualsieta che podet esse cunvertite in forma de stringa cun numeru interpretabile dinte |

### S’uscidas

| S’istru | Tipu | Descrizione |
| --- | --- | --- |
| `int` | `INT 𝌠` | Tutus i numerus cuntròttu in sa stringa cun decimales troncatos. |
| `float` | `FLOAT 𝌠` | Tutus i numerus cuntròttu in sa stringa in forma de float. |
| `string` | `STRING 𝌠` | Tutus i numerus cuntròttu in sa stringa in forma de float cunvertidos in stringa. |
| `count` | `INT` | Quantità de numerus cuntròttu in sa valura. |

