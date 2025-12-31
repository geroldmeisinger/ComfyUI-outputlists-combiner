## OutputLists 조합

![OutputLists Combinations](CombineOutputLists/CombineOutputLists.png)

(ComfyUI 워크플로우 포함)

최대 4개의 OutputLists를 받아 그것들의 모든 조합을 생성합니다.

예시: `[1, 2, 3] x ["A", "B"] = [(1, "A"), (1, "B"), (2, "A"), (2, "B"), (3, "A"), (3, "B")]`

`unzip_a` .. `unzip_d` 는 `is_output_list=True` (기호 `𝌠` 로 표시됨) 를 사용하며, 해당 노드에 의해 순차적으로 처리됩니다.

모든 리스트는 선택 사항이며, 빈 리스트는 무시됩니다.

기술적으로 이 노드는 *카르테시안 곱*을 계산하여 각 조합을 요소별로 분할하여 출력합니다 (`unzip`), 빈 리스트는 `None` 값으로 대체되며, 해당 출력에서는 `None`을 방출합니다.

예시: `[1, 2] x [] x ["A", "B"] x [] = [(1, None, "A", None), (1, None, "B", None), (2, None, "A", None), (2, None, "B", None)]`

### 입력

| 이름 | 타입 | 설명 |
| --- | --- | --- |
| `list_a` | `*` | (선택 사항) |
| `list_b` | `*` | (선택 사항) |
| `list_c` | `*` | (선택 사항) |
| `list_d` | `*` | (선택 사항) |

### 출력

| 이름 | 타입 | 설명 |
| --- | --- | --- |
| `unzip_a` | `* 𝌠` | `list_a`에 해당하는 조합의 값. |
| `unzip_b` | `* 𝌠` | `list_b`에 해당하는 조합의 값. |
| `unzip_c` | `* 𝌠` | `list_c`에 해당하는 조합의 값. |
| `unzip_d` | `* 𝌠` | `list_d`에 해당하는 조합의 값. |
| `index` | `INT 𝌠` | 인덱스로 사용할 수 있는 0..count 범위. |
| `count` | `INT` | 총 조합 수. |

