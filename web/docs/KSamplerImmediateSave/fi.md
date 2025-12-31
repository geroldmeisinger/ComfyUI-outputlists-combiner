## KSampler Immediate Save

![KSampler Immediate Save](KSamplerImmediateSave/KSamplerImmediateSave.png)

(ComfyUI-työnkulku mukana)

Solmun laajennus oletus `CheckpointLoader`, `KSampler`, `VAE Decode` ja `Save Image` -solmuista käsitelläksesi yhtenä.
Tämä on hyödyllinen, jos haluat tallentaa väliväliset kuvat ruudukkoihin heti.

*"Mukautettu KSampler vain kuvan tallentamiseksi? Olen nyt tullut siitä, mitä pyrin tuhoamaan!"*

### Syötteet

| Nimi | Tyyppi | Kuvaus |
| --- | --- | --- |
| `cpkt_name` | `COMBO` | Ladattavan tarkistuspisteen (mallin) nimi. |
| `positive` | `STRING` | Ehdotus, joka kuvaa ominaisuuksia, jotka haluat sisällyttää kuvaan. |
| `negative` | `STRING` | Ehdotus, joka kuvaa ominaisuuksia, jotka haluat poissulkea kuvasta. |
| `latent_image` | `LATENT` | Käytettävä latentti kuva. |
| `seed` | `INT` | Satunnaisluku, jota käytetään kohinan luomiseen. |
| `steps` | `INT` | Denoisointiprosessissa käytettävien askelten määrä. |
| `cfg` | `FLOAT` | Luokittelu- ja ohjeiden ohjausaste tasapainottaa luovuutta ja ohjeen noudattamista. Korkeammat arvot tuottavat kuvia, jotka täsmäävät tarkemmin ohjeeseen, mutta liian korkeat arvot vaikuttavat negatiivisesti laatuun. |
| `sampler_name` | `COMBO` | Näytteenottoalgoritmi, jota käytetään, vaikuttaa laatuun, nopeuteen ja tuotetun tuloksen tyyliin. |
| `scheduler` | `COMBO` | Suunnittelija ohjaa, kuinka kohina vähenee muodostaen kuvan. |
| `denoise` | `FLOAT` | Soveltamisen määrä, pienemmät arvot säilyttävät alkuperäisen kuvan rakenteen, mahdollistaen kuvasta kuvaan näytteenoton. |
| `filename_prefix` | `STRING` | Tallennettavan tiedoston etuliite. Tämä voi sisältää muotoilutietoja, kuten %date:yyyy-MM-dd% tai %Empty Latent Image.width%, jotta voidaan sisällyttää arvot solmuista. |

### Tulosteet

| Nimi | Tyyppi | Kuvaus |
| --- | --- | --- |
| `image` | `IMAGE` | Purettu kuva. |

