## KSampler Immediate Save

![KSampler Immediate Save](KSamplerImmediateSave/KSamplerImmediateSave.png)

(ComfyUI workflow zahrnut)

Rozšíření uzlu výchozího `CheckpointLoader`, `KSampler`, `VAE Decode` a `Save Image` pro zpracování jako jeden celek.
Toto je užitečné, pokud chcete okamžitě ukládat mezilehlé obrázky pro mřížky.

*"Vlastní KSampler jenom kvůli uložení obrázku? Nyní se stal tím, čím jsem se snažil bojovat!"*

### Vstupy

| Název | Typ | Popis |
| --- | --- | --- |
| `cpkt_name` | `COMBO` | Název kontrolního bodu (modelu) k načtení. |
| `positive` | `ŘETĚZEC` | Podmínění popisující vlastnosti, které chcete zahrnout do obrázku. |
| `negative` | `ŘETĚZEC` | Podmínění popisující vlastnosti, které chcete vyloučit z obrázku. |
| `latent_image` | `LATENT` | Latentní obraz k dešumování. |
| `seed` | `CELÉ ČÍSLO` | Náhodný semínko použité při vytváření šumu. |
| `steps` | `CELÉ ČÍSLO` | Počet kroků použitých v procesu dešumování. |
| `cfg` | `DESETINNÉ ČÍSLO` | Měřítko bez classifikačního vedení (Classifier-Free Guidance) vyrovnává kreativitu a oddanost výzvě. Vyšší hodnoty vedou k obrázkům blíže odpovídajícím výzvě, avšak příliš vysoké hodnoty negativně ovlivní kvalitu. |
| `sampler_name` | `COMBO` | Algoritmus použitý při vzorkování, může ovlivnit kvalitu, rychlost a styl generovaného výstupu. |
| `scheduler` | `COMBO` | Plánovač řídí, jak se šum postupně odstraňuje pro vytvoření obrázku. |
| `denoise` | `DESETINNÉ ČÍSLO` | Množství dešumování aplikovaného, nižší hodnoty zachovají strukturu počátečního obrázku, což umožňuje vzorkování obrazu z obrazu. |
| `filename_prefix` | `ŘETĚZEC` | Prefix souboru k uložení. Může zahrnovat informace o formátování, jako například %date:yyyy-MM-dd% nebo %Empty Latent Image.width%, aby zahrnoval hodnoty z uzlů. |

### Výstupy

| Název | Typ | Popis |
| --- | --- | --- |
| `image` | `OBRÁZEK` | Dekódovaný obrázek. |

