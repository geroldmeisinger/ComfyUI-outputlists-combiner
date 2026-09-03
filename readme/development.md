# Development

## This node pack

* Node interface design: the core feature of OutputLists Combiner revolves around [data lists](https://docs.comfy.org/custom-nodes/backend/lists). One of my design goals is to introduce new custom nodes only if they are necessary in the most common use-cases and avoid cluttering with more duplicate functionality that is already available in other essential nodes, see [third-party nodes](#third-party-custom-nodes).
* Research: I try to research the ecosystem and honor existing solutions first before implementing something new.
* Tutorials: I try to provide documentation and examples for every node and use-case, because I hate that in other nodes packs. If you find anything to be unclear, please let me know!
* Documentation: is generated from /readme via a pytest `test_generate_docs.py` (it's akward, I know, but I get the ComfyUI API in code this way).
* Debugging: launch ComfyUI via [vscode launch](/.vscode/launch.json) and then just set breakpoints in code.
* Code style: I use [Elastic Tabstops Redux for vscode](https://marketplace.visualstudio.com/items?itemName=gerold-meisinger.elastic-tabstops-lite-redux).

## Tools

* To export workflow images I use [Workflow-Image-Export](https://github.com/nomadoor/ComfyUI-Workflow-Image-Export) which has many useful options like transparent background and cropping, but doesn't always work [on some output nodes](https://github.com/nomadoor/ComfyUI-Workflow-Image-Export/issues).
* I used to use pythongosssss' custom script [export worfklow image](https://github.com/pythongosssss/ComfyUI-Custom-Scripts) with [a specialized theme](/docs/dark_exportworkflow.json) that has a transparent background image, but has some other quirks.
* [workflow extract script](/docs/workflow_extract.nemo_action) to get the workflow JSON out of a image (my [feature request](https://github.com/Comfy-Org/comfy-cli/issues/341) to get this function Comfy CLI was declined).
* [workflow reinsert script](workflow_reinsert.nemo_action) to get the workflow JSON back into a image after I have made changes to it (cropping, annotations, adding outputs manually).
* For translation I use [md-translator](https://github.com/rockbenben/md-translator) any Qwen 9B (supports [most languages](/docs/qwen3_languages.csv) as of 2025) via [Unsloth Studio](https://unsloth.ai)

## Custom node development

* [official docs](https://docs.comfy.org/custom-nodes/intro)
  * [data types](https://docs.comfy.org/custom-nodes/backend/datatypes)
  * [data list](https://docs.comfy.org/custom-nodes/backend/lists)
  * [Schema v3](https://docs.comfy.org/custom-nodes/v3_migration)
  * [node expansion](https://docs.comfy.org/custom-nodes/backend/expansion)
* [chrisgoringe - Comfy Custom Node How-To](https://github.com/chrisgoringe/Comfy-Custom-Node-How-To/wiki)
* [Suzie1 ComfyUI - Guide To Making Custom Nodes](https://github.com/Suzie1/ComfyUI_Guide_To_Making_Custom_Nodes/wiki)
* and inspecting other third-party nodes
