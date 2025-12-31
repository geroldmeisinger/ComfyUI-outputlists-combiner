## Number OutputList

![Number OutputList](NumberOutputList/NumberOutputList.png)

(ComfyUI workflow d'ofgesech)

Erstellt e OutputList mat engem Beräich vun numeresche Wäerter.
Benotzt intern [numpy.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html), well et mat dem Float-Wäerter méi robuster arbeit.
Wann Dir stattdessen Zuelenlisten mat willkierlechen Schrëtt definéieren wëllt, kuckt den JSON OutputList an definéiert e Array, e.g. `[1, 42, 123]`.
`int`, `float`, `string` an `index` benotzen (s) `is_output_list=True` (indizéiert duerch den Symbol `𝌠`) an ginn sequentiell duerch d'entspriechend Nodes verarbeit.

### Input

| Numm | Typ | Beschreiwung |
| --- | --- | --- |
| `start` | `FLOAT` | Startwäert, vun deen de Beräich generéiert gëtt. |
| `stop` | `FLOAT` | Ennwäert. Wann `endpoint=include` da gëtt dës Zuel an der Lëscht opgenomme. |
| `num` | `INT` | D'Zuel vun Elementer an der Lëscht (verwirbelt et net mat enger `step`). |
| `endpoint` | `BOOLEAN` | Bestëmmt, ob de `stop` Wäert opgenomme oder ausgeschloss gëtt an de Elementer. |

### Output

| Numm | Typ | Beschreiwung |
| --- | --- | --- |
| `int` | `INT 𝌠` | De Wäert umgewandelt zu int (runter/gerond). |
| `float` | `FLOAT 𝌠` | De Wäert als Float. |
| `string` | `STRING 𝌠` | De Wäert als Float umgewandelt zu String. |
| `index` | `INT 𝌠` | Beräich vun 0..count, de als Index benotzt wärend. |
| `count` | `INT` | D'Selwecht wéi `num`. |

