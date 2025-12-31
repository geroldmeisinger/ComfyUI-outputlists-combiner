## Kichanganyiko cha Kufanana

![Kichanganyiko cha Kufanana](WorkflowDiscriminator/WorkflowDiscriminator.png)

(ComfyUI workflow imejazwa)

Inachanganya mifano ya workflow na kufanana ili kutoa thamani tofauti kama orodha za matokeo.
Unaweza kutumia kichaguo hiki ili kurejesha jinsi kila picha ilivyotengenezwa kutoka kwa orodha ya picha zilizo na workflow sawa.
Kumbuka kwamba `IMAGE` ya ComfyUI haija na metadata ya workflow na unahitaji kupakia picha kwa kutumia kivinjari maalum za picha+metadata na kuunganisha metadata kwa kichaguo hiki.
Vikichwa vya kufanana vya kuvutia metadata vinajumuisha:
* `Load Any File.metadata` -> `JSON OutputList(jsonpath=$.["PNG:Prompt"]).value`
* [Crystool](https://github.com/crystian/ComfyUI-Crystools) `🪛 Load image with metadata.Metadata RAW` -> `🪛 Metadata extractor.prompt`
* [Simple_Readable_Metadata](https://github.com/ShammiG/ComfyUI-Simple_Readable_Metadata-SG) `Simple Readable Metadata-SG.metadata_raw`

### Ingizo

| Jina | Aina | Maelezo |
| --- | --- | --- |
| `objs_0` | `*` | (si lazima) Kitu moja (au orodha ya vitu), kwa kawaida cha workflow. `objs_0` na `more_objs` zitapangwa pamoja na kuwa kwa faida, ikiwa unataka kufanana vitu viwili. |
| `more_objs` | `*` | (si lazima) Kitu kingine (au orodha ya vitu), kwa kawaida cha workflow. `objs_0` na `more_objs` zitapangwa pamoja na kuwa kwa faida, ikiwa unataka kufanana vitu viwili. |
| `ignore_jsonpaths` | `STRING` | (si lazima) Orodha ya JSONPaths za kupuuza ikiwa unataka kufanana vichaguo vingi. |

### Pato

| Jina | Aina | Maelezo |
| --- | --- | --- |
| `list_a` | `* 𝌠` |  |
| `list_b` | `* 𝌠` |  |
| `list_c` | `* 𝌠` |  |
| `list_d` | `* 𝌠` |  |
| `jsonpaths` | `STRING 𝌠` |  |

