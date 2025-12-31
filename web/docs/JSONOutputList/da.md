## JSON OutputList

![JSON OutputList](JSONOutputList/JSONOutputList.png)

(ComfyUI workflow inkluderet)

Opretter en OutputList ved at udpakke arrays eller dictionaries fra JSON objekter.
Bruger JSONPath syntaks til at udpakke værdierne, se [JSONPath på Wikipedia](https://en.wikipedia.org/wiki/JSONPath) .
Alle matchede værdier bliver fladt i en lang liste.
Du kan også bruge denne node til at oprette objekter fra litterale strenge som `[1, 2, 3]`.
`key`, `value`, `int` og `float` bruger `is_output_list=True` (angivet af symbolet `𝌠`) og vil blive behandlet sekventielt af tilsvarende noder.

### Input

| Navn | Type | Beskrivelse |
| --- | --- | --- |
| `jsonpath` | `STRENG` | JSONPath som bruges til at udpakke værdierne. |
| `json` | `STRENG` | En JSON streng som oversættes til et objekt. |
| `obj` | `*` | (valgfrit) objekt af enhver type som erstatter JSON strengen |

### Output

| Navn | Type | Beskrivelse |
| --- | --- | --- |
| `key` | `STRENG 𝌠` | Nøglen for dictionaries eller indekset for arrays (som streng). Teknisk set er det et globalt indeks for den flattede liste for alle ikke-nøgler. |
| `value` | `STRENG 𝌠` | Værdien som en streng. |
| `int` | `HELTAL 𝌠` | Værdien som et heltal (hvis det ikke kan parse tallet, bruger standardværdien 0). |
| `float` | `FLYDENDE TAL 𝌠` | Værdien som et flydende tal (hvis det ikke kan parse tallet, bruger standardværdien 0). |
| `count` | `HELTAL` | Totalt antal elementer i den flattede liste |
| `debug` | `STRENG` | Debug output af alle matchede objekter som en formateret JSON streng |

