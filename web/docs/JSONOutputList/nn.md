## JSON OutputList

![JSON OutputList](JSONOutputList/JSONOutputList.png)

(ComfyUI workflow inkludert)

Lagar ein OutputList ved å trekke ut arrayar eller ordbøker frå JSON-objekt.
Brukar JSONPath-syntaks for å trekke ut verdiane, sjå [JSONPath på Wikipedia](https://en.wikipedia.org/wiki/JSONPath) .
Alle samsvarende verdiar blir flatt i ein lang liste.
Du kan òg bruke denne noden til å lage objekt frå litterale strengar som `[1, 2, 3]`.
`key`, `value`, `int` og `float` brukar `is_output_list=True` (indikert av symbolet `𝌠`) og blir handsama sekvensielt av tilhøyrande noder.

### Inndata

| Namn | Type | Skildring |
| --- | --- | --- |
| `jsonpath` | `STRING` | JSONPath som blir brukt til å trekke ut verdiene. |
| `json` | `STRING` | Ein JSON-streng som blir omgjort til eit objekt. |
| `obj` | `*` | (valfritt) objekt av kva for ein type som helst som vil erstatt JSON-strengen |

### Utdata

| Namn | Type | Skildring |
| --- | --- | --- |
| `key` | `STRING 𝌠` | Nøkkelen for ordbøker eller indeksen for arrayar (som streng). Teknisk sett er det ein global indeks for den flattete lista for alle ikkje-nøklar. |
| `value` | `STRING 𝌠` | Verdien som ein streng. |
| `int` | `INT 𝌠` | Verdien som eit heiltal (viss det ikkje kan tolke talet, blir standardverdi 0). |
| `float` | `FLOAT 𝌠` | Verdien som eit flyttal (viss det ikkje kan tolke talet, blir standardverdi 0). |
| `count` | `INT` | Totalt tal på element i den flattete lista |
| `debug` | `STRING` | Feilsøkingsoutput av alle samsvarende objekt som ei formatert JSON-streng |

