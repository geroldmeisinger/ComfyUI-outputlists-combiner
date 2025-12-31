## Spreadsheet OutputList

![Spreadsheet OutputList](SpreadsheetOutputList/SpreadsheetOutputList.png)

(ComfyUI workflow ပါဝင်ပါသည်)

စာရင်းပြောင်း (`.csv .tsv .ods .xlsx .xls`) မှ OutputList များအများကြီးကို ဖြစ်စေပါသည်။
`Load any File` node ကိုအသုံးပြု၍ base64-encoding ဖြင့်ဖြင့်ဖိုင်တစ်ဖိုင်ကို တင်နိုင်ပါသည်။
အတွင်းရှိအတိုင်း *pandas* [read_excel](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html) နှင့် [read_csv](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html) ကိုအသုံးပြု၍ စာရင်းပြောင်းဖိုင်များကိုတင်ပါသည်။
အားလုံးသည် `is_output_list=True` ကိုအသုံးပြုပြီး (symbol `𝌠` ဖြင့်ပြသပါသည်) နှင့် အကြိမ်အတိုင်း အတူတူဖြစ်သော nodes များအား လုပ်ဆောင်ပါသည်။

### အတိုင်းအတွင်းများ

| နာမည် | အမျိုးအစား | ဖော်ပြချက် |
| --- | --- | --- |
| `rows_and_cols` | `STRING` | စာရင်းပြောင်းတွင် အမှတ်နှင့် အမည်များကို ပြောင်းပါ။ စာရင်းပြောင်းတွင် အမှတ်များကို ၁ မှစပြုပြီး အကွက်များကို A မှစပြုသည်။ OutputLists များသည် `select-nth` တွင် ၀ မှစပြုသည်။ |
| `header_rows` | `INT` | စာရင်းပြောင်းတွင် ပထမဆုံး x အမှတ်များကို မပြောင်းပါ။ `rows_and_cols` တွင် အကွက်ကို ပေးထားသည့်အခါသာ အသုံးပြုပါသည်။ |
| `header_cols` | `INT` | စာရင်းပြောင်းတွင် ပထမဆုံး x အကွက်များကို မပြောင်းပါ။ `rows_and_cols` တွင် အမှတ်ကို ပေးထားသည့်အခါသာ အသုံးပြုပါသည်။ |
| `select_nth` | `INT` | nth entry ကိုသာ ရွေးပါ (၀ မှစပြုပါသည်။) အသုံးပြုသူများအတွက် `PrimitiveInt+control_after_generate=increment` ပေါင်းစပ်ပြုလုပ်ရန် အသုံးပြုနိုင်ပါသည်။ |
| `string_or_base64` | `STRING` | CSV/TSV string သို့မဟုတ် စာရင်းပြောင်းဖိုင်တစ်ဖိုင်ကို base64 ဖြင့် (အမှတ်အသားများအတွက် `.ods .xlsx .xls`) အသုံးပြုပါ။ `Load Any File` node ကိုအသုံးပြု၍ ဖိုင်တစ်ဖိုင်ကို base64 အဖြစ်တင်ပါ။ |

### ထုတ်လုပ်မှုများ

| နာမည် | အမျိုးအစား | ဖော်ပြချက် |
| --- | --- | --- |
| `list_a` | `STRING 𝌠` |  |
| `list_b` | `STRING 𝌠` |  |
| `list_c` | `STRING 𝌠` |  |
| `list_d` | `STRING 𝌠` |  |
| `count` | `INT` | အရှည်ဆုံးစာရင်းတွင် အရာအား အရေအတွက်ပါဝင်ပါသည်။ |

