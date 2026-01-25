import os
import json
import numpy as np
from PIL import Image
from PIL.PngImagePlugin import PngInfo

import folder_paths
from comfy.cli_args import args
from comfy_api.latest import io


class SaveImagePassthrough(io.ComfyNode):
    """
    A Save Image node that also outputs the image, allowing it to be used
    in ForeachList loops where the image needs to flow through to ForeachListEnd.
    
    Unlike the standard Save Image node which has no output, this node passes
    the image through so it can be part of the dependency chain.
    """
    
    @classmethod
    def define_schema(cls) -> io.Schema:
        return io.Schema(
            description="""Saves images to disk AND outputs them for further processing.

This node is designed for use inside ForeachList loops where you need to save each 
intermediate image while still passing it through to ForeachListEnd.

The standard Save Image node has no output, so it can't be part of the loop's 
dependency chain. This node solves that by outputting the same image it saves.

**Usage in ForeachList:**
1. Connect VAE Decode → SaveImagePassthrough → ForeachListEnd (intermediate_output)
2. Each iteration will save the image AND pass it to the loop

The saved images will appear in your ComfyUI output folder.
""",
            node_id="SaveImagePassthrough",
            display_name="Save Image Passthrough",
            category="image",
            inputs=[
                io.Image.Input("images", display_name="images", tooltip="The images to save."),
                io.String.Input("filename_prefix", display_name="filename_prefix", default="ComfyUI", 
                               tooltip="The prefix for the file to save. This may include formatting information such as %date:yyyy-MM-dd% to include values from nodes."),
            ],
            outputs=[
                io.Image.Output("images", display_name="images", tooltip="The same images that were saved (passthrough)."),
            ],
            hidden=[
                io.Prompt.Input("prompt"),
                io.ExtraPngInfo.Input("extra_pnginfo"),
            ],
            is_output_node=True,
        )

    def __init__(self):
        self.output_dir = folder_paths.get_output_directory()
        self.type = "output"
        self.compress_level = 4

    @classmethod
    def execute(cls, images, filename_prefix="ComfyUI", prompt=None, extra_pnginfo=None) -> io.NodeOutput:
        # Get instance attributes via a temporary instance
        output_dir = folder_paths.get_output_directory()
        compress_level = 4
        
        full_output_folder, filename, counter, subfolder, filename_prefix = folder_paths.get_save_image_path(
            filename_prefix, output_dir, images[0].shape[1], images[0].shape[0]
        )
        
        results = []
        for batch_number, image in enumerate(images):
            i = 255. * image.cpu().numpy()
            img = Image.fromarray(np.clip(i, 0, 255).astype(np.uint8))
            
            metadata = None
            if not args.disable_metadata:
                metadata = PngInfo()
                if prompt is not None:
                    metadata.add_text("prompt", json.dumps(prompt))
                if extra_pnginfo is not None:
                    for x in extra_pnginfo:
                        metadata.add_text(x, json.dumps(extra_pnginfo[x]))

            filename_with_batch_num = filename.replace("%batch_num%", str(batch_number))
            file = f"{filename_with_batch_num}_{counter:05}_.png"
            img.save(os.path.join(full_output_folder, file), pnginfo=metadata, compress_level=compress_level)
            results.append({
                "filename": file,
                "subfolder": subfolder,
                "type": "output"
            })
            counter += 1

        # Return both the UI update AND the passthrough image
        return io.NodeOutput(images, ui={"images": results})

