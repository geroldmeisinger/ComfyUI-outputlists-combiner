## Number OutputList

![Number OutputList](NumberOutputList/NumberOutputList.png)

(ComfyUI workflow included)

បង្កើត OutputList ដោយមានចន្លោះតម្លៃលេខ។
ប្រើ [numpy.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html) ដោយផ្ទាល់ ដោយសារថាត្រូវបានប្រើប្រាស់ដោយប្រាកដជាងនៅក្នុងតម្លៃ floating-point។
ប្រសិនបើអ្នកចង់កំណត់បញ្ជាក់លិស្សិតលេខដោយចំនួនជាមួយការផ្លាស់ប្ដូរបាន សូមពិនិត្យ JSON OutputList ហើយកំណត់អារេ ឧទាហរណ៍ `[1, 42, 123]`។
`int`, `float`, `string` និង `index` ប្រើ `is_output_list=True` (បានបញ្ជាក់ដោយសញ្ញា `𝌠`) ហើយនឹងត្រូវបានដំណើរការតាមលំដាប់ដោយផ្ទាល់ដោយអ្នកចាប់ផ្តើមនឹងការផ្លាស់ប្ដូរដែលមាន។

### បញ្ចូល

| ឈ្មោះ | ប្រភេទ | ការពិពណ៌នា |
| --- | --- | --- |
| `start` | `FLOAT` | តម្លៃចាប់ផ្តើមដើម្បីបង្កើតចន្លោះពីវានោះ។ |
| `stop` | `FLOAT` | តម្លៃចុងក្រោយ។ ប្រសិនបើ `endpoint=include` នោះតម្លៃនោះនឹងត្រូវបានបញ្ជូលក្នុងបញ្ជាក់។ |
| `num` | `INT` | ចំនួនធាតុនៅក្នុងបញ្ជាក់ (កុះកូនកាត់វានឹង `step`)។ |
| `endpoint` | `BOOLEAN` | សម្រាប់សំរាប់កំណត់តម្លៃ `stop` ត្រូវបានបញ្ជូលឬមិនបញ្ជូលនៅក្នុងធាតុ។ |

### លទ្ធផល

| ឈ្មោះ | ប្រភេទ | ការពិពណ៌នា |
| --- | --- | --- |
| `int` | `INT 𝌠` | តម្លៃដែលបានប្ដូរទៅជា int (បានកាត់ចោល/បានធ្វើឱ្យមានតម្លៃទាប)។ |
| `float` | `FLOAT 𝌠` | តម្លៃជា float។ |
| `string` | `STRING 𝌠` | តម្លៃជា float បានប្ដូរទៅជា string។ |
| `index` | `INT 𝌠` | ចន្លោះ 0..count ដែលអាចប្រើជា index បាន។ |
| `count` | `INT` | ដូចគ្នាទៅនឹង `num`។ |

