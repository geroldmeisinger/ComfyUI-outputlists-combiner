## Workflow Discriminator

![Workflow Discriminator](WorkflowDiscriminator/WorkflowDiscriminator.png)

(ComfyUI workflow ပါဝင်ပါသည်)

Workflow များကို ရှိနှိုင်းပြီး အသုံးပြုသူအတွက် သို့မဟုတ် အများအားဖြင့် workflow တစ်ခုကို ပြောင်းလဲရန် အတွက် အသုံးပြုသည့် OutputList များအဖြစ် မျှော်လင့်မှုတစ်ခုကို ပြုလုပ်ပေးသည်။
သင်သည် အများအားဖြင့် အတူတူသော workflow ဖြင့် ပြုလုပ်ထားသော ဓာတ်ပုံများအတွက် တစ်ခုချင်းစီ သူ့ကို ဖြစ်ပွားခဲ့သော ဓာတ်ပုံများကို ပြန်လည်ရယူရန် ဤ node ကို အသုံးပြုနိုင်ပါသည်။
ComfyUI အတွက် `IMAGE` သည် workflow metadata များကို မပါဝင်သော်လည်း သင်သည် ပြောင်းလဲသော ဓာတ်ပုံများကို အသုံးပြုရန် အတွက် အထူးသဖြင့် ဓာတ်ပုံ + metadata loader များကို အသုံးပြုပြီး သူ့ကို ဤ node တွင် ချိတ်ဆက်ရန် လိုအပ်ပါသည်။
metadata loader များကို ပေါင်းထည့်ထားသော custom node များသည် အောက်ပါအတိုင်းဖြစ်ပါသည်။
* `Load Any File.metadata` -> `JSON OutputList(jsonpath=$.["PNG:Prompt"]).value`
* [Crystool](https://github.com/crystian/ComfyUI-Crystools) `🪛 Load image with metadata.Metadata RAW` -> `🪛 Metadata extractor.prompt`
* [Simple_Readable_Metadata](https://github.com/ShammiG/ComfyUI-Simple_Readable_Metadata-SG) `Simple Readable Metadata-SG.metadata_raw`

### ထောင့်အတွက်

| နာမည် | အမျိုးအစား | ဖော်ပြချက် |
| --- | --- | --- |
| `objs_0` | `*` | (မဖြစ်မီ) အများအားဖြင့် workflow တစ်ခု၏ အရာတစ်ခု (သို့မဟုတ် အရာများစွာ) ဖြစ်သည်။ `objs_0` နှင့် `more_objs` သည် ပေါင်းစပ်၍ အလွယ်တကူ အသုံးပြုရန် အတွက် အသုံးပြုသည်။ သင်သည် အရာနှစ်ခုကို ရှိနှိုင်းချင်သော အခါ သာ အသုံးပြုပါသည်။ |
| `more_objs` | `*` | (မဖြစ်မီ) အများအားဖြင့် workflow တစ်ခု၏ အရာတစ်ခု (သို့မဟုတ် အရာများစွာ) ဖြစ်သည်။ `objs_0` နှင့် `more_objs` သည် ပေါင်းစပ်၍ အလွယ်တကူ အသုံးပြုရန် အတွက် အသုံးပြုသည်။ သင်သည် အရာနှစ်ခုကို ရှိနှိုင်းချင်သော အခါ သာ အသုံးပြုပါသည်။ |
| `ignore_jsonpaths` | `STRING` | (မဖြစ်မီ) သင်သည် အများအားဖြင့် အသုံးပြုသော JSONPath များကို အမှားယွင်းမှုကို ဖြစ်စေရန် အတွက် သို့မဟုတ် အများအားဖြင့် အများအားဖြင့် အသုံးပြုသော discriminator များကို ပေါင်းစပ်ရန် အတွက် အသုံးပြုပါသည်။ |

### ထုတ်လုပ်မှုများ

| နာမည် | အမျိုးအစား | ဖော်ပြချက် |
| --- | --- | --- |
| `list_a` | `* 𝌠` |  |
| `list_b` | `* 𝌠` |  |
| `list_c` | `* 𝌠` |  |
| `list_d` | `* 𝌠` |  |
| `jsonpaths` | `STRING 𝌠` |  |

