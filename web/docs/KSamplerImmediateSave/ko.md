## KSampler Immediate Save

![KSampler Immediate Save](KSamplerImmediateSave/KSamplerImmediateSave.png)

(ComfyUI workflow 포함)

기본 `CheckpointLoader`, `KSampler`, `VAE Decode` 및 `Save Image` 노드를 하나로 처리하기 위한 확장 노드입니다.
이 노드는 그리드를 위한 중간 이미지를 즉시 저장하고 싶을 때 유용합니다.

*"이미지를 저장하기 위해 특별히 만든 KSampler? 이제 내가 막을려고 했던 것과 같은 존재가 되어버렸다!"*

### 입력

| 이름 | 유형 | 설명 |
| --- | --- | --- |
| `cpkt_name` | `COMBO` | 로드할 체크포인트(모델)의 이름입니다. |
| `positive` | `STRING` | 이미지에 포함하고 싶은 속성을 설명하는 조건입니다. |
| `negative` | `STRING` | 이미지에서 제외하고 싶은 속성을 설명하는 조건입니다. |
| `latent_image` | `LATENT` | 노이즈를 제거할 잠재 이미지입니다. |
| `seed` | `INT` | 노이즈 생성에 사용되는 난수 시드입니다. |
| `steps` | `INT` | 노이즈 제거 프로세스에 사용되는 단계 수입니다. |
| `cfg` | `FLOAT` | 분류자 없음 안내 규모는 창의성과 프롬프트 준수 사이의 균형을 맞춥니다. 높은 값은 프롬프트에 더 가까운 이미지를 생성하지만 너무 높은 값은 품질에 부정적인 영향을 줄 수 있습니다. |
| `sampler_name` | `COMBO` | 샘플링 시 사용되는 알고리즘으로, 이는 생성된 출력의 품질, 속도 및 스타일에 영향을 줄 수 있습니다. |
| `scheduler` | `COMBO` | 스케줄러는 이미지를 형성하기 위해 점진적으로 노이즈를 제거하는 방식을 제어합니다. |
| `denoise` | `FLOAT` | 적용되는 노이즈 제거량으로, 낮은 값은 초기 이미지의 구조를 유지하여 이미지 간 샘플링을 가능하게 합니다. |
| `filename_prefix` | `STRING` | 저장할 파일의 접두사입니다. 이는 %date:yyyy-MM-dd% 또는 %Empty Latent Image.width%와 같은 형식 정보를 포함할 수 있으며, 노드에서 값을 포함할 수 있습니다. |

### 출력

| 이름 | 유형 | 설명 |
| --- | --- | --- |
| `image` | `IMAGE` | 디코딩된 이미지입니다. |

