## String OutputList

![String OutputList](StringOutputList/StringOutputList.png)

(ComfyUI vinnusvæði included)

Býr til OutputList með því að skipta strenginum í textareitnum með aðskiljare. 
`value` og `index` notar `is_output_list=True` (sýnt með tákninu `𝌠`) og verður þá meðhöndlað síðan af samsvarandi node.

### Inntök

| Nafn | Gerð | Lýsing |
| --- | --- | --- |
| `separator` | `STRING` | Strengurinn sem notaður er til að skipta textareitnum. |
| `values` | `STRING` | Textinn sem þú vilt skipta í lista. Athugaðu að strengurinn er skurður af afgangandi línum áður en skipt er, og hvert atriði er aftur skurður af bilum. |

### Úttök

| Nafn | Gerð | Lýsing |
| --- | --- | --- |
| `value` | `* 𝌠` | Gildin frá listanum. |
| `index` | `INT 𝌠` | Svið 0..count. Þú getur notað þetta sem index. |
| `count` | `INT` | Fjöldi atriða í listanum. |
| `inspect_combo` | `COMBO` | Dummy-úttak sem þú getur notað til að tengja við `COMBO` og fylla það með gildunum. Tengingin verður þá sjálfkrafa endurtengd `value` úttaki. |

