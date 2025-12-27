<!-- This file was auto-translated with a local LLM and last updated on 2025-12-27. -->
## OutputListen kombinazioak

![OutputListen kombinazioak](CombineOutputLists/CombineOutputLists.png)

(ComfyUI workflow included)

Hautatzen ditu 4 OutputListen batek eta izekiko ditu zehar bakoitzaren kombinazioa.

Adierazpena: `[1, 2, 3] x ["A", "B"] = [(1, "A"), (1, "B"), (2, "A"), (2, "B"), (3, "A"), (3, "B")]`

`unzip_a` .. `unzip_d` `is_output_list=True` erabiltzen du (𝌠 simboloa adierazten du) eta hainbeste nodoen bidez bertan bertan egiten da.

Bidezko listak obligatua ez da, hala nola, huts listak ez dira kontsideratzen.

Hala, zehaztuta dagoen *kartesiar produktua* kalkulatzen du eta bakoitzaren elementuak zehaztzen ditu (`unzip`), huts listak `None` unitatekin sustatzen dira eta hauen balioa `None` izango da bere erantzunetan.

Adierazpena: `[1, 2] x [] x ["A", "B"] x [] = [(1, None, "A", None), (1, None, "B", None), (2, None, "A", None), (2, None, "B", None)]`

### Sarrera

| Izena | Motak | Deskribapena |
| --- | --- | --- |
| `list_a` | `*` | (optzionala) |
| `list_b` | `*` | (optzionala) |
| `list_c` | `*` | (optzionala) |
| `list_d` | `*` | (optzionala) |

### Egitura

| Izena | Motak | Deskribapena |
| --- | --- | --- |
| `unzip_a` | `* 𝌠` | `list_a`ren kombinazioen balioa. |
| `unzip_b` | `* 𝌠` | `list_b`ren kombinazioen balioa. |
| `unzip_c` | `* 𝌠` | `list_c`ren kombinazioen balioa. |
| `unzip_d` | `* 𝌠` | `list_d`ren kombinazioen balioa. |
| `index` | `INT 𝌠` | 0..count balioa, index bat izan daitekeeneko. |
| `count` | `INT` | Kombinazio kopurua. |

