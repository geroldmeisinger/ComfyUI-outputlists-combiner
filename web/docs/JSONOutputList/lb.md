## JSON OutputList

![JSON OutputList](JSONOutputList/JSONOutputList.png)

(ComfyUI workflow d'ofgesech)

Erstellt e OutputList, andeem Arrays oder Dictionaries aus JSON-Objete extrahéiert ginn.
Benotzt JSONPath-Syntax, fir d'Wäerter ze extrahéieren, kuck [JSONPath op Wikipedia](https://en.wikipedia.org/wiki/JSONPath) .
All ugestuermte Wäerter ginn an eng laang Lëscht flatten.
Dir kënnt dës Node och benotzen, fir Objete aus Literal-Strings ze erstellen, wéi `[1, 2, 3]`.
`key`, `value`, `int` an `float` benotzen (s) `is_output_list=True` (indizéiert duerch den Symbol `𝌠`) an ginn sequentiell duerch d'entspriechend Nodes verarbeit.

### Input

| Numm | Typ | Beschreiwung |
| --- | --- | --- |
| `jsonpath` | `STRING` | JSONPath, deen fir d'Extrahéierung vun den Wäerter benotzt gëtt. |
| `json` | `STRING` | E JSON-String, deen zu engem Object iwwegesat gëtt. |
| `obj` | `*` | (optional) Object vun all Typ, deen de JSON-String ersetzt |

### Output

| Numm | Typ | Beschreiwung |
| --- | --- | --- |
| `key` | `STRING 𝌠` | De Schlëssel fir Dictionaries oder Index fir Arrays (als String). Technesch, et ass e global Index vun der flatten Lëscht fir all net-Schlësser. |
| `value` | `STRING 𝌠` | De Wäert als String. |
| `int` | `INT 𝌠` | De Wäert als Integer (wann de Zuel net parse gëtt, gëtt 0 als Standard verwent). |
| `float` | `FLOAT 𝌠` | De Wäert als Float (wann de Zuel net parse gëtt, gëtt 0 als Standard verwent). |
| `count` | `INT` | Gesamte Zuel vun Elementer an der flatten Lëscht |
| `debug` | `STRING` | Debug-Output vun all ugestuermte Objete als formatéierte JSON-String |

