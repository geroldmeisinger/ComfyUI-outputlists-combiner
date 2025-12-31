## Mga Kombinasyon ng OutputLists

![Mga Kombinasyon ng OutputLists](CombineOutputLists/CombineOutputLists.png)

(kasama ang ComfyUI workflow)

Kinukuha ang hanggang 4 OutputLists at bumubuo ng lahat ng mga kombinasyon ng mga ito.

Halimbawa: `[1, 2, 3] x ["A", "B"] = [(1, "A"), (1, "B"), (2, "A"), (2, "B"), (3, "A"), (3, "B")]`

`unzip_a` .. `unzip_d` gamit ang `is_output_list=True` (na ipinapakita ng simbolo `𝌠`) at ipaproseso nang sequence ng mga corresponding nodes.

Lahat ng mga list ayopsyonal at ang mga walang laman na list ay ipapalampas.

Sa teknikal na pagkuha ay nagcompute ito ng *Cartesian product* at ibinibigay ang bawat kombinasyon na hiwa-hiwa sa kanilang mga elemento (`unzip`), habang ang mga walang laman na list ay papalitan ng mga unit ng `None` at ipapahayag ang `None` sa kaukulang output.

Halimbawa: `[1, 2] x [] x ["A", "B"] x [] = [(1, None, "A", None), (1, None, "B", None), (2, None, "A", None), (2, None, "B", None)]`

### Mga Input

| Pangalan | Uri | Paglalarawan |
| --- | --- | --- |
| `list_a` | `*` | (opsyonal) |
| `list_b` | `*` | (opsyonal) |
| `list_c` | `*` | (opsyonal) |
| `list_d` | `*` | (opsyonal) |

### Mga Output

| Pangalan | Uri | Paglalarawan |
| --- | --- | --- |
| `unzip_a` | `* 𝌠` | Ang halaga ng mga kombinasyon na tumutugma sa `list_a`. |
| `unzip_b` | `* 𝌠` | Ang halaga ng mga kombinasyon na tumutugma sa `list_b`. |
| `unzip_c` | `* 𝌠` | Ang halaga ng mga kombinasyon na tumutugma sa `list_c`. |
| `unzip_d` | `* 𝌠` | Ang halaga ng mga kombinasyon na tumutugma sa `list_d`. |
| `index` | `INT 𝌠` | Sakto ang 0..count na maaaring gamitin bilang index. |
| `count` | `INT` | Kabuuang bilang ng mga kombinasyon. |

