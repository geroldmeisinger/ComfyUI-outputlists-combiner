# Advanced Examples

## Animating LoRA strength

* Custom nodes: [KJNodes](https://github.com/kijai/ComfyUI-KJNodes) (only to put the label into a image)
* Custom LoRA: [Z-Image Turbo - Realistic Snapshot v5](https://civitai.com/models/2268008/realistic-snapshot-z-image-turbo-krea-2?modelVersionId=2617751)

![Animating LoRA strength example](/workflows/advanced/AnimatingLoRAStrength.png)

(ComfyUI workflow included)

Makes use of a `Number OutputList` to iterate over the range `0.0..1.0`. Note that num is `+1` because we to split it into well-formed floatingpoint values and `endpoint=True` to include `1.00` in the values. Also uses `Format Text` with `{0:0.2f}` and KJNodes's `Add Label` to add the strength information as well-formatted label into the image itself. Note that the images are rebatched into `batch_size=count` because `Create Video` expects batches.

https://github.com/user-attachments/assets/da707caa-6342-40db-9f48-4b8384b55867

Also see
* [XYZ-GridPlots with Videos](#xyz-gridplots-with-videos) if you want to compare multiple subjects next to each other in a video
* [Compare LoRA-model and LoRA-strength](#compare-lora-model-and-lora-strength) if you want to compare multiple models with different trigger words

Old Stable Diffusion 1.5 example:

https://github.com/user-attachments/assets/59220dec-bafc-4abc-9294-ae76e3372da8

* Custom LoRAs: [MoXinV1.safetensors](https://civitai.com/models/12597)

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


## Bake values into workflows

If multiple images are created from an output list, the same workflow is stored for ALL images. This workflows allows to bake the specific string into the workflow JSON for the very string that was used in a individual image.

![Bake String Iterate Loop Nodes before](/workflows/advanced/BakeStringIterateLoopNodes_0.png)

(ComfyUI workflow included)

Makes use of `Bake String` which works as a string passthrough during the workflow phase but on `Save Image` stores the string in `override` field. It's important to use the `Iterate Begin -> worklfow -> Iterate End` pattern here and use the `Bake String` in a passthrough so it gets executed on every iteration, otherwise it will only be execute once (for `cat`) and all images use the same string. The `Bake String` output is hooked on a `OutputLists Combinations` which we exploit as a on-signal node, because it needs to be part of the execution. The actual value is used from `Iterate Begin`, otherwise - when you drag the output image into the workspace - will use the same string for all images. To fix this, see the next example.

When you drag an output image onto the workspace you get the following:

![Bake String Iterate Loop Nodes after](/workflows/advanced/BakeStringIterateLoopNodes_1.png)

(e.g. `dog`, which was on the second iteration)

Here you can see that the string `dog` is baked into the `override` field.

## Bake values into flexible workflows

This workflow lets you use the same workflow to either re-generate the individual image or the original workflow for all images. FOr example when generating a XYZ GridPlot you want know which parameter was used for an individual image but also re-generate the whole grid again.

![Bake String in XYZ GridPlot before](/workflows/advanced/BakeStringXYZGridPlotSupergrids_0.png)

This workflow is an expansion of [bake values into workflows]](#bake-values-into-workflows) and the [XYZ GridPlot](#xyz-gridplot). Makes use of an `Bake String` node for the whole workflow (the outer) and one `Bake String` for the iterated workflow (the inner in `Iterate Begin -> worklfow -> Iterate End`). To check if this workflow is baked or not the outer `Bake String.is_override` is used together with a `If/Else Switch` to either use the original list (not baked) or use only one item (baked), which will be overriden by the sub-sequent inner `Bake String`. Hence, if the workflow is not baked, the list items will be used as is, otherwise the list collapses to one item which gets overriden by the inner string and only executes once. Because the downstream nodes for `XYZ GridPlot` don't make sense for a single item we block further execution with a `Execution Blocker` based on the outer `Bake String.is_override`.

When you drag an individual output image into the workspace you get the following:

![Bake String in XYZ GridPlot after](/workflows/advanced/BakeStringXYZGridPlotSupergrids_1.png)

Here you can see that the string `a dog with a green hat` is baked into the `override` field and when you execute the workflow again it generates the image again of which this individual image was a part of. If you clear the outer and inner `override` strings you can generate the full image grid again.

## Bake images into workflows

This allows to ship input images with the workflow. Useful for img2img or Control-Net workflows.

![Bake String in Load Any File before](/workflows/advanced/BakeStringLoadAnyFile_0.png)

(ComfyUI workflow included)

Makes use of `Load Any File` (1st) to load a image file as a base64 string and `Bake String` to insert this string as the `override` value into the workflow (once the image save in `Save Image`). Another `Load Any File` (2nd) loads the same image (again!) from the base64 string and passes it on to a img2img workflow. Hence, if the file exists, it will be loaded from disk, otherwise the base64 string will be used instead. When you drag the following output image into your workspace:

![Bake String example_baked.png](/tests/imgs/example_baked.png)

(This file has ~600 KiB because the image diffusion introduced a lot of noise which PNG doesn't like. The workflow only increased by about 2x18 KiB due to the base64 input image.)

you should see the following worfklow (note the base64 string in `Bake String`):

![Bake String in Load Any File after](/workflows/advanced/BakeStringLoadAnyFile_1.png)

If you are asking _"Do we really insert a wasteful base64 cleartext version of a binary PNG file into the workflow JSON as a string?"_ the answer is: _"Yes!"_. It's a _image-in-a-JSON-in-a-image_ :) base64 uses up about +33% more space, so it's okay. Here is what it will look like to take the `example.png` resized to 16x16 (374bytes) and encoded as base64 (500bytes) in the workflow json:
```json
"widgets_values": [
	"",
	"iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAIAAACQkWg2AAAAAXNSR0IB2cksfwAAAARnQU1BAACxjwv8YQUAAAAgY0hSTQAAeiYAAICEAAD6AAAAgOgAAHUwAADqYAAAOpgAABdwnLpRPAAAAAlwSFlzAAALEwAACxMBAJqcGAAAAN9JREFUKM+tkjEKgzAUhn+1ToJDF88knqFVqIOi0BMU6R0i7aCgOPQE4pm6dCgoQpB2SKrRilTov+SF9/0vLy+R9uSFNdoAyAMAoHUIQNWIHY+IPACtQ1UjAOwYMlsYRBWraavECXs6ccKmrVjMGEls6XLgObUrWUAVC4Cfmj0ji6f7qal2Jae708Q8Yxgk0G5GlgxuRhjhFsYEZRrdIdndeeHyAYBaW16lMEZjHcoXBgIvvx35Vo8+meuXIfCWXkvIygt0f9T40su1ZwwrJf/SxvTziWKjdPUoeZ7/09Ib1L5LGKJX9wUAAAAASUVORK5CYII=",
	10240,
	true
],
```

You find the original `example_bat.png` in `tests/imgs`.

## Discriminate multiple files

![Iterate checkpoints example](/workflows/advanced/DiscriminateMultipleFiles.png)

(ComfyUI workflow included)

Similar to the basic `Workflow Discriminator` example, but uses a `Load Any File` with a glob pattern expansion to load multiple files, where all files are discriminated against.

## Nested iterate loop nodes

![Nested iterate loop nodes example](/workflows/advanced/NestedIterateLoopNodes.png)

(ComfyUI workflow included)

## Iterate prompts from PromptManager

Custom nodes:
* [PromptManager](https://github.com/ComfyAssets/ComfyUI_PromptManager)
* [ComfyUI-HTTP](https://github.com/wawahuy/ComfyUI-HTTP)

PromptManager keeps track of all the prompt you generated in a database which you can annotate with tags and categories. The following workflow allows you to search by text, tags and categories to get selection of the prompts and iterate them.

![Load prompts with GET HTTP and extract JSON with JSON OutputList](/workflows/advanced/PromptManager.png)

(ComfyUI workflow included)

Makes use of ComfyUI-HTTP's `HTTP GET Request` to call PromptManager's search API route at `http://127.0.0.1:8188/prompt_manager/search` and `JSON OutputList` to extract the `text` field using a JSONPath. The prompts are emitted as an OutputList and will be processed sequentially.
