## String OutputList

![String OutputList](StringOutputList/StringOutputList.png)

(ComfyUI workflow inbegrepen)

Maakt een OutputList door de string in het tekstveld op te splitsen met een scheidingsteken.
`value` en `index` gebruiken `is_output_list=True` (aangegeven door het symbool `𝌠`) en worden sequentieel verwerkt door bijbehorende nodes.

### Invoer

| Naam | Type | Beschrijving |
| --- | --- | --- |
| `separator` | `STRING` | De string die wordt gebruikt om de waarden in het tekstveld op te splitsen. |
| `values` | `STRING` | De tekst die je wilt splitsen in een lijst. Let op dat de string wordt afgekapt van afsluitende newlines voor het splitsen, en elk item opnieuw wordt afgekapt van whitespace. |

### Uitvoer

| Naam | Type | Beschrijving |
| --- | --- | --- |
| `value` | `* 𝌠` | De waarden uit de lijst. |
| `index` | `INT 𝌠` | Bereik van 0..aantal. Je kunt dit gebruiken als index. |
| `count` | `INT` | Het aantal items in de lijst. |
| `inspect_combo` | `COMBO` | Een dummy-uitvoer die je kunt gebruiken om te verbinden met een `COMBO` en vooraf te vullen met de waarden ervan. De verbinding wordt dan automatisch opnieuw gekoppeld aan de `value`-uitvoer. |

