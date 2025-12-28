<!-- This file was auto-translated with a local LLM and last updated on 2025-12-28. -->
## Int Float Strra konvertitu

![Int Float Strra konvertitu](ConvertNumberToIntFloatStr/ConvertNumberToIntFloatStr.png)

(ComfyUI workflow included)

Baztertzen du zehaztua ez den zenbakiak `INT` `FLOAT` `STRING` bezalakoak eginez.
`nums_from_string.get_nums` erabiltzen du, zenbakiak onartzen ditu zehaztua ez dena. Zenbakiak, zenbakiak edo zenbakiak string formakoak, edo stringak bestelako zenbakiak dituztenak.
`123;234;345` stringa erabili nahi du zehaztua ez den zenbakiak sortzeko. Komadak erabili gabe, zehaztua ez den zenbakiak zehaztua ez dena izan daiteke.
`int`, `float` eta `string` `is_output_list=True` (𝌠 simboloa) erabiltzen dute eta hemen dagoen nodoen bidez sekuentzialki prozesatzen dira.

### Sarrera

| Izena | Tipoa | Deskribapena |
| --- | --- | --- |
| `any` | `*` | Stringra konvertitzeko zehaztua ez dena, eta hemen dagoen zenbakiak onartzen direla |

### Egitura

| Izena | Tipoa | Deskribapena |
| --- | --- | --- |
| `int` | `INT 𝌠` | Stringan aurkitutako zenbakiak, desbideak trunkatu ziren. |
| `float` | `FLOAT 𝌠` | Stringan aurkitutako zenbakiak, float formakoak. |
| `string` | `STRING 𝌠` | Stringan aurkitutako zenbakiak, float formakoak string formakoak. |
| `count` | `INT` | Aurkitutako zenbakiak kopurua. |

