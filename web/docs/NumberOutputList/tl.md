## Number OutputList

![Number OutputList](NumberOutputList/NumberOutputList.png)

(ComfyUI workflow included)

Ginagawa ang OutputList na may isang hanay ng mga numero.
Ginagamit ang [numpy.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html) sa loob, dahil mas reliable ito sa mga floating-point na mga value.
Kung gusto mong magtakda ng mga listahan ng mga numero na may kahalagang mga step, tingnan ang JSON OutputList at magtakda ng isang array, halimbawa `[1, 42, 123]`.
`int`, `float`, `string` at `index` gamit ang `is_output_list=True` (na ipinapakita ng simbolo `𝌠`) at ipaproseso nang sekwestyal ang mga ito sa mga katugma ng nodes.

### Mga Input

| Pangalan | Uri | Paglalarawan |
| --- | --- | --- |
| `start` | `FLOAT` | Ang simula ng hanay ng mga value. |
| `stop` | `FLOAT` | Ang dulo ng hanay. Kung `endpoint=include` ang number na ito ay kasama sa listahan. |
| `num` | `INT` | Bilang ng mga item sa listahan (huwag ikokonekta ito sa `step`). |
| `endpoint` | `BOOLEAN` | Tinatukoy kung dapat isama o iwanan ang `stop` na value sa mga item. |

### Mga Output

| Pangalan | Uri | Paglalarawan |
| --- | --- | --- |
| `int` | `INT 𝌠` | Ang value na nai-convert sa int (binawas ang kabuuan). |
| `float` | `FLOAT 𝌠` | Ang value bilang float. |
| `string` | `STRING 𝌠` | Ang value bilang float na nai-convert sa string. |
| `index` | `INT 𝌠` | Hanay ng 0..count na maaaring gamitin bilang index. |
| `count` | `INT` | Katulad ng `num`. |

