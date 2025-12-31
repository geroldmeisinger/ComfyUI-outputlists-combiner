## KSampler Berehala Gorde

![KSampler Berehala Gorde](KSamplerImmediateSave/KSamplerImmediateSave.png)

(ComfyUI workflow included)

`CheckpointLoader`, `KSampler`, `VAE Decode` eta `Save Image` lehenetsitako nodoen hedapena, bat bezala prozesatzeko.
Hau erabilgarria da sareko irudien arteko irudia gorde nahi baduzu.

*"KSampler pertsonalizatu bat irudia gordetzeko? Orain nire aurka erabakitzeko gauza izan naiz!"*

### Sarrerak

| Izena | Mota | Deskribapena |
| --- | --- | --- |
| `cpkt_name` | `COMBO` | Kargatzeko kontrol-puntua (modelo) izena. |
| `positive` | `STRING` | Irudian sartu nahi dituzun atributuen deskribapena. |
| `negative` | `STRING` | Iruditik kanporatu nahi dituzun atributuen deskribapena. |
| `latent_image` | `LATENT` | Zarata kendu beharreko irudia. |
| `seed` | `INT` | Zarata sortzeko erabilitako ausazko gakoa. |
| `steps` | `INT` | Zarata kenduko den prozesuan erabilitako urrats kopurua. |
| `cfg` | `FLOAT` | Sailkapenik gabeko gidapen eskala, sortzailea eta prompt-era jarraitzea balantzatu egiten du. Balio altuagoak prompt-era gehienekoz egokitzen diren irudiak ematen ditu, baina balio altuek kalitatea negatiboki eragina dutenak. |
| `sampler_name` | `COMBO` | Laginak egiteko erabilitako algoritmoa, honek emaitzaren kalitatea, abiadura eta estiloa eragina dutenak. |
| `scheduler` | `COMBO` | Programatzaileak kontrolatzen du zaratari irudia eraikitzen denean. |
| `denoise` | `FLOAT` | Kendutako zaratari kopurua, balio baxuagoak hasierako irudiaren egitura mantentzen dute, irudia iruditik laginak egiteko aukera ematen dutenak. |
| `filename_prefix` | `STRING` | Gordeko den fitxategiaren aurrizkia. Honek formateatze informazioa izan dezake, adibidez %date:yyyy-MM-dd% edo %Empty Latent Image.width% nodeetatik balioak sartzeko. |

### Irteerak

| Izena | Mota | Deskribapena |
| --- | --- | --- |
| `image` | `IMAGE` | Deskodifikatutako irudia. |

