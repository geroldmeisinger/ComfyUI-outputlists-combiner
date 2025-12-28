<!-- This file was auto-translated with a local LLM and last updated on 2025-12-28. -->
## Converti in Intero, Float, Stringa

![Converti in Intero, Float, Stringa](ConvertNumberToIntFloatStr/ConvertNumberToIntFloatStr.png)

(Workflow ComfyUI incluso)

Convertisce qualsiasi valore numerico in `INT`, `FLOAT`, `STRING`.
Utilizza internamente `nums_from_string.get_nums`, che è molto permissivo nei numeri che accetta. Qualsiasi valore, da interi reali, da float reali, da stringhe contenenti interi o float, da stringhe che contengono più numeri con separatori di migliaia.
Usa una stringa come `123;234;345` per generare rapidamente una lista di numeri. Non usare le virgole come separatori, poiché potrebbero essere interpretate come separatori di migliaia.
`int`, `float` e `string` usano `is_output_list=True` (indicato dal simbolo `𝌠`) e saranno elaborati sequenzialmente dai nodi corrispondenti.

### Input

| Nome | Tipo | Descrizione |
| --- | --- | --- |
| `any` | `*` | Qualsiasi cosa che può essere convertita in una stringa con numeri leggibili all'interno |

### Output

| Nome | Tipo | Descrizione |
| --- | --- | --- |
| `int` | `INT 𝌠` | Tutti i numeri trovati nella stringa con i decimali troncati. |
| `float` | `FLOAT 𝌠` | Tutti i numeri trovati nella stringa come float. |
| `string` | `STRING 𝌠` | Tutti i numeri trovati nella stringa convertiti in stringa come float. |
| `count` | `INT` | Quantità di numeri trovati nel valore. |

