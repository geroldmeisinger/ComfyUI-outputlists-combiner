## Zou Int Float Str convertéieren

![Convert To Int Float Str](ConvertNumberToIntFloatStr/ConvertNumberToIntFloatStr.png)

(ComfyUI workflow d'ofgesech)

Convertéiert alles Zuel-ähnlech zu `INT` `FLOAT` `STRING`.
Benotzt `nums_from_string.get_nums` intern, déi sehr permissiv ass wéinst d'Zuele, déi se ugesinn. Alles vun echte Ganzzuele, echte Kommazuele, Ganzzuele oder Kommazuele als String, Strings déi e puer Zuele mat Tausendseparrécker enthalen.
Benotzt e String `123;234;345` fir schnell eng Lëscht vun Zuele ze generéieren. Benotzt keng Komma als Separatoren, well se als Tausendseparrécker interpretéiert kënnen.
`int`, `float` an `string` benotzen (s) `is_output_list=True` (indizéiert duerch den Symbol `𝌠`) an ginn sequentiell duerch d'entspriechend Nodes verarbeit.

### Input

| Numm | Typ | Beschreiwung |
| --- | --- | --- |
| `any` | `*` | Alles wat meaningfull zu engem String convertéiert kënnen, an Zuele mat parsebar Zuele enthalen |

### Output

| Numm | Typ | Beschreiwung |
| --- | --- | --- |
| `int` | `INT 𝌠` | All Zuele, déi an der String fonnt goufen, mat de Dezimalen ofgeschnidden. |
| `float` | `FLOAT 𝌠` | All Zuele, déi an der String fonnt goufen, als Kommazuel. |
| `string` | `STRING 𝌠` | All Zuele, déi an der String fonnt goufen, als Kommazuel convertéiert zu engem String. |
| `count` | `INT` | Aantal vun Zuele, déi an der Wäert fonnt goufen. |

