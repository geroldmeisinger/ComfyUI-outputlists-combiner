# For-Loops

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

* [official TensorLoop](https://github.com/kijai/ComfyUI/blob/2bf117a8257a3a1351d7f8db55a9f2ade8870277/comfy_extras/nodes_looping.py)
* [Execution Inversion Demo](https://github.com/BadCafeCode/execution-inversion-demo-comfyui) ([code1](https://github.com/BadCafeCode/execution-inversion-demo-comfyui/blob/main/flow_control.py) [code2](https://github.com/BadCafeCode/execution-inversion-demo-comfyui/blob/main/utility_nodes.py))
* [Easy-Use](https://github.com/yolain/ComfyUI-Easy-Use) ([code](https://github.com/yolain/ComfyUI-Easy-Use/blob/4de1ab3b66e48da916b6f263bacd001df53a2720/py/nodes/logic.py#L591))
* [Inspire-Pack](https://github.com/ltdrdata/ComfyUI-Inspire-Pack) ([Hidden example](https://github.com/ltdrdata/ComfyUI-Impact-Pack/issues/824#issuecomment-2493301831)) ([code](https://github.com/ltdrdata/ComfyUI-Inspire-Pack/blob/d23db9aa544de9a6d4c609cb7005fa9e0d42031d/inspire/list_nodes.py#L82))
* [Control-Flow Utils](https://github.com/VykosX/ControlFlowUtils) ([In-Depth Node Explanation](https://github.com/VykosX/ControlFlowUtils/wiki/ControlFlowUtils-%E2%80%90-In-Depth-Node-Explanation))
* [ThepExcel ComfyAngel](https://github.com/ThepExcel/ComfyAngel) (TODO)
* [Akatz-Loop-Nodes](https://github.com/akatz-ai/Akatz-Loop-Nodes) ([code](https://github.com/akatz-ai/Akatz-Loop-Nodes/blob/main/flow_control.py))
* [Latent Austronaut Suite](https://github.com/latentastronaut/comfyui-latent-astronaut-suite) ([code](https://github.com/latentastronaut/comfyui-latent-astronaut-suite/blob/main/nodes/for_loop.py), [examples](https://github.com/latentastronaut/comfyui-latent-astronaut-suite/tree/main/workflows))
* [PixNodes](https://github.com/pixixai/Comfyui-PixNodes) (chinese, [code](https://github.com/pixixai/Comfyui-PixNodes/tree/main/nodes/Loop))
* [Deforum](https://github.com/deforum/deforum-comfy-nodes)

Not in the registry:
* [WainWong ComfyUI-Loop-image](https://github.com/WainWong/ComfyUI-Loop-image)
* [jeankassio ComfyUI-ForLoops](https://github.com/jeankassio/ComfyUI-ForLoops)

If you are one of these developers and read this, thank you for your work, but please fix your documentation and examples!

**Non-loops**

The following packages have loop in there name but don't provide actual looping functionality in the sense described above:

* [Bjornulf_custom_nodes](https://github.com/justUmen/Bjornulf_custom_nodes) just data lists
* [Hullabalo/ComfyUI-Loop](https://github.com/Hullabalo/ComfyUI-Loop) multi-run blackmagic
* [O-oshir/comfy-loop-utilities](https://github.com/O-oshir/comfy-loop-utilities) just data lists
* [t22m003/ComfyUI_LoopNode](https://github.com/t22m003/ComfyUI_LoopNode) just data lists
* multiple looped sampler implementations which only work for one use-case
