## String OutputList

![String OutputList](StringOutputList/StringOutputList.png)

(ComfyUI workflow bijgevoegd)

Maakt ‘n OutputList um ‘t te splitten um de string um ‘t tekstveld um ‘n separator.
`value` en `index` gebruk `is_output_list=True` (aangegeven door ‘t symbool `𝌠`) en zien verwerkt in sequentiele nodes.

### Invoere

| Naom | Type | Beschrèving |
| --- | --- | --- |
| `separator` | `STRING` | De string um ‘t tekstveld waardes um ‘t splitten. |
| `values` | `STRING` | De tekst um ‘t te splitten um ‘n lijst. Let op dat de string um trailing newlines trimt voor ‘t splitten, en elk item um ‘t weer trimt um whitespace. |

### Uitvoere

| Naom | Type | Beschrèving |
| --- | --- | --- |
| `value` | `* 𝌠` | De waardes um de lijst. |
| `index` | `INT 𝌠` | Reeks um 0..count. Ge kin ‘t gebruke um ‘n index te make. |
| `count` | `INT` | ‘t Aantal items um de lijst. |
| `inspect_combo` | `COMBO` | ‘n dummy-output um ‘t te verbinne um ‘n `COMBO` en um ‘t te vullen um ‘t waardes. De verbinding kin dan automatisch um ‘t te koppelen um `value` output. |

