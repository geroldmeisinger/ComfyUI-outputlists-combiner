## Discriminator workflow

![Discriminator workflow](WorkflowDiscriminator/WorkflowDiscriminator.png)

(ComfyUI workflow zahrnutý)

Porovnáva workflow a rozlišuje ich, aby extrahoval rôzne hodnoty ako jednotlivé OutputListy.
Tento uzol môžete použiť na obnovenie toho, ako bolo každé jednotlivé obrázok vytvorené zoznamom obrázkov s rovnakým workflow.
Všimnite si, že ComfyUI `IMAGE` neobsahuje metadáta workflow a musíte načítať obrázky pomocou špecializovaných načítavačov obrázkov+metadát a pripojiť metadáta k tomuto uzlu.
Vlastné uzly s načítavačmi metadát zahŕňajú:
* `Load Any File.metadata` -> `JSON OutputList(jsonpath=$.["PNG:Prompt"]).value`
* [Crystool](https://github.com/crystian/ComfyUI-Crystools) `🪛 Load image with metadata.Metadata RAW` -> `🪛 Metadata extractor.prompt`
* [Simple_Readable_Metadata](https://github.com/ShammiG/ComfyUI-Simple_Readable_Metadata-SG) `Simple Readable Metadata-SG.metadata_raw`

### Vstupy

| Názov | Typ | Popis |
| --- | --- | --- |
| `objs_0` | `*` | (voliteľné) Jedna objekt (alebo zoznam objektov), zvyčajne z workflow. `objs_0` a `more_objs` budú spojené dohromady a existujú pre pohodlie, ak chcete porovnávať iba dva objekty. |
| `more_objs` | `*` | (voliteľné) Ďalší objekt (alebo zoznam objektov), zvyčajne z workflow. `objs_0` a `more_objs` budú spojené dohromady a existujú pre pohodlie, ak chcete porovnávať iba dva objekty. |
| `ignore_jsonpaths` | `STRING` | (voliteľné) Zoznam JSONPath, ktoré sa majú ignorovať, ak chcete reťazit viacero diskriminátorov spolu. |

### Výstupy

| Názov | Typ | Popis |
| --- | --- | --- |
| `list_a` | `* 𝌠` |  |
| `list_b` | `* 𝌠` |  |
| `list_c` | `* 𝌠` |  |
| `list_d` | `* 𝌠` |  |
| `jsonpaths` | `STRING 𝌠` |  |

