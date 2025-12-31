## XYZ-GridPlot

![XYZ-GridPlot](XyzGridPlot/XyzGridPlot.png)

(ComfyUI workflow incluso)

Genera un XYZ-Gridplot da una lista di immagini.
Prende una lista di immagini (incluse le batch) e le appiattisce in una lunga lista prima (quindi `batch_size=1`).

**Forma della griglia**
Determina la forma della griglia tramite:
1. il numero di etichette di riga
2. il numero di etichette di colonna
3. le immagini secondarie rimanenti.
Puoi usare `order=inside_out` per invertire la selezione delle immagini (utile se `batch_size>1` e vuoi etichettare le batch).

**Allineamento**
* Se un'etichetta va a capo nella riga successiva l'intero asse viene considerato "multiriga" e viene allineato in alto con spaziatura giustificata.
* Se tutte le etichette sono numeri o terminano in numeri (es. `strength: 1.`) l'intero asse viene considerato "numerico" e viene allineato a destra.
* Tutti gli altri testi vengono considerati "singola riga" e vengono allineati al centro.
* Allinea le etichette singole e numeriche per le colonne in basso, e per le righe le allinea verticalmente al centro.

**Dimensione del carattere**
* L'altezza dell'area delle etichette di colonna è determinata da `font_size` o da `la metà dell'altezza del più grande pacchetto di immagini secondarie in qualsiasi riga` (quello che è maggiore).
* La larghezza dell'area delle etichette di riga è determinata dalla larghezza massima del pacchetto di immagini secondarie (con un minimo di 256px).
* Il testo viene ridimensionato fino a quando non si adatta (fino a `font_size_min=6`) e utilizza la stessa dimensione del carattere per l'intero asse (etichette di riga o di colonna).
Se la dimensione del carattere è già al minimo, taglia qualsiasi testo rimanente.

**Pacchetto di immagini secondarie**
Modella le immagini secondarie (di solito dalle batch) nella zona più quadrata (il "pacchetto di immagini secondarie"), a meno che `output_is_list=True`, in tal caso utilizza solo un'immagine per cella e crea una lista di griglie intere di immagini.
Puoi usare questa lista di griglie di immagini per collegare un altro nodo XyzGridPlot per creare super-griglie.
Se le immagini secondarie consistono in batch di dimensioni diverse, riempe le celle mancanti con immagini vuote.
Il numero di immagini per cella (incluse le immagini batch) deve essere un multiplo di `rows * columns`.

### Input

| Nome | Tipo | Descrizione |
| --- | --- | --- |
| `images` | `IMAGE` | Una lista di immagini (incluse le batch) |
| `row_labels` | `*` | Testi delle etichette di riga sul lato sinistro |
| `col_labels` | `*` | Testi delle etichette di colonna in alto |
| `gap` | `INT` | Spazio tra i pacchetti di immagini secondarie. Nota che all'interno delle immagini secondarie non viene usato alcuno spazio. Se vuoi uno spazio tra le immagini secondarie collega un altro nodo XyzGridPlot. |
| `font_size` | `FLOAT` | Dimensione del carattere desiderata. Il testo verrà ridimensionato fino a quando non si adatta (fino a `font_size_min=6`). |
| `row_label_orientation` | `COMBO` | Orientamento del testo delle etichette di riga. Utile se vuoi risparmiare spazio. |
| `order` | `BOOLEAN` | Definisce l'ordine in cui le immagini devono essere elaborate. Questo è rilevante solo se hai immagini secondarie. Utile se `batch_size>1` e vuoi tracciare le batch. |
| `output_is_list` | `BOOLEAN` | Questo è rilevante solo se hai immagini secondarie o vuoi creare super-griglie. |

### Output

| Nome | Tipo | Descrizione |
| --- | --- | --- |
| `image` | `IMAGE 𝌠` | L'immagine XYZ-GridPlot. Se `output_is_list=True` crea una lista di immagini che puoi collegare a un altro nodo XYZ-GridPlot per creare super-griglie. |

