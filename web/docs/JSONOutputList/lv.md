## JSON OutputList

![JSON OutputList](JSONOutputList/JSONOutputList.png)

(ComfyUI workflow iekļauts)

Izveido OutputList, izvelkot masīvus vai vārdnīcas no JSON objektiem.
Izmanto JSONPath sintaksi, lai izvilktu vērtības, skat. [JSONPath Wikipedia](https://en.wikipedia.org/wiki/JSONPath) .
Visas atbilstošās vērtības tiek izlīdzinātas vienā garā sarakstā.
Jūs varat arī izmantot šo mezglu, lai izveidotu objektus no burtālajām virknēm, piemēram, `[1, 2, 3]`.
`key`, `value`, `int` un `float` izmanto `is_output_list=True` (apzīmēts ar simbolu `𝌠`) un tiks apstrādāti secīgi ar atbilstošajiem mezgliem.

### Ievades

| Nosaukums | Tips | Apraksts |
| --- | --- | --- |
| `jsonpath` | `STRING` | JSONPath, kas tiek izmantots, lai izvilktu vērtības. |
| `json` | `STRING` | JSON virkne, kas tiek pārveidota uz objektu. |
| `obj` | `*` | (papildus) objekts jebkura tipa, kas aizstās JSON virkni |

### Izvades

| Nosaukums | Tips | Apraksts |
| --- | --- | --- |
| `key` | `STRING 𝌠` | Atslēga vārdnīcām vai indekss masīviem (kā virkne). Tehniski tas ir globālais indekss izlīdzinātā sarakstā visiem ne-atlēgām. |
| `value` | `STRING 𝌠` | Vērtība kā virkne. |
| `int` | `INT 𝌠` | Vērtība kā vesels skaitlis (ja nevar parsēt skaitli, noklusējuma vērtība ir 0). |
| `float` | `FLOAT 𝌠` | Vērtība kā decimālskaitlis (ja nevar parsēt skaitli, noklusējuma vērtība ir 0). |
| `count` | `INT` | Kopējais vienību skaits izlīdzinātā sarakstā |
| `debug` | `STRING` | Atkļūdošanas izvade ar visiem atbilstošajiem objektiem kā formatēta JSON virkne |

