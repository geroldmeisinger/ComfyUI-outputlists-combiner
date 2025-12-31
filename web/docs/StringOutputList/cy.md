## Llwytho Ffeil Unrhyw

![Llwytho Ffeil Unrhyw](StringOutputList/StringOutputList.png)

(Cyflun ComfyUI wedi'i gynnwys)

Creu OutputList trwy rannu'r llinyn yn y maes testun â gwahanydd.
Defnyddir `value` a `index` `is_output_list=True` (nodwyd gan y symbol `𝌠`) a byddai'n cael ei brosesu yn dilynol gan nodau cyfatebol.

### Mewnbwn

| Enw | Math | Disgrifiad |
| --- | --- | --- |
| `separator` | `STRING` | Y llinyn a ddefnyddir i rannu gwerthoedd maes testun. |
| `values` | `STRING` | Y testun y dymuniwch ei rannu i restr. Sylwer bod y llinyn yn tynnu'r llinellau newline yn ddiweddar cyn rhannu, a bydd pob eitem yn tynnu'r bylchau ar y ffordd. |

### Allbwn

| Enw | Math | Disgrifiad |
| --- | --- | --- |
| `value` | `* 𝌠` | Y gwerthoedd o'r rhestr. |
| `index` | `INT 𝌠` | Talwr o 0..count. Gallwch ddefnyddio hwn fel index. |
| `count` | `INT` | Y nifer o eitemau yn y rhestr. |
| `inspect_combo` | `COMBO` | Allbwn ddummy a allwch ei ddefnyddio i gysylltu i `COMBO` a'i llenwi â'i gwerthoedd. Bydd y cysylltiad yn ailddefnyddio'n awtomatig i allbwn `value`. |

