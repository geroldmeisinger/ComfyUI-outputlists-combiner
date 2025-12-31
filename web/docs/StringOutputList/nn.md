## String OutputList

![String OutputList](StringOutputList/StringOutputList.png)

(ComfyUI workflow inkludert)

Lagar ein OutputList ved å dela opp strengen i tekstfeltet med ein separator.
`value` og `index` brukar `is_output_list=True` (indikert av symbolet `𝌠`) og vil bli handsama sekvensielt av tilhøyrande noder.

### Innputar

| Namn | Type | Description |
| --- | --- | --- |
| `separator` | `STRING` | Strengen som blir brukt til å dela opp tekstfeltverdiane. |
| `values` | `STRING` | Teksten du vil dela opp i ei liste. Merk at strengen blir fjerna av linjeskift bakerst før den blir delt, og kvart element blir fjerna av mellomrom. |

### Utputar

| Namn | Type | Description |
| --- | --- | --- |
| `value` | `* 𝌠` | Verdiane frå lista. |
| `index` | `INT 𝌠` | Rekkje 0..count. Du kan bruke denne som ein indeks. |
| `count` | `INT` | Talet på element i lista. |
| `inspect_combo` | `COMBO` | Eit dummy-utgang du kan bruke til å kopla til ein `COMBO` og fylle med verdiane. Tilkoplinga blir då automatisk kopla om til `value`-utgang. |

