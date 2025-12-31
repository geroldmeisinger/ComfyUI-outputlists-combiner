## نمبر آؤپٽ فہرست

![Number OutputList](NumberOutputList/NumberOutputList.png)

(ComfyUI ورک فلا و شامل آهي)

عدد جي فہرست ٺاهي ٿي جي گهٽ ۾ گهٽ عدد جي وضاحت ڪري ٿي.
داخلو ۾ [numpy.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html) استعمال ڪري ٿي، چوھن گهٽ ۾ گهٽ عدد جي وضاحت ۾ گهٽ ۾ گهٽ گهٽ ۾ گهٽ چلندو آهي.
جيڪو چاهيو ٿا ته گهٽ ۾ گهٽ عدد جي فہرست ٺاهي ٿي، اُن کي چيک ڪريو JSON OutputList ۽ فہرست ٺاهيو، جيئن `[1, 42, 123]`.
`int`, `float`, `string` ۽ `index` `is_output_list=True` استعمال ڪري ٿي (symbol `𝌠` جي نشان ۾) ۽ ڀيٽ ۾ چلندو آهي.

### اِن پٽ

| نالو | قسم | وضاحت |
| --- | --- | --- |
| `start` | `FLOAT` | اِس گهٽ ۾ گهٽ چلندو آهي. |
| `stop` | `FLOAT` | آخر جو گهٽ ۾ گهٽ. جيڪو `endpoint=include` هجي ته اِس گهٽ ۾ گهٽ فہرست ۾ شامل آهي. |
| `num` | `INT` | فہرست ۾ گهٽ ۾ گهٽ جي گهٽ ۾ گهٽ (اِس گهٽ ۾ گهٽ `step` ۾ گهٽ ۾ گهٽ چلندو نه آهي). |
| `endpoint` | `BOOLEAN` | چلندو آهي ته `stop` گهٽ ۾ گهٽ فہرست ۾ شامل ٿي ٿو يا نه. |

### آؤٽ پٽ

| نالو | قسم | وضاحت |
| --- | --- | --- |
| `int` | `INT 𝌠` | گهٽ ۾ گهٽ چلندو آهي. |
| `float` | `FLOAT 𝌠` | گهٽ ۾ گهٽ چلندو آهي. |
| `string` | `STRING 𝌠` | گهٽ ۾ گهٽ چلندو آهي. |
| `index` | `INT 𝌠` | 0..count جي وضاحت چلندو آهي. |
| `count` | `INT` | `num` ۾ گهٽ ۾ گهٽ چلندو آهي. |

