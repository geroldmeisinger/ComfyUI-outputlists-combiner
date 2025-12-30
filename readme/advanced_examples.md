# Advanced Examples

## XYZ-GridPlots with Supergrids

I recommend to start ComfyUI with `--cache-ram` for this example if you want to experiment with the settings alot!

![XYZ-GridPlots with Supergrids example](/workflows/ExampleAdv_00a_XYZGridPlot_Supergrids.png)

(ComfyUI workflow included)

Uses two `XYZ-GridPlot` in sequence to put one image grid inside the other. For more complex image grids the question always is: How should the axis be ordered and in which way the images be shuffled, e.g. do we want to show `cat|dog|rat` x `red|blue|green` and then the batch next to each other in a subgrid (`RxCxB`), or four separate images each with a grid of `cat|dog|rat` x `red|blue|green` (`BxCxR`). To achieve this you can play around with the options `order=outside-in|inside-out` and `output_is_list=False|True`, but make sure the `row_labels` and `col_labels` match what you want to achieve, as this info is also used how the grid is shaped.

## Immediately save intermediate images of image grid

One thing you may have noticed when you make a large image grid is that you have to wait for ALL intermediate images to be processed before anything is saved and the grid created. Thus you could loose a lot of processed images when something happens or you cancel the job (though ComfyUI keeps them in cache and should pick up immediately). If you want to save the intermediate images after each step you can use the `KSampler immediate Save Image` beta-node. For this node to be visible in the node searchbox you need to activate `Settings -> Comfy -> Show experimental nodes in search`.

