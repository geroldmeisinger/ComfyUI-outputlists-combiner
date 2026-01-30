# Third-party custom nodes

I consider the following custom nodes essential for any ComfyUI installation and especially for this custom node pack:

- [KJNodes](https://github.com/kijai/ComfyUI-KJNodes)
- [rgthree](https://github.com/rgthree/rgthree-comfy)
- [ComfyUI Essentials](https://github.com/cubiq/ComfyUI_essentials)
- [Impact-Pack](https://github.com/ltdrdata/ComfyUI-Impact-Pack)
- [Crystools](https://github.com/crystian/ComfyUI-Crystools)
- [WAS Node Suite](https://github.com/ltdrdata/was-node-suite-comfyui) [(old)](https://github.com/WASasquatch/was-node-suite-comfyui)
- [Custom Scripts](https://github.com/pythongosssss/ComfyUI-Custom-Scripts)

Remember that the core feature of OutputLists Combiner revolves around [data lists](https://docs.comfy.org/custom-nodes/backend/lists). One of my design goals was to introduce new custom nodes only if they are necessary in every common use-case and avoid cluttering with more duplicate functionality that is already available in other essential nodes. The following is a reference of useful third-party custom nodes which support the use of data lists, multi-prompting or XYZ-GridPlots. The list is opionated and incomplete on purpose. I left out: specializations (string lists, mask lists), niche-uses, endless list manipulation variants, and unpopular custom node packs.

Many custom nodes provide some support for data lists, multi-prompting and XYZ-GridPlots but always lack some essential features, resort to black magic or are not thought all the way through. I also want use this reference to discuss some shortcomings of other nodes and make some arguments why the OutputLists Combiner was necessary.

## Data Lists

Any node which declares `INPUT_IS_LIST = True` or `OUTPUT_IS_LIST = (..., True, ...)` (in Scheme v1), `is_output_list = True` or `is_input_list = True` (in [Scheme v3](https://docs.comfy.org/custom-nodes/v3_migration)) makes use of [data lists](https://docs.comfy.org/custom-nodes/backend/lists). You can search for these patterns in code if want to find which ones make use of it.

### Core

`Rebatch Images`

![Rebatch Images](/media/Core_RebatchImages.png)

`ImageFromBatch`

![ImageFromBatch](/media/Core_ImageFromBatch.png)

- Useful in conjunction with the [PrimitiveInt control_after_generate=increment pattern](https://github.com/geroldmeisinger/ComfyUI-outputlists-combiner?tab=readme-ov-file#the-primitiveint-control_after_generateincrement-pattern).
- Also see `Select Nth Item (Any list)`.

### Custom Scripts

[Custom Scripts](https://github.com/pythongosssss/ComfyUI-Custom-Scripts)

`Show Text`

![Show Text](/media/CustomScripts_ShowText.png)

The main advantage of this node is that it adds a new entry for every list item, whereas most other string output nodes only show the first or last entry.

`Repeater`

![Repeater](/media/CustomScripts_Repeater.png)

### Impact Pack

[Impact-Pack](https://github.com/ltdrdata/ComfyUI-Impact-Pack)

`List Bridge`

![List Bridge](/media/ImpactPack_ListBridge.png)

Uses `INPUT_IS_LIST=True` which means it collects and concatenates all input lists.

`Make List (Any)`

![Make List (Any)](/media/ImpactPack_MakeListAny.png)

- Useful if you want to manually create a data list.
- Also see `List of Any`.

`Make Image List`

![Make Image List](/media/ImpactPack_MakeImageList.png)

Same as `Make List (Any)` except it's type-safe on images.

`Select Nth Item (Any list)`

![Select Nth Item (Any list)](/media/ImpactPack_SelectNthItem.png)

- Useful in conjunction with the [PrimitiveInt control_after_generate=increment pattern](https://github.com/geroldmeisinger/ComfyUI-outputlists-combiner?tab=readme-ov-file#the-primitiveint-control_after_generateincrement-pattern).
- Also see `ImageFromBatch`.

`Image List To Image Batch`

![Image List To Image Batch](/media/ImpactPack_ImageListToImageBatch.png)

`Image Batch To Image List`

![Image Batch To Image List](/media/ImpactPack_ImageBatchToImageList.png)

### Inspire Pack

[Inspire Pack](https://github.com/ltdrdata/ComfyUI-Inspire-Pack)

`Float Range`

![Float Range](/media/InspirePack_FloatRange.png)

An alternative to [Number OutputList](https://github.com/geroldmeisinger/ComfyUI-outputlists-combiner?tab=readme-ov-file#number-outputlist) if you prefer `steps` instead.

### Crystools

`Pipe To` and `Pipe From`

![Pipe To and Pipe From](/media/Crystools_Pipe.png)

`List of Any`

![List of Any](/media/Crystools_ListOfAny.png)

- Useful if you want to manually create a data list.
- Also see `Make List (Any)`.

### KJNodes

[KJNodes](https://github.com/kijai/ComfyUI-KJNodes)

`Get Images From Batch Indexed`

![Get Images From Batch Indexed](/media/Crystools_GetImagesFromBatchIndexed.png)

### ComfyUI Essentials

[ComfyUI Essentials](https://github.com/cubiq/ComfyUI_essentials)

`Batch Count` and `Get Image Size`

![Batch Count](/media/ComfyUIEssentials_BatchCount.png)
![Get Image Size](/media/ComfyUIEssentials_GetImageSize.png)

`Image List To Batch`

![Image List To Batch](/media/ComfyUIEssentials_ImageListToBatch.png)

An alternative to `Image List To Image Batch` although I recommend the Impact-Pack version because it also provides the inverse.

### Easy-Use

[Easy-Use](https://github.com/yolain/ComfyUI-Easy-Use)

`Length Any`

![Length Any](/media/EasyUse_LengthAny.png)

`Index Any`

![Index Any](/media/EasyUse_IndexAny.png)

An alternative to `Select Nth Item (Any list)`

`Image List To Image Batch`

![Image List To Image Batch](/media/EasyUse_ImageListToImageBatch.png)

An alternative to the Impact-Pack variant.

`Image Batch To Image List`

![Image Batch To Image List](/media/EasyUse_ImageBatchToImageList.png)

An alternative to the Impact-Pack variant.

### ComfyRoll

[ComfyRoll](https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes)

See [List Nodes](https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/List-Nodes)

### Basic Data Handling

[Basic Data Handling](https://github.com/StableLlama/ComfyUI-basic_data_handling)

See [Data List](https://github.com/StableLlama/ComfyUI-basic_data_handling#data-list)

### Bjornulf

[Bjornulf Custom nodes](https://github.com/justUmen/Bjornulf_custom_nodes)

### Job Iterator

[Job-Iterator](https://github.com/ali1234/comfyui-job-iterator)

## Multi-Prompts

### Core

`Load Image Dataset from Folder`

![Load Image Dataset from Folder](/media/Core_LoadImageDatasetFromFolder.png)

- Core node, but I recommend [Load Any File](https://github.com/geroldmeisinger/ComfyUI-outputlists-combiner?tab=readme-ov-file#load-any-file) instead.
- Note: this is a BETA node and you need to activate experimental nodes in settings.

`Regex`

### Impact-Pack

[Impact-Pack](https://github.com/ltdrdata/ComfyUI-Impact-Pack)

### Inspire-Pack

[Inspire-Pack](https://github.com/ltdrdata/ComfyUI-Inspire-Pack)

`Load Image List From Dir (Inspire)` and `Load Image Batch From Dir (Inspire)`)

![Load Image List From Dir](/media/InspirePack_LoadImageListFromDir.png)
![Load Image Batch From Dir](/media/InspirePack_LoadImageBatchFromDir.png)

- Allows to load from arbitrary directory (warning: this has security implications!).
- I recommend [Load Any File](https://github.com/geroldmeisinger/ComfyUI-outputlists-combiner?tab=readme-ov-file#load-any-file) instead, but this one provides more settings.

`Load Prompts From Dir`

![Load Prompts From Dir](/media/InspirePack_LoadPromptsFromDir.png)

`Load Prompts From File`

![Load Prompts From File](/media/InspirePack_LoadPromptsFromFile.png)

### Easy-Use

See [PromptList](https://docs.easyuse.yolain.com/en/nodes/prompt#promptlist)

See [Wildcards](https://docs.easyuse.yolain.com/en/nodes/prompt#wildcards)

## List-like types

When you open the node searchbox and filter by types you often stumble upon list-like types, which are not actual data lists, and contribute to some confusion:

- `FLOATS` from Core and only used in `Create Hook Keyframes From Floats`
- `LIST` from [WAS Node Suite](https://github.com/ltdrdata/was-node-suite-comfyui) [(old)](https://github.com/WASasquatch/was-node-suite-comfyui): a wrapper for python list of any type
- `ListString` from [Crystools](https://github.com/crystian/ComfyUI-Crystools): a wrapper for python list of strings
- `RangeFloat` and `RangeInt` from [Easy-Use](https://github.com/yolain/ComfyUI-Easy-Use)
- `INT,FLOAT` from [ComfyUI Essentials](https://github.com/cubiq/ComfyUI_essentials): a variable type which supports `INT` and `FLOAT`, sometimes declared as `NUMBER`

## XYZ-GridPlots

### OutputLists Combiner

**Recommended!**

[OutputLists Combiner](https://github.com/geroldmeisinger/ComfyUI-outputlists-combiner)

- very versatile dispite the minimal amount of nodes
- native integration of LoRAs, checkpoints and other COMBOs, no custom KSampler required
- lots of examples
- lots of documentation including multi-lingual node documentation

### Images Grid

[Images Grid](https://github.com/LEv145/images-grid-comfy-plugin)

- Very simple and intuitive but restricted feature set
- Minor issue: manual list population with separators instead of native lists
- Minor issue: duplicate nodes (`ImagesGridByColumns`, `ImagesGridByRows`)

### Core

`Image Grid`

- Simple image grid but no support for labels
- Note: this is a BETA node and you need to activate experimental nodes in settings

### WAS Node Suite

[WAS Node Suite](https://github.com/ltdrdata/was-node-suite-comfyui) [(old)](https://github.com/WASasquatch/was-node-suite-comfyui)

`Create Grid Image` and `Create Grid Image from Batch`

- Simple image grid but no support for labels

### Soze

[Soze](https://github.com/SozeInc/ComfyUI_Soze)

- versatile due to data lists
- requires a lot of manual entries due to extra textfields for every input
- no documentation, no examples, only a node overview image

### Easy-Use

[Easy-Use](https://github.com/yolain/ComfyUI-Easy-Use)

`xyAny`

- [No documentation](https://docs.easyuse.yolain.com/en/nodes/xyInputs)
- [Useless and hidden example](https://github.com/yolain/ComfyUI-Yolain-Workflows?tab=readme-ov-file#1-7-xy%E5%AF%B9%E6%AF%94)

### ComfyRoll

[ComfyRoll](https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes)

- [Useless examples](https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/XY-Grid-Nodes)

### TinyTerra

[TinyTerra](https://github.com/TinyTerra/ComfyUI_tinyterraNodes)

`xyPlot` (and `advanced xyPlot`)

- requires custom KSampler and doesn't integrate natively with ComfyUI
- requires to learn custom syntax to enter images and labels manually, or use custom context-menu black magic to fill entries, or use extra nodes to generate them

### Efficiency Nodes

[Efficiency Nodes](https://github.com/LucianoCirino/efficiency-nodes-comfyui)

- requires custom KSampler
- lots of specialized nodes for singular use-cases (for Sampler/Scheduler, LoRAs etc.)

### D2 Nodes

[D2 Nodes](https://github.com/da2el-ai/D2-nodes-ComfyUI)

- [hidden examples](https://github.com/da2el-ai/D2-nodes-ComfyUI/tree/main/workflow)
- requires custom KSampler
- lots of specialized nodes for singular use-cases (for Sampler/Scheduler, LoRAs etc.)

### qq-nodes

[qq-nodes](https://github.com/kenjiqq/qq-nodes-comfyui)

- requires multiple round-trip black magic to populate the grid
