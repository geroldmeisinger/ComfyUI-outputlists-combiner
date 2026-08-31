# Advanced Examples

## Iterate checkpoints

The `Load Checkpoint` node also suffers from [the execution stalling problem](#the-execution-stalling-problem) in that it loads ALL checkpoints at once before emitting them which will likely cause OOM. You can workaround this limitation by using the `Iterate Begin` and `Iterate End` nodes.

![Iterate checkpoints example](/workflows/advanced/CheckpointsImmediateSave.png)

(ComfyUI workflow included)

Makes use of `Iterate Begin` and `Iterate End` to mark the nodes between the `flow_control` as a "sequential group". This works similar to other loop nodes except that they work with output lists. It's important to use a output node with passthrough to see the intermediate results, otherwise they will only act upon the first item. Newer ComfyUI versions already have them.

## XYZ-GridPlots with Supergrids

I recommend to start ComfyUI with `--cache-ram` for this example if you want to experiment with the settings alot!

![XYZ-GridPlots with Supergrids example](/workflows/advanced/XYZGridPlotSupergrids.png)

(ComfyUI workflow included)

Uses two `XYZ-GridPlot` in sequence to put one image grid inside the other. For more complex image grids the question always is: How should the axis be ordered and in which way the images be shuffled, e.g. do we want to show `cat|dog|rat` x `red|blue|green` and then the batch next to each other in a subgrid (`RxCxB`), or four separate images each with a grid of `cat|dog|rat` x `red|blue|green` (`BxCxR`). To achieve this you can play around with the options `order=outside-in|inside-out` and `output_is_list=False|True`, but make sure the `row_labels` and `col_labels` match what you want to achieve, as this info is also used how the grid is shaped.

## Immediately save intermediate images of image grid

Generating a huge grid like this also suffer from [the execution stalling problem](#the-execution-stalling-problem). You can workaround this limitation by using the `Iterate Begin` and `Iterate End` nodes with an output node passthrough.

![ImageGrids example](/workflows/advanced/XYZGridPlotImmediateSave.png)

(ComfyUI workflow included)

Makes use of `Iterate Begin` and `Iterate End` to mark the nodes between the `flow_control` as a "sequential group". This works similar to other loop nodes except that they work with output lists. It's important to use a output node with passthrough to see the intermediate results, otherwise they will only act upon the first item. Newer ComfyUI versions already have them.

## Load all images from grid

Let's say you generated a lot of images for your grid and (hopefully) stored them with some clever naming scheme, e.g. `cell_{c:02d}-{a}-{b}` like in the previous example. Now you need to load them from the output folder, without accidentally loading any other images. This uses the same prompt combination as before but uses the string to load the image filename. The following workflow makes use of `Load Any File`,

![Load Image with Format Text](/workflows/advanced/LoadWithFormattedString.png)

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

![Load prompts with GET HTTP and extract JSON with JSON OutputList](/workflows/advanced/PromptManager.png)

(ComfyUI workflow included)

Makes use of ComfyUI-HTTP's `HTTP GET Request` to call PromptManager's search API route at `http://127.0.0.1:8188/prompt_manager/search` and `JSON OutputList` to extract the `text` field using a JSONPath. The prompts are emitted as an OutputList and will be processed sequentially.

## Discriminate multiple files

![Iterate checkpoints example](/workflows/advanced/DiscriminateMultipleFiles.png)

(ComfyUI workflow included)

Similar to the basic `Workflow Discriminator` example, but uses a `Load Any File` with a glob pattern expansion to load multiple files, where all files are discriminated against.

## Animating LoRA strength

Custom nodes: [KJNodes](https://github.com/kijai/ComfyUI-KJNodes)
Custom LoRA: [Z-Image Turbo - Realistic Snapshot v5](https://civitai.com/models/2268008/realistic-snapshot-z-image-turbo-krea-2?modelVersionId=2617751)

![Animating LoRA strength example](/workflows/advanced/AnimatingLoRAStrength.png)

(ComfyUI workflow included)

Makes use of a `Number OutputList` to iterate over the range `0.0..1.0`. Note that num is `+1` because we to split it into well-formed floatingpoint values and `endpoint=True` to include `1.00` in the values. Also uses `Format Text` with `{0:0.2f}` and KJNodes's `Add Label` to add the strength information as well-formatted label into the image itself. Note that the images are rebatched into `batch_size=count` because `Create Video` expects batches.

https://github.com/user-attachments/assets/da707caa-6342-40db-9f48-4b8384b55867

Also see
* [XYZ-GridPlots with Videos](#xyz-gridplots-with-videos) if you want to compare multiple subjects next to each other in a video
* [Compare LoRA-model and LoRA-strength](#compare-lora-model-and-lora-strength) if you want to compare multiple models with different trigger words

Old Stable Diffusion 1.5 example:

https://github.com/user-attachments/assets/59220dec-bafc-4abc-9294-ae76e3372da8

Custom LoRAs: [MoXinV1.safetensors](https://civitai.com/models/12597)

## Nested iterate loop nodes

![Nested iterate loop nodes example](/workflows/advanced/NestedIterateLoopNodes.png)

(ComfyUI workflow included)
