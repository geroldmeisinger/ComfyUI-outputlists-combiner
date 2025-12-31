## Tal OutputList

![Tal OutputList](NumberOutputList/NumberOutputList.png)

(ComfyUI workflow inkluderet)

Opretter en OutputList med et interval af numeriske værdier.
Bruger [numpy.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html) internt, fordi det fungerer mere pålideligt med flydende punkt-værdier.
Hvis du vil definere tal-lister med vilkårlige trin, tjek da JSON OutputList og definer en array, f.eks. `[1, 42, 123]`.
`int`, `float`, `string` og `index` bruger `is_output_list=True` (angivet af symbolet `𝌠`) og vil blive behandlet sekventielt af tilsvarende noder.

### Input

| Navn | Type | Beskrivelse |
| --- | --- | --- |
| `start` | `FLYDENDE TAL` | Startværdi for at generere intervallet fra. |
| `stop` | `FLYDENDE TAL` | Slutværdi. Hvis `endpoint=include` så er denne værdi inkluderet i listen. |
| `num` | `HELTAL` | Antallet af elementer i listen (forveksl ikke med et `trin`). |
| `endpoint` | `BOOLEAN` | Bestemmer om `stop` værdien skal inkluderes eller ekskluderes i elementerne. |

### Output

| Navn | Type | Beskrivelse |
| --- | --- | --- |
| `int` | `HELTAL 𝌠` | Værdien konverteret til heltal (rundet ned/floored). |
| `float` | `FLYDENDE TAL 𝌠` | Værdien som et flydende tal. |
| `string` | `STRENG 𝌠` | Værdien som et flydende tal konverteret til streng. |
| `index` | `HELTAL 𝌠` | Intervallet 0..count som kan bruges som et index. |
| `count` | `HELTAL` | Samme som `num`. |

