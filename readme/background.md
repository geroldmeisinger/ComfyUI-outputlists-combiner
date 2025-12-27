# Background

Did you know that ComfyUI supports so called output lists which tell nodes downstream to execute multiple times within the same run? Notice how this output list emits four strings and causes the KSampler to run four times:

https://github.com/user-attachments/assets/303115d3-7c28-42e8-bb52-d02e7cc1022b

*Wait, what?*

Yeah, I didn't know about it either. Apparently everytime you see the symbol `𝌠` it's an [output list](https://docs.comfy.org/custom-nodes/backend/lists). This feature is very underutilized but it allows you to be process sequentially without weird workarounds (like for-loops, increment counters or external python scripts) and makes it perfect for prompt combinations and XYZ-gridplots. I always found grids a hazzle in ComfyUI whereas they were straightforward in Automatic1111. Most custom nodes either require a lot of manual work or you have to use some extra-special nodes (like custom KSamplers). This project tries to make good use of output lists, integrate well with the ComfyUI's paradigm and finally make XYZ-gridplots easy to use again.

**Make sure you understand what's happening in this example as it's crucial to work with the following nodes!**

