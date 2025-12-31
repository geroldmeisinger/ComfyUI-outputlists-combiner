## String OutputList

![String OutputList](StringOutputList/StringOutputList.png)

(ComfyUI workflow 포함)

입력 필드의 문자열을 구분자로 분할하여 OutputList를 생성합니다.
`value`와 `index`는 `is_output_list=True` (기호 `𝌠`으로 표시됨)를 사용하며, 해당 노드에 의해 순차적으로 처리됩니다.

### 입력

| 이름 | 유형 | 설명 |
| --- | --- | --- |
| `separator` | `STRING` | 텍스트 필드 값을 분할하는 데 사용되는 문자열입니다. |
| `values` | `STRING` | 목록으로 분할하려는 텍스트입니다. 문자열은 분할 전에 후행 개행 문자를 제거하고, 각 항목은 다시 공백 문자를 제거한다는 점에 주의하세요. |

### 출력

| 이름 | 유형 | 설명 |
| --- | --- | --- |
| `value` | `* 𝌠` | 목록의 값들입니다. |
| `index` | `INT 𝌠` | 0..count 범위입니다. 인덱스로 사용할 수 있습니다. |
| `count` | `INT` | 목록의 항목 수입니다. |
| `inspect_combo` | `COMBO` | `COMBO`에 연결하여 값으로 미리 채우는 데 사용할 수 있는 더미 출력입니다. 연결은 자동으로 `value` 출력으로 다시 연결됩니다. |

