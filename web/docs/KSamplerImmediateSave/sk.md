## KSampler Immediate Save

![KSampler Immediate Save](KSamplerImmediateSave/KSamplerImmediateSave.png)

(ComfyUI workflow je zahrnutý)

Rozšírenie predvoleného uzla `CheckpointLoader`, `KSampler`, `VAE Decode` a `Save Image` na spracovanie ako jeden uzol.
Toto je užitočné, ak chcete okamžite ukladať medziobrazové obrazy pre mriežky.

*"Vlastný KSampler len na uloženie obrázka? Teraz som sa stal tým, čo som sa snažil zničiť!"*

### Vstupy

| Názov | Typ | Popis |
| --- | --- | --- |
| `cpkt_name` | `COMBO` | Názov kontrolnej body (modelu) na načítanie. |
| `positive` | `STRING` | Podmienky popisujúce vlastnosti, ktoré chcete zahrnúť do obrázka. |
| `negative` | `STRING` | Podmienky popisujúce vlastnosti, ktoré chcete vylúčiť z obrázka. |
| `latent_image` | `LATENT` | Latentný obraz na odšumovanie. |
| `seed` | `INT` | Náhodný semeno použité na vytvorenie šumu. |
| `steps` | `INT` | Počet krokov použitých v procese odšumovania. |
| `cfg` | `FLOAT` | Classifier-Free Guidance mierka vyváži kreativitu a prispôsobenie sa výzve. Vyššie hodnoty vytvárajú obrázky bližšie zodpovedajúce výzve, avšak príliš vysoké hodnoty negatívne ovplyvnia kvalitu. |
| `sampler_name` | `COMBO` | Algoritmus použitý pri vzorkovaní, môže ovplyvniť kvalitu, rýchlosť a štýl generovaného výstupu. |
| `scheduler` | `COMBO` | Plánovač riadi, ako sa postupne odstraňuje šum, aby sa vytvoril obraz. |
| `denoise` | `FLOAT` | Množstvo odšumovania použité, nižšie hodnoty zachovajú štruktúru počiatočného obrázka, čo umožňuje image to image vzorkovanie. |
| `filename_prefix` | `STRING` | Prefix pre súbor na uloženie. Môže obsahovať informácie o formátovaní, ako napríklad %date :yyyy-MM-dd% alebo %Empty Latent Image.width% na zahrnutie hodnôt z uzlov. |

### Výstupy

| Názov | Typ | Popis |
| --- | --- | --- |
| `image` | `IMAGE` | Dekódovaný obraz. |

