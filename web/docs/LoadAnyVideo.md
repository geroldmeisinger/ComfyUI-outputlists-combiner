## Load Any Video

![Load Any Video](LoadAnyVideo/LoadAnyVideo.png)

(ComfyUI workflow included)

This node is a duplicate of nodes_video.py LoadVideo except with the fix included from [issue#11017](https://github.com/comfyanonymous/ComfyUI/issues/11017)
It is required to load videos based on annotated filepaths which are restricted to user directories.

### Inputs

| Name | Type | Description |
| --- | --- | --- |
| `file` | `STRING` |  |

### Outputs

| Name | Type | Description |
| --- | --- | --- |
| `None` | `VIDEO` |  |
