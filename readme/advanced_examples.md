# Advanced Examples

## The execution stalling problem

One thing you may have noticed when you make a large image grid is that you have to wait for ALL intermediate images to be processed before anything is saved and the grid created. Thus you could loose a lot of processed images when something happens or you cancel the job (though ComfyUI keeps them in cache and should pick up immediately). Another problem that occurs with loader nodes is that the load ALL resources at once before passing on execution which will eventually lead to OOM.

I have filled a [RFC](https://github.com/Comfy-Org/rfcs/discussions/43) specifically for this problem and proposed changes to the execution scheme of ComfyUI. In the meantime there are multiple workarounds:
* Ignore it and just wait it out (I recommend to start ComfyUI with `--cache-ram` though, so you can pick up were you left off anytime)
* Use the `KSampler immediate Save Image` BETA node if your workflow just uses the standard `CheckpointLoaderSimple -> KSampler -> VAE Decode -> Save Image` pattern (see [below](#immediately-save-intermediate-images-of-image-grid)).
* Use the [PrimitiveInt control\_after\_generate=increment pattern](#the-primitiveint-control_after_generateincrement-pattern) to cancel out the effect of outputlists
* Use [for-loops](#for-loops) with passthrough nodes (see below)

## XYZ-GridPlots with Supergrids

I recommend to start ComfyUI with `--cache-ram` for this example if you want to experiment with the settings alot!

![XYZ-GridPlots with Supergrids example](/workflows/ExampleAdv_00a_XYZGridPlot_Supergrids.png)

(ComfyUI workflow included)

Uses two `XYZ-GridPlot` in sequence to put one image grid inside the other. For more complex image grids the question always is: How should the axis be ordered and in which way the images be shuffled, e.g. do we want to show `cat|dog|rat` x `red|blue|green` and then the batch next to each other in a subgrid (`RxCxB`), or four separate images each with a grid of `cat|dog|rat` x `red|blue|green` (`BxCxR`). To achieve this you can play around with the options `order=outside-in|inside-out` and `output_is_list=False|True`, but make sure the `row_labels` and `col_labels` match what you want to achieve, as this info is also used how the grid is shaped.

## Immediately save intermediate images of image grid

If you want to save the intermediate images after each step you can use the `KSampler immediate Save Image` beta-node. For this node to be visible in the node searchbox you need to activate `Settings -> Comfy -> Show experimental nodes in search`.

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

The `Load Checkpoint` node also suffers from [the execution stalling problem](#the-execution-stalling-problem) in that it loads ALL checkpoints at once before emitting them which will likely cause OOM. You can workaround this limitation by using the `KSampler Immediate Save` but note that this only works for default `Load Checkpoint -> KSampler -> VAE Decode -> Save Image` pattern, i.e. no `CFGGuider`, no `ModelShift`, no dual samplers etc. If you need them you have to implement your own node expansion or extend [ksampler_immediate_saveimage.py](src/outputlists_combiner/ksampler_immediate_saveimage.py). I know this is unfortunate and probably to difficult for some people (it's not that hard actually, you just have to be careful when connecting node in code).

Another workaround is to use the [PrimitiveInt control\_after\_generate=increment pattern](#the-primitiveint-control_after_generateincrement-pattern) but you will loose the OutputLists abilities.

Another workaround is to use [for-loops](#for-loops).

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

## For-Loops

**DISCLAIMER: The following example is in no way intended to glorify the use of for-loops in ComfyUI or any other forms of violence. In no event can the copyright holder be held liable to damages to your brain or mental functions. No one knows how for-loops actually work in ComfyUI and I do in no way claim to posses this wisdom either.**

**Only use this if you are effected by the [execution stalling problem](#the-execution-stalling-problem)!**

Custom nodes:
* [Easy-Use](https://github.com/yolain/ComfyUI-Easy-Use)
* [basic data handling](https://github.com/StableLlama/ComfyUI-basic_data_handling)
* (optional) [Inspire-Pack](https://github.com/ltdrdata/ComfyUI-Inspire-Pack) for `Preview Image Bridge`
* (optional) [was-ns](https://github.com/ltdrdata/was-node-suite-comfyui)/[was-node-suite-comfyui (old)](https://github.com/WASasquatch/was-node-suite-comfyui) for `Image Save Passthrough`

**For-Loop over images**

![For-Loop images example](/workflows/ExampleAdv_08a_ForLoops_Images.png)

(ComfyUI workflow included)

This workflow makes use of Easy-Use's `For Loop Start`+`For Loop End` and `Index Any` and basic-data-handling's `create LIST`, `append (LIST)` and `convert to Data List` to iterate over an outputlist and map the results to a new outputlist, while executing all the sub-nodes within the for-loop for each item. Note that Easy-Use's `For Loop` is rather intended as a feedback cycle and as such more complicated then it needs to be for this simple value transformation and mapping. What happens here is that we use the outputlists `count` as the number of cycles, and start with an empty list as the accumlator. The for-loop index is used to access the item in the list, then generates the corresponding and appends it to the list. In the next cycle the list (with one image) is fed back to the start and then generates the next image and appends. In order for an output node (`Preview Image`, `Save Image` etc.) to be considered part of the node expansion it needs a "passthrough". You can either use Inspire-Pack's `Preview Image Bridge` or WAS's `Image Save Passthrough`.

**For-Loop over checkpoints**

![For-Loop checkpoints example](/workflows/ExampleAdv_08b_ForLoops_Checkpoints.png)

(ComfyUI workflow included)

The same as above except we are iterate over SDXL checkpoints instead of strings. This workflow loads the checkpoints one-by-one and unloads them after usage.

Note: You have to start with `--cache-none` for this to work. I tried [Unload Models](https://github.com/SeanScripts/ComfyUI-Unload-Model) and [Purge VRAM V2](https://github.com/chflame163/ComfyUI_LayerStyle) but they didn't work with default cache setting.

**Background**

In August 2024 ComfyUI introduced [execution inversion](https://github.com/comfyanonymous/ComfyUI/pull/2666) which changed how nodes are processed. Read the [Execution Model Announcement](https://blog.comfy.org/p/august-2024-flux-support-new-frontend-for-loops-and-more?open=false#%C2%A7pr-2666-execution-inversion) and the [Execution Model Inversion Guide](https://docs.comfy.org/development/comfyui-server/execution_model_inversion_guide).

Confused? Good, because you are in good company. It's another example of sophisticated engineering wasted due to lack of any useful documentation. Anyway, one point of this feature is that it enables [Node Expansion](https://docs.comfy.org/custom-nodes/backend/expansion). You can think of it as a custom node which automatically copy-pastes and links other nodes in the background. If done the right way - by inspecting the node graph and the dependencies during runtime using `dynprompt` and copy-pasting the nodes in between multiple times - this gives rise to looping functionality (see code [here](https://github.com/BadCafeCode/execution-inversion-demo-comfyui/blob/main/flow_control.py)). Many other custom node packs implement different variants of looping, but again - in a cycle of elitism - lack any useful documentation and examples, hence why they are not used anywhere. Which brings me to the conclusion that no one (NO ONE!) knows how for-loops in ComfyUI actually work and they are merely a cruel inside joke to mess with everyone.

Also note that most loop nodes want to support some form of feedback cycle and use the previous result as the input for the next cycle (e.g. a img2img loop). As such the nodes within the loop always need an input image, but because the first output image hasn't been generated yet, they need an initial value independent of the generation. In programming terms you could compare that to a `reduce` (or Arrow Loop) as opposed to a `map` (or Functor).

**Alternative loop variants**

* [Easy-Use](https://github.com/yolain/ComfyUI-Easy-Use)
* [Inspire-Pack](https://github.com/ltdrdata/ComfyUI-Inspire-Pack) ([Hidden example](https://github.com/ltdrdata/ComfyUI-Impact-Pack/issues/824#issuecomment-2493301831))
* [Control-Flow Utils](https://github.com/VykosX/ControlFlowUtils) ([In-Depth Node Explanation](https://github.com/VykosX/ControlFlowUtils/wiki/ControlFlowUtils-%E2%80%90-In-Depth-Node-Explanation))
* [Akatz-Loop-Nodes](https://github.com/akatz-ai/Akatz-Loop-Nodes)
* [Execution Inversion Demo](https://github.com/BadCafeCode/execution-inversion-demo-comfyui)

If you are one of these developers and read this, thank you for your work, but please fix your documentation and examples!
