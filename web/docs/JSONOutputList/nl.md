## JSON OutputList

![JSON OutputList](JSONOutputList/JSONOutputList.png)

(ComfyUI workflow inclusief)

Maakt een OutputList door arrays of dictionaries uit JSON objecten te extraheren.
Gebruikt JSONPath syntax om de waarden te extraheren, zie [JSONPath op Wikipedia](https://en.wikipedia.org/wiki/JSONPath).
Alle gematchte waarden worden samengevoegd tot één lange lijst.
Je kunt deze node ook gebruiken om objecten te maken van letterlijke strings zoals `[1, 2, 3]`.
`key`, `value`, `int` en `float` gebruiken `is_output_list=True` (aangegeven door het symbool `𝌠`) en worden sequentieel verwerkt door overeenkomstige nodes.

### Invoeren

| Naam | Type | Beschrijving |
| --- | --- | --- |
| `jsonpath` | `STRING` | JSONPath gebruikt om de waarden te extraheren. |
| `json` | `STRING` | Een JSON string die wordt omgezet naar een object. |
| `obj` | `*` | (optioneel) object van elke type dat de JSON string zal vervangen |

### Uitvoeren

| Naam | Type | Beschrijving |
| --- | --- | --- |
| `key` | `STRING 𝌠` | De key voor dictionaries of index voor arrays (als string). Technisch gezien is het een globale index van de geplaatste lijst voor alle niet-keys. |
| `value` | `STRING 𝌠` | De waarde als string. |
| `int` | `INT 𝌠` | De waarde als int (als het getal niet geïnterpreteerd kan worden, wordt standaard 0 gebruikt). |
| `float` | `FLOAT 𝌠` | De waarde als float (als het getal niet geïnterpreteerd kan worden, wordt standaard 0 gebruikt). |
| `count` | `INT` | Totaal aantal items in de geplaatste lijst |
| `debug` | `STRING` | Debug output van alle gematchte objecten als een geformatteerde JSON string |

