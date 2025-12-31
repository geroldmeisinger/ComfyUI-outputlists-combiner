## OutputLists Pörun

![OutputLists Pörun](CombineOutputLists/CombineOutputLists.png)

(ComfyUI vinnusaga included)

Tekur upp að 4 OutputLists og býr til hverja pörun af þeim.

Dæmi: `[1, 2, 3] x ["A", "B"] = [(1, "A"), (1, "B"), (2, "A"), (2, "B"), (3, "A"), (3, "B")]`

`unzip_a` .. `unzip_d` notar `is_output_list=True` (merkt með tákninu `𝌠`) og verður meðhöndlað síður af samsvarandi nodes.

Öll listarnir eru valfrjálsir og tóm listi verða hunsaðir.

Á stefnumáta reiknar það *Cartesian product* og skilar hverri pörun með því að skipta upp í einingar (`unzip`), á meðan tóm listi verða skiptir út fyrir einingar af `None` og þær skila `None` á viðeigandi úttaki.

Dæmi: `[1, 2] x [] x ["A", "B"] x [] = [(1, None, "A", None), (1, None, "B", None), (2, None, "A", None), (2, None, "B", None)]`

### Inntök

| Nafn | Tegund | Lýsing |
| --- | --- | --- |
| `list_a` | `*` | (valfrjáls) |
| `list_b` | `*` | (valfrjáls) |
| `list_c` | `*` | (valfrjáls) |
| `list_d` | `*` | (valfrjáls) |

### Úttak

| Nafn | Tegund | Lýsing |
| --- | --- | --- |
| `unzip_a` | `* 𝌠` | Gildi pöranna sem samsvara `list_a`. |
| `unzip_b` | `* 𝌠` | Gildi pöranna sem samsvara `list_b`. |
| `unzip_c` | `* 𝌠` | Gildi pöranna sem samsvara `list_c`. |
| `unzip_d` | `* 𝌠` | Gildi pöranna sem samsvara `list_d`. |
| `index` | `INT 𝌠` | Svið frá 0..count sem hægt er að nota sem index. |
| `count` | `INT` | Heildarfjöldi pörna. |

