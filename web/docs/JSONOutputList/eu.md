## JSON OutputList

![JSON OutputList](JSONOutputList/JSONOutputList.png)

(ComfyUI workflow included)

JSON objektuetatik array-ak edo hiztegiak ateratuz OutputList sortzen du.
Balioak ateratzeko JSONPath sintaxia erabiltzen du, ikusi [JSONPath Wikipedia-en](https://en.wikipedia.org/wiki/JSONPath) .
Berdintasun guztiak zerrenda luze batean gainjartzen dira.
Nodo hau erabil dezakezu `[1, 2, 3]` bezalako literaletako kateetatik objektuak sortzeko.
`key`, `value`, `int` eta `float` erabiltzen du `is_output_list=True` (`.𝌠` ikurraz adierazita) eta elkarreragileen node-ekin sekuentzialki prozesatuko dira.

### Sarrerak

| Izena | Mota | Deskribapena |
| --- | --- | --- |
| `jsonpath` | `STRING` | Balioak ateratzeko erabilitako JSONPath. |
| `json` | `STRING` | Objektura bihurtzen den JSON katea. |
| `obj` | `*` | (aukerakoa) JSON katea ordezkatuko den edozein motatako objektua |

### Irteerak

| Izena | Mota | Deskribapena |
| --- | --- | --- |
| `key` | `STRING 𝌠` | Hiztegiakiko gakoa edo array-aren indizea (kate bezala). Teknikoki, gainjartutako zerrendaren indize globala da gakoak ez diren guztientzat. |
| `value` | `STRING 𝌠` | Balioa kate bezala. |
| `int` | `INT 𝌠` | Balioa int bezala (zenbakia ezin bada analizatu, 0-era lehentsi egiten da). |
| `float` | `FLOAT 𝌠` | Balioa float bezala (zenbakia ezin bada analizatu, 0-era lehentsi egiten da). |
| `count` | `INT` | Gainjartutako zerrendako elementu kopurua |
| `debug` | `STRING` | Berdintasun guztien irteera, JSON kate formatuatuan |

