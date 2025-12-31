## Number OutputList

![Number OutputList](NumberOutputList/NumberOutputList.png)

(ComfyUI workflow iekļauts)

Izveido OutputList ar skaitliskām vērtībām diapazonā.
Iekšēji izmanto [numpy.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html), jo tas darbojas uzticamāk ar peldošā punkta vērtībām.
Ja vēlaties definēt skaitļu sarakstus ar patvaļīgiem soliem, pārbaudiet JSON OutputList un definējiet masīvu, piemēram, `[1, 42, 123]`.
`int`, `float`, `string` un `index` izmanto `is_output_list=True` (atspoguļots ar simbolu `𝌠`) un tiks apstrādāti secīgi ar atbilstošiem mezgliem.

### Ievades

| Nosaukums | Tips | Apraksts |
| --- | --- | --- |
| `start` | `FLOAT` | Sākuma vērtība, no kuras ģenerēt diapazonu. |
| `stop` | `FLOAT` | Beigu vērtība. Ja `endpoint=include`, tad šī skaitlis iekļaujas sarakstā. |
| `num` | `INT` | Saraksta elementu skaits (nejauši to nejauši sajaukt ar `step`). |
| `endpoint` | `BOOLEAN` | Lēšana, vai `stop` vērtība jāiekļauj vai jāizslēdz no elementiem. |

### Izvades

| Nosaukums | Tips | Apraksts |
| --- | --- | --- |
| `int` | `INT 𝌠` | Vērtība, konvertēta uz int (noapaļota uz leju). |
| `float` | `FLOAT 𝌠` | Vērtība kā float. |
| `string` | `STRING 𝌠` | Vērtība kā float, konvertēta uz virkni. |
| `index` | `INT 𝌠` | 0..count diapazons, ko var izmantot kā indeksu. |
| `count` | `INT` | Tas pats, kas `num`. |

