## Bihurtu Int Float Str bihurtzailea

![Bihurtu Int Float Str](ConvertNumberToIntFloatStr/ConvertNumberToIntFloatStr.png)

(ComfyUI workflow included)

Zenbaki bezalako edozer `INT` `FLOAT` `STRING` bihurtzen du.
`nums_from_string.get_nums` erabiltzen du barnean, eta zenbakiak onartzea oso lasaiagoa da. Egiazko int-ak, egiazko float-ak, int-ak edo float-ak string bezala, milakoen bereizleak dituzten hainbat zenbaki dituen string-ak bezala.
Erabili `123;234;345` string bat zenbaki-zerrenda azkar bat sortzeko. Ez erabili komak bereizle bezala, milakoen bereizle bezala interpretatu daitezkeelako.
`int`, `float` eta `string` erabiltzen du `is_output_list=True` (`.𝌠` ikurraz adierazita) eta elkarreragileen node-ekin sekuentzialki prozesatuko dira.

### Sarrerak

| Izena | Mota | Deskribapena |
| --- | --- | --- |
| `any` | `*` | String batean azpizkioak dituen zenbaki bezalako edozer |

### Irteerak

| Izena | Mota | Deskribapena |
| --- | --- | --- |
| `int` | `INT 𝌠` | String-ean aurkitutako zenbaki guztiak komatik moztu ondoren. |
| `float` | `FLOAT 𝌠` | String-ean aurkitutako zenbaki guztiak float bezala. |
| `string` | `STRING 𝌠` | String-ean aurkitutako zenbaki guztiak float bezala bihurtu eta string bezala. |
| `count` | `INT` | Balioan aurkitutako zenbaki kopurua. |

