## JSON OutputList

![JSON OutputList](JSONOutputList/JSONOutputList.png)

(ComfyUI workflow bijgevoegd)

Maakt ‘n OutputList door arrays of dictionaries te extrahere um JSON objecte.
Gebruk JSONPath syntax um de waardes te extrahere, zie [JSONPath op Wikipedia](https://en.wikipedia.org/wiki/JSONPath) .
Alle gevènd waardes zien geplaat in ‘n lange leeste.
Ge koet ‘t node oec gebruke um objecte te make um literal strings es `[1, 2, 3]`.
`key`, `value`, `int` en `float` gebruk `is_output_list=True` (aangegeven door ‘t symbool `𝌠`) en zien verwerkt in sequentiele nodes.

### Invoere

| Naom | Type | Beschrèving |
| --- | --- | --- |
| `jsonpath` | `STRING` | JSONPath gebrukt um de waardes te extrahere. |
| `json` | `STRING` | ‘n JSON string wat gebrukt weurd um ‘n object te make. |
| `obj` | `*` | (optioneel) object um elk type wat ‘t JSON string vervange |

### Uitvoere

| Naom | Type | Beschrèving |
| --- | --- | --- |
| `key` | `STRING 𝌠` | De key um dictionaries of index um arrays (as string).  Technisch is ‘t ‘n globale index um de geplaatte leeste veur alle non-keys. |
| `value` | `STRING 𝌠` | De waarde as ‘n string. |
| `int` | `INT 𝌠` | De waarde as ‘n int (es ‘t nummer neet parseerbaar is, gebruk ‘t default 0). |
| `float` | `FLOAT 𝌠` | De waarde as ‘n float (es ‘t nummer neet parseerbaar is, gebruk ‘t default 0). |
| `count` | `INT` | Totale aantal items um de geplaatte leeste |
| `debug` | `STRING` | Debug output um alle gevènde objecte as ‘n geformateerde JSON string |

