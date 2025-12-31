## JSON OutputList

![JSON OutputList](JSONOutputList/JSONOutputList.png)

(ComfyUI workflow inclus)

Creează o listă de ieșire prin extragerea array-urilor sau a dicțiunarelor din obiecte JSON.
Folosește sintaxa JSONPath pentru a extrage valorile, vezi [JSONPath pe Wikipedia](https://en.wikipedia.org/wiki/JSONPath).
Toate valorile potrivite sunt aplatizate într-o listă lungă.
De asemenea, poți folosi acest nod pentru a crea obiecte din șiruri literale precum `[1, 2, 3]`.
`key`, `value`, `int` și `float` folosesc `is_output_list=True` (indicat de simbolul `𝌠`) și vor fi procesate secvențial de nodurile corespunzătoare.

### Intrări

| Nume | Tip | Descriere |
| --- | --- | --- |
| `jsonpath` | `STRING` | JSONPath folosit pentru a extrage valorile. |
| `json` | `STRING` | Un șir JSON care este tradus într-un obiect. |
| `obj` | `*` | (opțional) obiect de orice tip care va înlocui șirul JSON |

### Ieșiri

| Nume | Tip | Descriere |
| --- | --- | --- |
| `key` | `STRING 𝌠` | Cheia pentru dicțiuni sau index pentru array-uri (ca șir). Tehnic, este un index global al listei aplatizate pentru toate valorile care nu sunt chei. |
| `value` | `STRING 𝌠` | Valoarea ca șir. |
| `int` | `INT 𝌠` | Valoarea ca int (dacă nu poate analiza numărul, valoarea implicită este 0). |
| `float` | `FLOAT 𝌠` | Valoarea ca float (dacă nu poate analiza numărul, valoarea implicită este 0). |
| `count` | `INT` | Numărul total de elemente din lista aplatizată |
| `debug` | `STRING` | Ieșirea de depanare a tuturor obiectelor potrivite ca șir JSON formatat |

