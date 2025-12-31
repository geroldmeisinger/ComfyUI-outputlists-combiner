## Katearen OutputList

![Katearen OutputList](StringOutputList/StringOutputList.png)

(ComfyUI workflow included)

Katea banatuz katearen testu-eremuan OutputList sortzen du banatzaile batekin.
`value` eta `index` erabiltzen du `is_output_list=True` (`.𝌠` ikurraz adierazita) eta elkarreragileen node-ekin sekuentzialki prozesatuko dira.

### Sarrerak

| Izena | Mota | Deskribapena |
| --- | --- | --- |
| `separator` | `STRING` | Testu-eremuko balioak banatzeko erabilitako katea. |
| `values` | `STRING` | Zerrenda batera banatu nahi duzun testua. Katea banatu aurretik amaierako lerro-jauziak moztu eta elementu bakoitzak berriro zuriuneak moztuko dituzte. |

### Irteerak

| Izena | Mota | Deskribapena |
| --- | --- | --- |
| `value` | `* 𝌠` | Zerrendako balioak. |
| `index` | `INT 𝌠` | 0..count barrutiko eremua. Hau index bezala erabil dezakezu. |
| `count` | `INT` | Zerrendako elementu kopurua. |
| `inspect_combo` | `COMBO` | `COMBO` batekin lotzeko erabil dezakezun irteera faltsua, eta bere balioekin aurre-betetzeko. Konexioa orduan automatikoki `value` irteerara berrelkartuko da. |

