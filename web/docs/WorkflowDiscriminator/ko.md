## Workflow Discriminator

![Workflow Discriminator](WorkflowDiscriminator/WorkflowDiscriminator.png)

(ComfyUI workflow 포함)

워크플로를 비교하고 다른 값을 개별 OutputList로 추출하기 위해 분류합니다.
이 노드를 사용하여 동일한 워크플로를 사용하는 이미지 목록에서 각 개별 이미지가 어떻게 생성되었는지 복원할 수 있습니다.
ComfyUI의 `IMAGE`에는 워크플로 메타데이터가 포함되어 있지 않으며, 전문적인 이미지+메타데이터 로더로 이미지를 로드하고 메타데이터를 이 노드에 연결해야 합니다.
메타데이터 로더를 포함한 사용자 정의 노드는 다음과 같습니다:
* `Load Any File.metadata` -> `JSON OutputList(jsonpath=$.["PNG:Prompt"]).value`
* [Crystool](https://github.com/crystian/ComfyUI-Crystools) `🪛 Load image with metadata.Metadata RAW` -> `🪛 Metadata extractor.prompt`
* [Simple_Readable_Metadata](https://github.com/ShammiG/ComfyUI-Simple_Readable_Metadata-SG) `Simple Readable Metadata-SG.metadata_raw`

### 입력

| 이름 | 유형 | 설명 |
| --- | --- | --- |
| `objs_0` | `*` | (선택 사항) 단일 객체(또는 객체 목록), 일반적으로 워크플로의 객체입니다. `objs_0`과 `more_objs`는 연결되어 있으며, 두 객체만 비교하려는 경우 편의를 위해 존재합니다. |
| `more_objs` | `*` | (선택 사항) 다른 객체(또는 객체 목록), 일반적으로 워크플로의 객체입니다. `objs_0`과 `more_objs`는 연결되어 있으며, 두 객체만 비교하려는 경우 편의를 위해 존재합니다. |
| `ignore_jsonpaths` | `STRING` | (선택 사항) 여러 분류기를 연결하려는 경우 무시할 JSONPaths 목록입니다. |

### 출력

| 이름 | 유형 | 설명 |
| --- | --- | --- |
| `list_a` | `* 𝌠` |  |
| `list_b` | `* 𝌠` |  |
| `list_c` | `* 𝌠` |  |
| `list_d` | `* 𝌠` |  |
| `jsonpaths` | `STRING 𝌠` |  |

