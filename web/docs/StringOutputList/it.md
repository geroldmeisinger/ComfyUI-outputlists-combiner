## String OutputList

![String OutputList](StringOutputList/StringOutputList.png)

(ComfyUI workflow incluso)

Crea un OutputList suddividendo la stringa nel campo di testo con un separatore.
`value` e `index` usano `is_output_list=True` (indicato dal simbolo `𝌠`) e saranno elaborati sequenzialmente dai nodi corrispondenti.

### Input

| Nome | Tipo | Descrizione |
| --- | --- | --- |
| `separator` | `STRINGA` | La stringa utilizzata per suddividere i valori del campo di testo. |
| `values` | `STRINGA` | Il testo che desideri suddividere in una lista. Nota che la stringa viene tagliata delle nuove righe finali prima della suddivisione, e ogni elemento viene ulteriormente tagliato degli spazi vuoti. |

### Output

| Nome | Tipo | Descrizione |
| --- | --- | --- |
| `value` | `* 𝌠` | I valori dalla lista. |
| `index` | `INTERO 𝌠` | Intervallo da 0..count. Puoi usarlo come indice. |
| `count` | `INTERO` | Il numero di elementi nella lista. |
| `inspect_combo` | `COMBO` | Un output fittizio che puoi usare per collegarlo a un `COMBO` e precompilarlo con i suoi valori. La connessione verrà poi automaticamente ricollegata all'output `value`. |

