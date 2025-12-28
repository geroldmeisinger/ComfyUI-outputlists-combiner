<!-- This file was auto-translated with a local LLM and last updated on 2025-12-28. -->
## Konvète a Int Float Str

![Konvète a Int Float Str](ConvertNumberToIntFloatStr/ConvertNumberToIntFloatStr.png)

(Workflow ComfyUI yon kote)

Konvète tout chose ki se pare a `INT` `FLOAT` `STRING`.
Fèt utilisation `nums_from_string.get_nums` ki a kapab akseptèt tout chose ki se pare a nivo. Tout chose ki se pare a entèy, flot, entèy oswa flot ki se pare a chif, chif ki genyen plis d'entèy ak sèparatè kilyon.
Fèt utilisation chif `123;234;345` pou genyen list chif. Pase pas koma pou sèparatè, pouke yo kapab genyen sèparatè kilyon.
`int`, `float` ak `string` fèt utilisation `is_output_list=True` (indikat pa simbol `𝌠`) ak genyen procese sekwansial pa nòd korespondan.

### Alòt

| Nom | Tip | Deskripsyon |
| --- | --- | --- |
| `any` | `*` | Tout chose ki kapab konvète a chif pou genyen chif kapab analizye |

### Ouput

| Nom | Tip | Deskripsyon |
| --- | --- | --- |
| `int` | `INT 𝌠` | Tòt chif genyen dèy a chif ki genyen dèy a ak desimèl kapab tronke. |
| `float` | `FLOAT 𝌠` | Tòt chif genyen dèy a chif ki genyen dèy a ak flot. |
| `string` | `STRING 𝌠` | Tòt chif genyen dèy a chif ki genyen dèy a ak flot konvète a chif. |
| `count` | `INT` | Nivo chif genyen dèy a. |

