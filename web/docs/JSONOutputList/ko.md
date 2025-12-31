## JSON OutputList

![JSON OutputList](JSONOutputList/JSONOutputList.png)

(ComfyUI workflow 포함)

JSON 객체에서 배열이나 딕셔너리를 추출하여 OutputList를 생성합니다.
값을 추출하기 위해 JSONPath 구문을 사용하며, [JSONPath on Wikipedia](https://en.wikipedia.org/wiki/JSONPath) 를 참조하세요.
모든 일치하는 값은 하나의 긴 목록으로 평탄화됩니다.
또한 `[1, 2, 3]` 과 같은 리터럴 문자열에서 객체를 생성하는 데에도 이 노드를 사용할 수 있습니다.
`key`, `value`, `int` 및 `float` 은 `is_output_list=True` (기호 `𝌠` 으로 표시됨) 를 사용하며, 해당 노드에 의해 순차적으로 처리됩니다.

### 입력

| 이름 | 유형 | 설명 |
| --- | --- | --- |
| `jsonpath` | `STRING` | 값을 추출하는 데 사용되는 JSONPath입니다. |
| `json` | `STRING` | 객체로 변환되는 JSON 문자열입니다. |
| `obj` | `*` | (선택사항) JSON 문자열을 대체할 모든 유형의 객체 |

### 출력

| 이름 | 유형 | 설명 |
| --- | --- | --- |
| `key` | `STRING 𝌠` | 딕셔너리의 키 또는 배열의 인덱스 (문자열로). 기술적으로 모든 키가 아닌 항목에 대해 평탄화된 목록의 전역 인덱스입니다. |
| `value` | `STRING 𝌠` | 문자열로 된 값입니다. |
| `int` | `INT 𝌠` | 값이 정수로 (숫자를 파싱할 수 없는 경우 기본값은 0)입니다. |
| `float` | `FLOAT 𝌠` | 값이 실수로 (숫자를 파싱할 수 없는 경우 기본값은 0)입니다. |
| `count` | `INT` | 평탄화된 목록의 총 항목 수 |
| `debug` | `STRING` | 모든 일치하는 객체의 디버그 출력을 형식화된 JSON 문자열로 표시합니다 |

