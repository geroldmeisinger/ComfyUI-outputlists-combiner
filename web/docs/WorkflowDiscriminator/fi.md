## Workflow Discriminator

![Workflow Discriminator](WorkflowDiscriminator/WorkflowDiscriminator.png)

(ComfyUI-työnkulku mukana)

Vertaa työnkuluja ja erottaa ne eri arvoiksi yksittäisinä OutputListeina.
Voit käyttää tätä solmua palauttamaan, miten jokainen yksittäinen kuva syntyi saman työnkulun kuvien listasta.
Huomaa, että ComfyUI:n `IMAGE` ei sisällä työnkulun metatietoja, ja sinun täytyy ladata kuvat erikoisilla kuvan+metatietojen lataajilla ja yhdistää metatiedot tähän solmuun.
Metatietojen lataajia tarjoavat mukautetut solmut:
* `Load Any File.metadata` -> `JSON OutputList(jsonpath=$.["PNG:Prompt"]).value`
* [Crystool](https://github.com/crystian/ComfyUI-Crystools) `🪛 Load image with metadata.Metadata RAW` -> `🪛 Metadata extractor.prompt`
* [Simple_Readable_Metadata](https://github.com/ShammiG/ComfyUI-Simple_Readable_Metadata-SG) `Simple Readable Metadata-SG.metadata_raw`

### Syötteet

| Nimi | Tyyppi | Kuvaus |
| --- | --- | --- |
| `objs_0` | `*` | (valinnainen) Yksittäinen objekti (tai objektien lista), yleensä työnkulusta. `objs_0` ja `more_objs` yhdistetään yhteen ja ne olemassa mukavuussyistä, jos haluat verrata vain kahta objektia. |
| `more_objs` | `*` | (valinnainen) Toinen objekti (tai objektien lista), yleensä työnkulusta. `objs_0` ja `more_objs` yhdistetään yhteen ja ne olemassa mukavuussyistä, jos haluat verrata vain kahta objektia. |
| `ignore_jsonpaths` | `STRING` | (valinnainen) Lista JSONPath:istä, jotka ohitetaan, jos haluat ketjuttaa useita erottimia yhteen. |

### Tulosteet

| Nimi | Tyyppi | Kuvaus |
| --- | --- | --- |
| `list_a` | `* 𝌠` |  |
| `list_b` | `* 𝌠` |  |
| `list_c` | `* 𝌠` |  |
| `list_d` | `* 𝌠` |  |
| `jsonpaths` | `STRING 𝌠` |  |

