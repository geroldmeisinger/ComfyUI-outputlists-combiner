## Streng OutputList

![Streng OutputList](StringOutputList/StringOutputList.png)

(ComfyUI workflow inkluderet)

Opretter en OutputList ved at opdele strengen i tekstfeltet med en separator.
`value` og `index` bruger `is_output_list=True` (angivet af symbolet `𝌠`) og vil blive behandlet sekventielt af tilsvarende noder.

### Input

| Navn | Type | Beskrivelse |
| --- | --- | --- |
| `separator` | `STRENG` | Strengen der bruges til at opdele tekstfeltværdierne efter. |
| `values` | `STRENG` | Den tekst du vil opdele i en liste. Bemærk at strengen beskæres for efterfølgende linjeskift før opdeling, og hvert element beskæres igen for mellemrum. |

### Output

| Navn | Type | Beskrivelse |
| --- | --- | --- |
| `value` | `* 𝌠` | Værdierne fra listen. |
| `index` | `HELTAL 𝌠` | Intervallet 0..count. Du kan bruge dette som et index. |
| `count` | `HELTAL` | Antal elementer i listen. |
| `inspect_combo` | `COMBO` | En dummy-output du kan bruge til at forbinde til en `COMBO` og forudfyldes med dens værdier. Forbindelsen vil derefter automatisk blive genforbundet til `value` output. |

