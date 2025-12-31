## Number OutputList

![Number OutputList](NumberOutputList/NumberOutputList.png)

(ComfyUI workflow inclusă)

Creează o OutputList cu un interval de valori numerice.
Folosește intern [numpy.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html), deoarece funcționează mai fiabil cu valori de tip float.
Dacă dorești să definești liste de numere cu pași arbitrați, consultă JSON OutputList și definește un array, de exemplu `[1, 42, 123]`.
`int`, `float`, `string` și `index` folosesc `is_output_list=True` (indicat de simbolul `𝌠`) și vor fi procesate secvențial de nodurile corespunzătoare.

### Intrări

| Nume | Tip | Descriere |
| --- | --- | --- |
| `start` | `FLOAT` | Valoarea de start pentru generarea intervalului. |
| `stop` | `FLOAT` | Valoarea de sfârșit. Dacă `endpoint=include`, atunci această valoare este inclusă în listă. |
| `num` | `INT` | Numărul de elemente din listă (nu confunda cu un `step`). |
| `endpoint` | `BOOLEAN` | Determină dacă valoarea `stop` trebuie inclusă sau exclusă din elemente. |

### Ieșiri

| Nume | Tip | Descriere |
| --- | --- | --- |
| `int` | `INT 𝌠` | Valoarea convertită în int (rotunjită în jos/în timp). |
| `float` | `FLOAT 𝌠` | Valoarea ca float. |
| `string` | `STRING 𝌠` | Valoarea ca float convertită în string. |
| `index` | `INT 𝌠` | Interval de 0..count care poate fi folosit ca index. |
| `count` | `INT` | La fel ca `num`. |

