## Workflow Discriminator

![Workflow Discriminator](WorkflowDiscriminator/WorkflowDiscriminator.png)

(ComfyUI workflow qo'shildi)

Workflowlarni solishtiradi va ularni ajratib, alohida chiqish ro'yxatlar sifatida turlicha qiymatlarni ajratadi.
Ushbu nodeni bir xil workflowdan yaratilgan rasm ro'yxatidan har bir rasm qanday yaratilganini tiklash uchun foydalanishingiz mumkin.
ComfyUI ning `IMAGE` workflow metama'lumotlarini o'z ichiga olmaganligini eslang va rasmni maxsus rasm+metama'lumot yuklagichlar bilan yuklashingiz va metama'lumotlarni ushbu nodaga ulashingiz kerak.
Metama'lumot yuklagichlar bilan maxsus nodlar quyidagilar:
* `Load Any File.metadata` -> `JSON OutputList(jsonpath=$.["PNG:Prompt"]).value`
* [Crystool](https://github.com/crystian/ComfyUI-Crystools) `🪛 Load image with metadata.Metadata RAW` -> `🪛 Metadata extractor.prompt`
* [Simple_Readable_Metadata](https://github.com/ShammiG/ComfyUI-Simple_Readable_Metadata-SG) `Simple Readable Metadata-SG.metadata_raw`

### Kirishlar

| Ism | Tur | Tavsif |
| --- | --- | --- |
| `objs_0` | `*` | (ixtiyoriy) Bitta ob'ekt (yoki ob'ektlar ro'yxati), odatda workflow. `objs_0` va `more_objs` birlashtiriladi va ikkalasi ham qulaylik uchun mavjud, agar siz faqat ikkita ob'ektni solishtirmoqchi bo'lsangiz. |
| `more_objs` | `*` | (ixtiyoriy) Boshqa ob'ekt (yoki ob'ektlar ro'yxati), odatda workflow. `objs_0` va `more_objs` birlashtiriladi va ikkalasi ham qulaylik uchun mavjud, agar siz faqat ikkita ob'ektni solishtirmoqchi bo'lsangiz. |
| `ignore_jsonpaths` | `STRING` | (ixtiyoriy) Agar siz bir nechta diskriminatorlarni bir-biri bilan ulamoqchi bo'lsangiz, e'tibor bermaslik kerak bo'lgan JSONPathlar ro'yxati. |

### Chiqishlar

| Ism | Tur | Tavsif |
| --- | --- | --- |
| `list_a` | `* 𝌠` |  |
| `list_b` | `* 𝌠` |  |
| `list_c` | `* 𝌠` |  |
| `list_d` | `* 𝌠` |  |
| `jsonpaths` | `STRING 𝌠` |  |

