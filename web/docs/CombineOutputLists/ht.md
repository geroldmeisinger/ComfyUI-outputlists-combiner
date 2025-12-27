<!-- This file was auto-translated with a local LLM and last updated on 2025-12-27. -->
## Kombinasyon yo nan OutputLists

![Kombinasyon yo nan OutputLists](CombineOutputLists/CombineOutputLists.png)

(Workflow ComfyUI ki genyen)

Pèmèt konsidere jwenn kominasyon pou jwenn kominasyon nan kote kominasyon yo.

Exemple: `[1, 2, 3] x ["A", "B"] = [(1, "A"), (1, "B"), (2, "A"), (2, "B"), (3, "A"), (3, "B")]`

`unzip_a` .. `unzip_d` fèt utilisation `is_output_list=True` (indikat pa simbol `𝌠`) ak te fèt konsidere sekwansielman pa nòt ki korespond.

Tout liz la te fèt optional ak liz vide te ignore.

Tèkni, li kalkile *produkt kartezyen* ak genyen kominasyon ki fèt separe pou l'element (unzip), nan kote liz vide te remplace pa uniti `None` ak genyen `None` nan output korespondan.

Exemple: `[1, 2] x [] x ["A", "B"] x [] = [(1, None, "A", None), (1, None, "B", None), (2, None, "A", None), (2, None, "B", None)]`

### Alòt

| Mwen | Tip | Deskriyasyon |
| --- | --- | --- |
| `list_a` | `*` | (optional) |
| `list_b` | `*` | (optional) |
| `list_c` | `*` | (optional) |
| `list_d` | `*` | (optional) |

### Ouput

| Mwen | Tip | Deskriyasyon |
| --- | --- | --- |
| `unzip_a` | `* 𝌠` | Valeur nan kominasyon ki korespond `list_a`. |
| `unzip_b` | `* 𝌠` | Valeur nan kominasyon ki korespond `list_b`. |
| `unzip_c` | `* 𝌠` | Valeur nan kominasyon ki korespond `list_c`. |
| `unzip_d` | `* 𝌠` | Valeur nan kominasyon ki korespond `list_d`. |
| `index` | `INT 𝌠` | Ekip 0..count ki kapab fèt kòm index. |
| `count` | `INT` | Nomb kominasyon total. |

