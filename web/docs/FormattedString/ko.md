## 형식화된 문자열

![형식화된 문자열](FormattedString/FormattedString.png)

(ComfyUI workflow 포함)

 자리 표시자 변수를 포함하는 문자열을 생성하고 해당 값을 대체합니다.
내부적으로 파이썬 `str.format()` 을 사용하며, [Python - Format String Syntax](https://docs.python.org/3/library/string.html#format-string-syntax) 를 참조하세요.
* `{a:.2f}` 를 사용하여 실수를 2자리 소수로 반올림할 수 있습니다.
* `{a:05d}` 를 사용하여 comfys 파일 이름 접미사 `ComfyUI_00001_.png` 에 맞추기 위해 최대 5자리의 앞쪽 0으로 채울 수 있습니다.
* 문자열 내에 `{ }` 을 작성하고 싶다면 (예: JSON의 경우) 이를 두 번 작성해야 합니다: `{{ }}`.

또한 `%date:yyyy-MM-dd hh:mm:ss%` 및 `%KSampler.seed%` 와 같은 *검색 및 교체(S&R) 구문*도 적용됩니다.
따라서 이 노드를 `GET-node` 로도 사용할 수 있습니다.
"검색 및 교체"는 자바스크립트 컨텍스트에서 실행되며 노드 실행 전에 실행된다는 점에 주의하세요.

### 입력

| 이름 | 유형 | 설명 |
| --- | --- | --- |
| `fstring` | `STRING` | 자리 표시자 변수를 포함하는 문자열을 생성하고 해당 값을 대체합니다.<br>내부적으로 파이썬 `str.format()` 을 사용하며, [Python - Format String Syntax](https://docs.python.org/3/library/string.html#format-string-syntax) 를 참조하세요.<br>* `{a:.2f}` 를 사용하여 실수를 2자리 소수로 반올림할 수 있습니다.<br>* `{a:05d}` 를 사용하여 comfys 파일 이름 접미사 `ComfyUI_00001_.png` 에 맞추기 위해 최대 5자리의 앞쪽 0으로 채울 수 있습니다.<br>* 문자열 내에 `{ }` 을 작성하고 싶다면 (예: JSON의 경우) 이를 두 번 작성해야 합니다: `{{ }}`.<br><br>또한 `%date:yyyy-MM-dd hh:mm:ss%` 및 `%KSampler.seed%` 와 같은 *검색 및 교체(S&R) 구문*도 적용됩니다.<br>따라서 이 노드를 `GET-node` 로도 사용할 수 있습니다.<br>"검색 및 교체"는 자바스크립트 컨텍스트에서 실행되며 노드 실행 전에 실행된다는 점에 주의하세요. |
| `a` | `*` | (선택사항) `{a}` 자리 표시자에 문자열로 표시될 값입니다. |
| `b` | `*` | (선택사항) `{b}` 자리 표시자에 문자열로 표시될 값입니다. |
| `c` | `*` | (선택사항) `{c}` 자리 표시자에 문자열로 표시될 값입니다. |
| `d` | `*` | (선택사항) `{d}` 자리 표시자에 문자열로 표시될 값입니다. |

### 출력

| 이름 | 유형 | 설명 |
| --- | --- | --- |
| `string` | `STRING` | 모든 자리 표시자가 해당 값으로 대체된 형식화된 문자열입니다. |

