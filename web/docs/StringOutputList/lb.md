## String OutputList

![String OutputList](StringOutputList/StringOutputList.png)

(ComfyUI workflow d'ofgesech)

Erstellt e OutputList duerch de String an der Textfeld mat engem Separator ze spännen.
`value` an `index` benotzen (s) `is_output_list=True` (indizéiert duerch den Symbol `𝌠`) an ginn sequentiell duerch d'entspriechend Nodes verarbeit.

### Input

| Numm | Typ | Beschreiwung |
| --- | --- | --- |
| `separator` | `STRING` | De String, de fir d'Textfeld-Wäerter ze spännen benotzt gëtt. |
| `values` | `STRING` | De Text, de Dir an eng Lëscht spännen wëllt. Opgepasst, well de String vun tréngenden Newlines virun dem Spännen gestrëngt gëtt, an all Element wäert wéider vun Leeschräume gestrëngt gëtt. |

### Output

| Numm | Typ | Beschreiwung |
| --- | --- | --- |
| `value` | `* 𝌠` | D'Wäerter vun der Lëscht. |
| `index` | `INT 𝌠` | Beräich vun 0..count. Dir kënnt dës als Index benotzen. |
| `count` | `INT` | D'Zuel vun Elementer an der Lëscht. |
| `inspect_combo` | `COMBO` | E Dummy-Output, de Dir fir e Link mat engem `COMBO` benotzen an mat dëse Wäerter vufëllen kënnt. D'Verbindung gëtt da automatesch op d'`value` Output reverbond. |

