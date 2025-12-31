## String OutputList

![String OutputList](StringOutputList/StringOutputList.png)

(ComfyUI workflow inkludert)

Oppretter en OutputList ved å dele strengen i tekstfeltet med en separator.
`value` og `index` bruker `is_output_list=True` (indikert av symbolet `𝌠`) og vil bli behandlet sekvensielt av tilsvarende noder.

### Innputter

| Navn | Type | Beskrivelse |
| --- | --- | --- |
| `separator` | `STRING` | Strengen som brukes til å dele tekstfeltverdiene etter. |
| `values` | `STRING` | Teksten du vil dele opp i en liste. Merk at strengen fjerner etterfølgende linjeskift før oppdeling, og hvert element fjernes også av mellomrom. |

### Utputter

| Navn | Type | Beskrivelse |
| --- | --- | --- |
| `value` | `* 𝌠` | Verdiene fra listen. |
| `index` | `INT 𝌠` | Område fra 0..count. Du kan bruke denne som et indeks. |
| `count` | `INT` | Antall elementer i listen. |
| `inspect_combo` | `COMBO` | En dummy-utgang du kan bruke til å koble til en `COMBO` og forhåndsutfylle med dens verdier. Koblingen vil da automatisk bli omlinket til `value`-utgangen. |

