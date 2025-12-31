## Streng OutputList

![Streng OutputList](StringOutputList/StringOutputList.png)

(ComfyUI workflow íðgu)

Gerir einn OutputList við at skilja strenginum í tekstfætini við einum separator.
`value` og `index` nýtir `is_output_list=True` (merkt við symbolið `𝌠`) og verða handtert í fylgjandi rætta av samsvarandi nodes.

### Inntak

| Navn | Slag | Lýsing |
| --- | --- | --- |
| `separator` | `STRING` | Strengurin ið nýtist til at skilja tekstfætini við. |
| `values` | `STRING` | Tekstin tú ynskir at skilja í einn lista. Tíðan er strengurin skeraður av truppu nýggjum línum áðrenn skiljan, og hvørjum item er einnig skeraður av whitespace. |

### Úttak

| Navn | Slag | Lýsing |
| --- | --- | --- |
| `value` | `* 𝌠` | Værdið frá lista. |
| `index` | `INT 𝌠` | Umráðið 0..count. Tú kanst nýta tað sum index. |
| `count` | `INT` | Tal av itemum í lista. |
| `inspect_combo` | `COMBO` | Einn dummy-úttak tú kanst nýta til at knýta til ein `COMBO` og fylla tað við tínum værdum. Tá knýtingin er gerð, verður tað sjálvvirkandi knýtt aftur til `value` úttaks. |

