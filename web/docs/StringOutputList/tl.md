## String OutputList

![String OutputList](StringOutputList/StringOutputList.png)

(ComfyUI workflow included)

Gumawa ng OutputList sa pamamagitan ng paghihiwalay ng string sa textfield gamit ang separator.
`value` at `index` gumagamit ng `is_output_list=True` (na ipinapakita ng simbolo `𝌠`) at ipaproseso nang sequence ng mga corresponding nodes.

### Mga Input

| Name | Type | Paglalarawan |
| --- | --- | --- |
| `separator` | `STRING` | Ang string na ginagamit para ihiwalay ang mga value ng textfield. |
| `values` | `STRING` | Ang text na gusto mong ihiwalay sa isang list. Tandaan na ang string ay tinatanggal ang trailing newlines bago ihiwalay, at ang bawat item ay muli't muli't tinatanggal ang whitespace. |

### Mga Output

| Name | Type | Paglalarawan |
| --- | --- | --- |
| `value` | `* 𝌠` | Ang mga value mula sa list. |
| `index` | `INT 𝌠` | Sakto sa 0..count. Maaari mong gamitin ito bilang isang index. |
| `count` | `INT` | Ang bilang ng mga item sa list. |
| `inspect_combo` | `COMBO` | Isang dummy-output na maaari mong gamitin para ikonekta sa isang `COMBO` at i-pre-fill gamit ang mga value nito. Ang koneksyon ay awtomatikong i-re-link sa output ng `value`. |

