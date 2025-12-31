## String OutputList

![String OutputList](StringOutputList/StringOutputList.png)

(ComfyUI workflow san áireamh)

Cruthaíonn OutputList trí an teaghrán i réimse téacs a roinnt le separator.
Úsáideann `value` agus `index` `is_output_list=True` (sonraithe ag an t-síneadh `𝌠`) agus déanfar iad a phróiseáil go sequential trí na nódanna comhfhreagracha.

### Ionchuir

| Ainm | Cineál | Cur Síos |
| --- | --- | --- |
| `separator` | `STRING` | An teaghrán a úsáidtear chun luachanna réimse téacs a roinnt. |
| `values` | `STRING` | An téacs is mian leat a roinnt go liosta. Tabhair faoi deara go dtíodh an teaghrán de níos mó de charachtair nua, agus gach mír déanfar a thriomú ar an spás. |

### Aschuir

| Ainm | Cineál | Cur Síos |
| --- | --- | --- |
| `value` | `* 𝌠` | Na luachanna ón liosta. |
| `index` | `INT 𝌠` | Raon de 0..count. Is féidir leat é seo a úsáid mar index. |
| `count` | `INT` | An t-uimhir de níomhais sa liosta. |
| `inspect_combo` | `COMBO` | Aschur deimhne is féidir leat a nascadh le `COMBO` agus a líonadh leis na luachanna. Déanfar an nasc a athnascadh go huathoibríoch go aschur `value`. |

