## Workflow Discriminator

![Workflow Discriminator](WorkflowDiscriminator/WorkflowDiscriminator.png)

(ComfyUI workflow daxildədir)

Workflow-ləri müqayisə edir və fərqli dəyərləri ayırmalı OutputList-lər kimi çıxarmaq üçün onları ayırd edir.
Bu node-ni eyni workflow ilə siyahıdan hər bir şəklin necə yaradıldığını bərpa etmək üçün istifadə edə bilərsiniz.
ComfyUI-nin `IMAGE` workflow metadata-ı ehtiva etmir və şəkilləri xüsusi şəkildə metadata loader-lar ilə yükləməli və metadata-nı bu node-a qoşmalısınız.
Metadata loader-lar ilə xüsusi node-lar:
* `Load Any File.metadata` -> `JSON OutputList(jsonpath=$.["PNG:Prompt"]).value`
* [Crystool](https://github.com/crystian/ComfyUI-Crystools) `🪛 Load image with metadata.Metadata RAW` -> `🪛 Metadata extractor.prompt`
* [Simple_Readable_Metadata](https://github.com/ShammiG/ComfyUI-Simple_Readable_Metadata-SG) `Simple Readable Metadata-SG.metadata_raw`

### Girişlər

| Ad | Tip | İzahat |
| --- | --- | --- |
| `objs_0` | `*` | (isteğe bağlı) Workflow-nin adətən bir obyekti (və ya obyekt siyahısı). `objs_0` və `more_objs` birləşdiriləcək və sadələşdirmək üçün mövcuddur, yalnız iki obyekt müqayisə etmək istəyirsinizsə. |
| `more_objs` | `*` | (isteğe bağlı) Workflow-nin adətən bir obyekti (və ya obyekt siyahısı). `objs_0` və `more_objs` birləşdiriləcək və sadələşdirmək üçün mövcuddur, yalnız iki obyekt müqayisə etmək istəyirsinizsə. |
| `ignore_jsonpaths` | `STRING` | (isteğe bağlı) Əgər bir neçə discriminator-ləri birləşdirmək istəyirsinizsə, nəzərə almaq üçün JSONPath-lərin siyahısı. |

### Çıxışlar

| Ad | Tip | İzahat |
| --- | --- | --- |
| `list_a` | `* 𝌠` |  |
| `list_b` | `* 𝌠` |  |
| `list_c` | `* 𝌠` |  |
| `list_d` | `* 𝌠` |  |
| `jsonpaths` | `STRING 𝌠` |  |

