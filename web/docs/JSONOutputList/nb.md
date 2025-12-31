## JSON OutputList

![JSON OutputList](JSONOutputList/JSONOutputList.png)

(ComfyUI workflow inkludert)

Oppretter en OutputList ved å trekke ut arrayer eller ordbøker fra JSON-objekter.
Bruker JSONPath-syntaks for å trekke ut verdiene, se [JSONPath på Wikipedia](https://en.wikipedia.org/wiki/JSONPath).
Alle matchede verdier blir flattet inn i en lang liste.
Du kan også bruke denne noden til å lage objekter fra litterale strenger som `[1, 2, 3]`.
`key`, `value`, `int` og `float` bruker `is_output_list=True` (indikert med symbolet `𝌠`) og vil bli prosessert sekvensielt av tilsvarende noder.

### Innputter

| Navn | Type | Beskrivelse |
| --- | --- | --- |
| `jsonpath` | `STRING` | JSONPath som brukes til å trekke ut verdiene. |
| `json` | `STRING` | En JSON-streng som blir oversatt til et objekt. |
| `obj` | `*` | (valgfritt) objekt av hvilken som helst type som erstatter JSON-strengen |

### Utputter

| Navn | Type | Beskrivelse |
| --- | --- | --- |
| `key` | `STRING 𝌠` | Nøkkelen for ordbøker eller indeksen for arrayer (som streng). Teknisk sett er det en global indeks for den flattede listen for alle ikke-nøkler. |
| `value` | `STRING 𝌠` | Verdien som en streng. |
| `int` | `INT 𝌠` | Verdien som et heltall (hvis det ikke kan tolke tallet, bruker standardverdi 0). |
| `float` | `FLOAT 𝌠` | Verdien som et flyttall (hvis det ikke kan tolke tallet, bruker standardverdi 0). |
| `count` | `INT` | Totalt antall elementer i den flattede listen |
| `debug` | `STRING` | Feilsøkingsoutput av alle matchede objekter som en formatert JSON-streng |

