## OutputLists Konbinazioak

![OutputLists Konbinazioak](CombineOutputLists/CombineOutputLists.png)

(ComfyUI workflow erantsita)

4 OutputList hartu eta beren konbinazio guztiak sortzen ditu.

Adibidea: `[1, 2, 3] x ["A", "B"] = [(1, "A"), (1, "B"), (2, "A"), (2, "B"), (3, "A"), (3, "B")]`

`unzip_a` .. `unzip_d` `is_output_list=True` erabiltzen dute ( `𝌠` ikurarekin adierazten da) eta dagokien nodoen bidez sekuentzialki prozesatuko dira.

Zerrenda guztiak aukerakoak dira eta hutsik dauden zerrendak ez dira kontuan hartuko.

Teknikoki *kartesiarrena kalkulatzen du* eta konbinazio bakoitza bere elementutan zatituta ematen du (`unzip`), hutsik dauden zerrendek `None` unitateekin ordezkatuko dira eta horrek `None` emango dute dagokien irteeran.

Adibidea: `[1, 2] x [] x ["A", "B"] x [] = [(1, None, "A", None), (1, None, "B", None), (2, None, "A", None), (2, None, "B", None)]`

### Sarrerak

| Izena | Mota | Deskribapena |
| --- | --- | --- |
| `list_a` | `*` | (aukerakoa) |
| `list_b` | `*` | (aukerakoa) |
| `list_c` | `*` | (aukerakoa) |
| `list_d` | `*` | (aukerakoa) |

### Irteerak

| Izena | Mota | Deskribapena |
| --- | --- | --- |
| `unzip_a` | `* 𝌠` | `list_a`-ren konbinazioei dagokien balioa. |
| `unzip_b` | `* 𝌠` | `list_b`-ren konbinazioei dagokien balioa. |
| `unzip_c` | `* 𝌠` | `list_c`-ren konbinazioei dagokien balioa. |
| `unzip_d` | `* 𝌠` | `list_d`-ren konbinazioei dagokien balioa. |
| `index` | `INT 𝌠` | 0..count tartea, index gisa erabil daitekeen. |
| `count` | `INT` | Konbinazio kopurua. |

