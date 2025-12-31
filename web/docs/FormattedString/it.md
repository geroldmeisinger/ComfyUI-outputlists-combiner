## Stringa Formattata

![Stringa Formattata](FormattedString/FormattedString.png)

(ComfyUI workflow incluso)

Crea una stringa che contiene variabili segnaposto e le sostituisce con i rispettivi valori.
Utilizza internamente `str.format()` di Python, vedi [Python - Sintassi Stringa di Formattazione](https://docs.python.org/3/library/string.html#format-string-syntax) .
* Puoi usare `{a:.2f}` per arrotondare un numero in virgola mobile a 2 decimali.
* Puoi usare `{a:05d}` per riempire con fino a 5 zeri iniziali per adattarsi al suffisso del nome file di Comfy `ComfyUI_00001_.png`.
* Se vuoi scrivere `{ }` all'interno delle stringhe (ad esempio per JSON) devi raddoppiarle: `{{ }}`.

Applica anche la sintassi *ricerca e sostituzione (R&S)* come `%date:yyyy-MM-dd hh:mm:ss%` e `%KSampler.seed%`.
Quindi puoi anche usarlo come un nodo `GET`.
Nota che la "ricerca e sostituzione" avviene nel contesto di JavaScript e viene eseguita prima dell'esecuzione del nodo.

### Input

| Nome | Tipo | Descrizione |
| --- | --- | --- |
| `fstring` | `STRINGA` | Crea una stringa che contiene variabili segnaposto e le sostituisce con i rispettivi valori.<br>Utilizza internamente `str.format()` di Python, vedi [Python - Sintassi Stringa di Formattazione](https://docs.python.org/3/library/string.html#format-string-syntax) .<br>* Puoi usare `{a:.2f}` per arrotondare un numero in virgola mobile a 2 decimali.<br>* Puoi usare `{a:05d}` per riempire con fino a 5 zeri iniziali per adattarsi al suffisso del nome file di Comfy `ComfyUI_00001_.png`.<br>* Se vuoi scrivere `{ }` all'interno delle stringhe (ad esempio per JSON) devi raddoppiarle: `{{ }}`.<br><br>Applica anche la sintassi *ricerca e sostituzione (R&S)* come `%date:yyyy-MM-dd hh:mm:ss%` e `%KSampler.seed%`.<br>Allora puoi anche usarlo come un nodo `GET`.<br>Nota che la "ricerca e sostituzione" avviene nel contesto di JavaScript e viene eseguita prima dell'esecuzione del nodo. |
| `a` | `*` | (opzionale) valore che verrà convertito in stringa al segnaposto `{a}`. |
| `b` | `*` | (opzionale) valore che verrà convertito in stringa al segnaposto `{b}`. |
| `c` | `*` | (opzionale) valore che verrà convertito in stringa al segnaposto `{c}`. |
| `d` | `*` | (opzionale) valore che verrà convertito in stringa al segnaposto `{d}`. |

### Output

| Nome | Tipo | Descrizione |
| --- | --- | --- |
| `string` | `STRINGA` | La stringa formattata con tutti i segnaposto sostituiti con i rispettivi valori. |

