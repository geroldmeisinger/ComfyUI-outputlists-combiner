<!-- This file was auto-translated with a local LLM and last updated on 2025-12-27. -->
## Combinazioni delle OutputLists

![Combinazioni delle OutputLists](CombineOutputLists/CombineOutputLists.png)

(workflow ComfyUI incluso)

Accetta fino a 4 OutputLists e genera tutte le loro combinazioni.

Esempio: `[1, 2, 3] x ["A", "B"] = [(1, "A"), (1, "B"), (2, "A"), (2, "B"), (3, "A"), (3, "B")]`

`unzip_a` .. `unzip_d` utilizzano `is_output_list=True` (indicato dal simbolo `𝌠`) e verranno elaborati sequenzialmente dai nodi corrispondenti.

Tutte le liste sono opzionali e le liste vuote verranno ignorate.

Tecnicamente calcola il *prodotto cartesiano* e restituisce ogni combinazione suddivisa nei suoi elementi (`unzip`), mentre le liste vuote verranno sostituite con valori `None` e emetteranno `None` sull'output corrispondente.

Esempio: `[1, 2] x [] x ["A", "B"] x [] = [(1, None, "A", None), (1, None, "B", None), (2, None, "A", None), (2, None, "B", None)]`

### Input

| Nome | Tipo | Descrizione |
| --- | --- | --- |
| `list_a` | `*` | (opzionale) |
| `list_b` | `*` | (opzionale) |
| `list_c` | `*` | (opzionale) |
| `list_d` | `*` | (opzionale) |

### Output

| Nome | Tipo | Descrizione |
| --- | --- | --- |
| `unzip_a` | `* 𝌠` | Valore delle combinazioni corrispondenti a `list_a`. |
| `unzip_b` | `* 𝌠` | Valore delle combinazioni corrispondenti a `list_b`. |
| `unzip_c` | `* 𝌠` | Valore delle combinazioni corrispondenti a `list_c`. |
| `unzip_d` | `* 𝌠` | Valore delle combinazioni corrispondenti a `list_d`. |
| `index` | `INT 𝌠` | Intervallo da 0 a count che può essere usato come indice. |
| `count` | `INT` | Numero totale di combinazioni. |

