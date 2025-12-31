## Zenbakiaren OutputList

![Zenbakiaren OutputList](NumberOutputList/NumberOutputList.png)

(ComfyUI workflow included)

Balio zenbakizko barruti batekin OutputList sortzen du.
Barnean [numpy.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html) erabiltzen du, zifra-errealen balioekin erabiltzeko egokia delako.
Zehaztutako urraketarekin zenbaki-zerrendak definitu nahi badituzu, ikusi JSON OutputList eta definitu array bat, adibidez `[1, 42, 123]`.
`int`, `float`, `string` eta `index` erabiltzen du `is_output_list=True` (`.𝌠` ikurraz adierazita) eta elkarreragileen node-ekin sekuentzialki prozesatuko dira.

### Sarrerak

| Izena | Mota | Deskribapena |
| --- | --- | --- |
| `start` | `FLOAT` | Barrutia sortzeko hasierako balioa. |
| `stop` | `FLOAT` | Amaierako balioa. `endpoint=include` bada, balio hau zerrendan sartzen da. |
| `num` | `INT` | Zerrendako elementu kopurua (`step`-ekin ez nahasteko). |
| `endpoint` | `BOOLEAN` | `stop` balioa zerrendan sartu edo ez ezartzen du. |

### Irteerak

| Izena | Mota | Deskribapena |
| --- | --- | --- |
| `int` | `INT 𝌠` | Balioa int-era bihurtuta (behera biratuta/eredura). |
| `float` | `FLOAT 𝌠` | Balioa float bezala. |
| `string` | `STRING 𝌠` | Balioa float bezala eta kate bihurtuta. |
| `index` | `INT 𝌠` | 0..count barrutiko zerrenda, index bezala erabil daitekeenak. |
| `count` | `INT` | `num` bezala. |