Custom nodes:
* [images-grid-comfy-plugin](https://github.com/LEv145/images-grid-comfy-plugin)
* [Impact-Pack](https://github.com/ltdrdata/ComfyUI-Impact-Pack)
* [ComfyUI_essentials](https://github.com/cubiq/ComfyUI_essentials) (optional)

![ImageGrids example](/workflows/ExampleAdv_00b_XYZGridPlot_ImmediateSave.png)

(ComfyUI workflow included)

Technically this node is implemented as a [node expansion](https://docs.comfy.org/custom-nodes/backend/expansion) and uses the default `CheckpointLoaderSimple`, `KSampler`, `VAE Decode` and `Save Image`.

- **TODO** I'm not happy that this node exists at all as I wanted to avoid custom KSampler nodes. Unfortunately I haven't found a way to [use subgraphs to force immediate processing](https://github.com/Comfy-Org/docs/discussions/532#discussioncomment-15115385) yet.

## Baking Values Into Workflow

Custom nodes:
* [Impact-Pack](https://github.com/ltdrdata/ComfyUI-Impact-Pack)
* [Crystools](https://github.com/crystian/ComfyUI-Crystools)

You may have noticed when you load the workflow from one of the grid images it contains the workflow for the whole grid, not the individual image, but sometimes you want to know which exact prompt or values resulted in this image. Thus we need store the individual values in the metadata. The following workflow makes use of Crystools' `Save image with Metadata` and `Load image with Metadata` and Impact-Pack's `Select Nth Item`.

![Save Index in Metadata example](/workflows/ExampleAdv_01a_IndexInMetadata.png)

(ComfyUI workflow included)

Uses the `index` of the combined list to store it as a JSON. It also uses the `index` of the individual lists combined the same way as the prompts, which gives as the rows and columns, for additional information, including the prompt: `{{ "prompt": "{a}", "index": {b}, "row": {c}, "col": {d} }}`

![Load Index from Metadata example](/workflows/ExampleAdv_01b_IndexFromMetadata.png)

(ComfyUI workflow included)

This example reads the index from the metadata with `Load Image with Metadata` and selects the index using `Select Nth Item`.

It's is not perfect because in the end you still have to manually put the image in `Load Image` and hook up the values from `Select Nth Item` to get this one exact image. If you work a lot with image grids you might want to include both of this patterns in one workflow.

- **TODO** This is unsatisfactory and requires a lot of manual work
- **TODO** If someone knows a native way include metadata please let me know (node expansion?, hidden extra pnginfo?, dynprompt?)!

## Load all images from grid

Let's say you generated a lot of images for your grid and (hopefully) stored them with some clever naming scheme, e.g. `cell_{c:02d}-{a}-{b}` like in the previous example. Now you need to load them from the output folder, without accidentally loading any other images. This uses the same prompt combination as before but uses the string to load the image filename. The following workflow makes use of `Load Any File`,

![Load Image with Formatted String](/workflows/ExampleAdv_02_LoadWithFormattedString.png)

(ComfyUI workflow included)

External custom nodes which support image loading via path:
* [was-ns](https://github.com/ltdrdata/was-node-suite-comfyui)/[was-node-suite-comfyui (old)](https://github.com/WASasquatch/was-node-suite-comfyui)
* [VideoHelperSuite](https://github.com/KosinkadinkComfyUI-VideoHelperSuite)
* [ComfyUI-RMBG](https://github.com/1038lab/ComfyUI-RMBG)

## Iterate prompts from PromptManager

Custom nodes:
* [PromptManager](https://github.com/ComfyAssets/ComfyUI_PromptManager)
* [ComfyUI-HTTP](https://github.com/wawahuy/ComfyUI-HTTP)

PromptManager keeps track of all the prompt you generated in a database which you can annotate with tags and categories. The following workflow allows you to search by text, tags and categories to get selection of the prompts and iterate them.

![Load prompts with GET HTTP and extract JSON with JSON OutputList](/workflows/ExampleAdv_03_PromptManager.png)

(ComfyUI workflow included)

Makes use of ComfyUI-HTTP's `HTTP GET Request` to call PromptManager's search API route at `http://127.0.0.1:8188/prompt_manager/search` and `JSON OutputList` to extract the `text` field using a JSONPath. The prompts are emitted as an OutputList and will be processed sequentially.

## XYZ-GridPlots with Videos

![XYZ-GridPlots with Videos example](/workflows/ExampleAdv_04_XYZGridPlot_Videos.png)

(ComfyUI workflow included)

You can ignore the subgraph on the left, it's just used  to create 9 ad-hoc videos of animals with colorful hats rotating. Makes use of `Get Video Components` to split a video into individual frames. The `XYZ-GridPlot` is set to `output_is_list` so we get individual frames of whole grid images. These need to be collected with `Image List to Image Batch` first before creating the video in the `Create Video` node (otherwise it would grid n videos with 1 frame).

https://github.com/user-attachments/assets/efc43311-1052-4832-8486-66b938a5d5f3

## Iterate checkpoints

![Iterate checkpoints example](/workflows/ExampleAdv_05_Checkpoints_ImmediateSave.png)

(ComfyUI workflow included)

The `Load Checkpoint` node suffers from [the same problem](https://github.com/Comfy-Org/docs/discussions/532#discussioncomment-15115385) as the `KSampler` in that it loads ALL checkpoints at once before emitting them which will likely cause OOM. You can workaround this limitation by using the `KSampler Immediate Save` but note that this only works for default `Load Checkpoint -> KSampler -> VAE Decode -> Save Image` pattern, i.e. no `CFGGuider`, no `ModelShift`, no dual samplers etc. If you need them you have to implement your own node expansion or extend [ksampler_immediate_saveimage.py](src/outputlists_combiner/ksampler_immediate_saveimage.py). I know this is unfortunate and probably to difficult for some people (it's not that hard actually, you just have to be careful when connecting node in code).

Another workaround is to use the [PrimitiveInt control\_after\_generate=increment pattern](#the-primitiveint-control_after_generateincrement-pattern) but you will loose the OutputLists abilities.

## Discriminate multiple files

![Iterate checkpoints example](/workflows/ExampleAdv_06_DiscriminateMultipleFiles.png)

(ComfyUI workflow included)

Similar to the basic `Workflow Discriminator` example, but uses a `Load Any File` with a glob pattern expansion to load multiple files, where all files are discriminated against.

## Animating LoRA strength

Custom nodes: [KJNodes](https://github.com/kijai/ComfyUI-KJNodes)

Custom LoRAs: [MoXinV1.safetensors](https://civitai.com/models/12597)

![Animating LoRA strength example](/workflows/ExampleAdv_07_AnimatingLoRAStrength.png)

(ComfyUI workflow included)

Makes use of a `Number OutputList` to iterate over the range `0.0..1.0`. Note that num is `+1` because we to split it into well-formed floatingpoint values and `endpoint=True` to include `1.00` in the values. Also uses `Formatted String` with `{0:0.2f]` and KJNodes's `Add Label` to add the strength information as well-formatted label into the image itself. Note that the images are rebatched into `batch_size=count` because `Create Video` expects batches.


https://github.com/user-attachments/assets/59220dec-bafc-4abc-9294-ae76e3372da8

Also see
* [XYZ-GridPlots with Videos](#xyz-gridplots-with-videos) if you want to compare multiple subjects next to each other in a video
* [Compare LoRA-model and LoRA-strength](#compare-lora-model-and-lora-strength) if you want to compare multiple models with different trigger words

