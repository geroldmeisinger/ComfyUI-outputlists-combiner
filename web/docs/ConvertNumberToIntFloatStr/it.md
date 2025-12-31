## Converti in Intero, Virgola Mobile, Stringa

![Converti in Intero, Virgola Mobile, Stringa](ConvertNumberToIntFloatStr/ConvertNumberToIntFloatStr.png)

(ComfyUI workflow incluso)

Converte qualsiasi cosa di tipo numerico in `INTERO` `VIRGOLA_MOBILE` `STRINGA`.
Utilizza internamente `nums_from_string.get_nums` che è molto permissiva nel tipo di numeri che accetta. Accetta qualsiasi cosa tra numeri interi effettivi, numeri in virgola mobile effettivi, interi o numeri in virgola mobile come stringhe, stringhe che contengono più numeri con separatori delle migliaia.
Usa una stringa `123;234;345` per generare rapidamente una lista di numeri. Non usare le virgole come separatori poiché potrebbero essere interpretate come separatori delle migliaia.
`int`, `float` e `string` usano `is_output_list=True` (indicato dal simbolo `𝌠`) e saranno elaborati sequenzialmente dai nodi corrispondenti.

### Input

| Nome | Tipo | Descrizione |
| --- | --- | --- |
| `any` | `*` | Qualsiasi cosa che possa essere convertita in modo significativo in una stringa con numeri analizzabili al suo interno |

### Output

| Nome | Tipo | Descrizione |
| --- | --- | --- |
| `int` | `INTERO 𝌠` | Tutti i numeri trovati nella stringa con la parte decimale eliminata. |
| `float` | `VIRGOLA_MOBILE 𝌠` | Tutti i numeri trovati nella stringa come virgola mobile. |
| `string` | `STRINGA 𝌠` | Tutti i numeri trovati nella stringa come virgola mobile convertiti in stringa. |
| `count` | `INTERO` | Quantità di numeri trovati nel valore. |

