## Number OutputList

![Number OutputList](NumberOutputList/NumberOutputList.png)

(ComfyUI workflow 포함)

숫자 값의 범위를 가진 OutputList를 생성합니다.
부동소수점 값에서 더 신뢰성 있게 작동하기 때문에 내부적으로 [numpy.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html)을 사용합니다.
임의의 단계로 숫자 목록을 정의하고 싶다면 JSON OutputList를 확인하고 배열을 정의하세요, 예를 들어 `[1, 42, 123]`.
`int`, `float`, `string` 및 `index`는 `is_output_list=True` (기호 `𝌠`으로 표시됨)를 사용하며, 해당 노드에 의해 순차적으로 처리됩니다.

### 입력

| 이름 | 유형 | 설명 |
| --- | --- | --- |
| `start` | `FLOAT` | 범위를 생성할 시작 값입니다. |
| `stop` | `FLOAT` | 끝 값입니다. `endpoint=include`인 경우 이 숫자는 목록에 포함됩니다. |
| `num` | `INT` | 목록의 항목 수 (`step`과 혼동하지 마세요). |
| `endpoint` | `BOOLEAN` | `stop` 값이 항목에 포함될지 제외될지를 결정합니다. |

### 출력

| 이름 | 유형 | 설명 |
| --- | --- | --- |
| `int` | `INT 𝌠` | 정수로 변환된 값 (내림/바닥). |
| `float` | `FLOAT 𝌠` | 실수로 된 값입니다. |
| `string` | `STRING 𝌠` | 실수로 변환된 값을 문자열로 표현한 값입니다. |
| `index` | `INT 𝌠` | 0..count 범위로, 인덱스로 사용할 수 있습니다. |
| `count` | `INT` | `num`과 같습니다. |

