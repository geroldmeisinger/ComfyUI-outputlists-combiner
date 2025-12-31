## KSampler Immediate Save

![KSampler Immediate Save](KSamplerImmediateSave/KSamplerImmediateSave.png)

(ComfyUI workflow mellékletként)

A default `CheckpointLoader`, `KSampler`, `VAE Decode` és `Save Image` csomópontok kiterjesztése egy feldolgozásra.
Ez akkor hasznos, ha az átmeneti képeket grid-ként azonnal menteni szeretnéd.

*"Egyéni KSampler csak egy kép mentésére? Most már az vagyok, amiért olyan erőt keresett, amit meg akart rombolni!"*

### Bemenetek

| Név | Típus | Leírás |
| --- | --- | --- |
| `cpkt_name` | `COMBO` | A betöltendő ellenőrzőpont (modell) neve. |
| `positive` | `STRING` | A feltétel, amely leírja azokat a tulajdonságokat, amelyeket a képbe szeretnél bevonni. |
| `negative` | `STRING` | A feltétel, amely leírja azokat a tulajdonságokat, amelyeket a képből ki szeretnél zárni. |
| `latent_image` | `LATENT` | A zajtelenítendő latens kép. |
| `seed` | `INT` | A zaj létrehozásához használt véletlenszám-seed. |
| `steps` | `INT` | A zajtelenítési folyamatban használt lépések száma. |
| `cfg` | `FLOAT` | A Classifier-Free Guidance skála egyensúlyt teremt a kreativitás és a prompt következetessége között. A magasabb értékek eredményeznek a prompt-hoz közelebbi képeket, de túl magas értékek negatívan befolyásolják a minőséget. |
| `sampler_name` | `COMBO` | A mintavétel során használt algoritmus, amely befolyásolhatja a generált kimenet minőségét, sebességét és stílusát. |
| `scheduler` | `COMBO` | A szcheduleder szabályozza, hogyan távolítja el a zajt, hogy létrehozza a képet. |
| `denoise` | `FLOAT` | A alkalmazott zajtisztítás mértéke, az alacsonyabb értékek megőrzik az eredeti kép szerkezetét, lehetővé téve a kép-képből való mintavételt. |
| `filename_prefix` | `STRING` | A mentendő fájl előtagja. Ez tartalmazhat formázási információkat, például %date:yyyy-MM-dd% vagy %Empty Latent Image.width%, hogy beillesztsük az értékeket a csomópontokból. |

### Kimenetek

| Név | Típus | Leírás |
| --- | --- | --- |
| `image` | `IMAGE` | A dekódolt kép. |

