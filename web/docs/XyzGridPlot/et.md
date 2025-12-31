## XYZ-ruudustikuline graafik

![XYZ-ruudustikuline graafik](XyzGridPlot/XyzGridPlot.png)

(ComfyUI töövoog on kaasatud)

Genereerib XYZ-ruudustikulise graafiku pildiloendist.
See võtab piltide loendi (sh. pakkidega) ja muudab need esmalt pikkudeks loendiks (seega `batch_size=1`).

**Ruudustiku kujundus**
Määrab ruudustiku kujundi järgmiselt:
1. ridade siltide arv
2. veergude siltide arv
3. ülejäänud alampildid.
Saad kasutada `order=inside_out`, et pööretada pildi valik (kasulik, kui `batch_size>1` ja soovid sildistada pakke).

**Joondus**
* Kui silt läheb järgmisele reale, siis kogu telg peetakse "mitmerealiseks" ja joondatakse neid üles, põhjustades vahet.
* Kui kõik sildid on numbrid või kõik lõppevad numbritega (nt `strength: 1.`), siis kogu telg peetakse "numbriliseks" ja joondatakse neid paremale.
* Kõik muud tekstid peetakse "ükserealiseks" ja joondatakse neid keskele.
* Joondab ükserealisi ja numbrilisi silte veergude jaoks all, ja ridade jaoks vertikaalselt keskele.

**Fondi suurus**
* Veeru sildi ala kõrgus määratakse `font_size` või `pool kõige suuremast alampildi pakitud kõrgusest igas reas` (mida suurem).
* Rea sildi ala laius määratakse kõige laiema alampildi pakitud laiuse järgi (vähemalt 256px).
* Tekst vähendatakse, kuni see mahub (kuni `font_size_min=6`) ja kasutatakse sama fondi suurust kogu telje jaoks (reageerimised või veerud).
Kui fondi suurus on juba miinimumis, lõigatakse ülejäänud tekst.

**Alampiltide pakitud kujundus**
Kujundab alampildid (tavaliselt pakidest) kõige ruutlikumasse alasse (alampildi pakitud kujundus), välja arvatud `output_is_list=True`, mil juhul kasutatakse ainult ühte pilti igas lahtris ja loome loendi täis pildi ruudustikest.
Saad kasutada seda pildi ruudustike loendit, et ühendada teise XYZ-ruudustikulise graafiku sõlme, et luua super-ruudustikud.
Kui alampildid koosnevad erinevate suurustega pakidest, täidetakse puuduvad lahtrid tühi pildid.
Piltide arv lahtris (sh. pakitud pildid) peab olema kordne `rows * columns`.

### Sisendid

| Nimi | Tüüp | Kirjeldus |
| --- | --- | --- |
| `images` | `IMAGE` | Piltide loend (sh. pakkidega) |
| `row_labels` | `*` | Ridade sildid vasakul |
| `col_labels` | `*` | Veergude sildid üleval |
| `gap` | `INT` | Vahet alampildi pakitud vahel. Pange tähele, et alampildid ise kasutavad vahet. Kui soovid vahet alampiltide vahel, ühenda teine XYZ-ruudustikuline graafik sõlm. |
| `font_size` | `FLOAT` | Sihtmääratud fondi suurus. Tekst vähendatakse, kuni see mahub (kuni `font_size_min=6`). |
| `row_label_orientation` | `COMBO` | Ridade siltide teksti orientatsioon. Kasulik, kui soovid salvestada ruumi. |
| `order` | `BOOLEAN` | Määrab, millises järjest pildid töödeldakse. See on oluline ainult, kui sul on alampildid. Kasulik, kui `batch_size>1` ja soovid pakkide graafikut joonistada. |
| `output_is_list` | `BOOLEAN` | See on oluline ainult, kui sul on alampildid või soovid luua super-ruudustikud. |

### Väljundid

| Nimi | Tüüp | Kirjeldus |
| --- | --- | --- |
| `image` | `IMAGE 𝌠` | XYZ-ruudustikuline graafik. Kui `output_is_list=True`, loob pildiloendi, mille saad ühendada teise XYZ-ruudustikulise graafiku sõlmega, et luua super-ruudustikud. |

