<!-- This file was auto-translated with a local LLM and last updated on 2025-12-28. -->
## Breyta í Heiltölu Flokkur Strengur

![Breyta í Heiltölu Flokkur Strengur](ConvertNumberToIntFloatStr/ConvertNumberToIntFloatStr.png)

(ComfyUI vinnubók innifalið)

Breytir hvaða sem er tölulegum gildi í `HEILTLIÐ`, `FLOKKUR`, `STRENGUR`.
Notar `nums_from_string.get_nums` innan sem er mjög leyfileg í tölurnar sem hún tekur við. Hvaða sem er frá raunverulegum heiltölum, raunverulegum flokkum, heiltölum eða flokkum sem strengir, strengum sem innihalda margar tölur með þúsundundir.
Notaðu strenginn `123;234;345` til að fljótt búa til listann af tölum. Notaðu ekki kommur sem aðgreinir vegna þess að þær gætu verið toludýrðar sem þúsundundir.
`heiltala`, `flokkur` og `strengur` notar `is_output_list=True` (táknað með táknið `𝌠`) og verður að röðuð fyrir samsíða aðgerð á samsíða hnútum.

### Inntök

| Nafn | Gerð | Lýsing |
| --- | --- | --- |
| `eftir` | `*` | Hvaða sem er sem getur verið skilgreint sem streng með lesanlegum tölum inni |

###Úttök

| Nafn | Gerð | Lýsing |
| --- | --- | --- |
| `heiltala` | `HEILTLIÐ 𝌠` | Allar tölur fundnar í strengnum með desimaltölum hættu. |
| `flokkur` | `FLOKKUR 𝌠` | Allar tölur fundnar í strengnum sem flokkar. |
| `strengur` | `STRENGUR 𝌠` | Allar tölur fundnar í strengnum sem flokkar breytt í streng. |
| `margfeldi` | `HEILTLIÐ` | Fjöldi tala sem fundust í gildinu. |

