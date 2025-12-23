import base64
import hashlib
import time
from io import BytesIO
from json import dumps

import chardet
import folder_paths
import node_helpers
import numpy as np
import torch
from comfy_api.latest import io
from exiftool import ExifToolHelper
from PIL import Image, ImageOps, ImageSequence, UnidentifiedImageError


class LoadAnyFile(io.ComfyNode):
	@classmethod
	def define_schema(cls) -> io.Schema:
		ret = io.Schema(
			description	= """Load any text or binary file and provide the file content as string or base64 string and additionally try to load it as a `IMAGE`.
""",
			node_id     	= "LoadAnyFile",
			display_name	= "Load Any File",
			category    	= "Utility",
			inputs      	= [
				io.String.Input("annotated_filepath", display_name="filepath"	,  tooltip="Base directory defaults to input directory. Use suffix `[input]` `[output]` or `[temp]` to specify a different ComfyUI user directory."),
			],
			outputs	= [
				io.String	.Output("string"  	, display_name="string"  	, is_output_list=True, tooltip="File content for text files, base64 for binary files."),
				io.Image 	.Output("image"   	, display_name="image"   	, is_output_list=True, tooltip="Image batch tensor."),
				io.Mask  	.Output("mask"    	, display_name="mask"    	, is_output_list=True, tooltip="Mask batch tensor."),
				io.String	.Output("metadata"	, display_name="metadata"	, is_output_list=True, tooltip="Exif data from ExifTool. Requires `exiftool` command to be available in `PATH`."),
			],
		)
		return ret

	@classmethod
	def execute(cls, annotated_filepath: str) -> io.NodeOutput:
		# https://github.com/comfyanonymous/ComfyUI/issues/11017
		if not annotated_filepath:
			ret = io.NodeOutput([], [], [], [])
			return ret

		# input_dir = folder_paths.get_input_directory()
		# files = [f for f in os.listdir(input_dir) if os.path.isfile(os.path.join(input_dir, f))]
		# files = folder_paths.filter_files_content_types(files, ["image"])
		# return {"required":
		#             {"image": (sorted(files), {"image_upload": True})},
		#         }

		file_path = folder_paths.get_annotated_filepath(annotated_filepath)

		with open(file_path, "rb") as f:
			raw_data = f.read()

		# check if binary
		try:
			result  	= chardet.detect(raw_data[:1024]) # trunc for performance
			encoding	= result["encoding"]
			if encoding:
				filecontent = raw_data.decode(encoding)
			else:
				filecontent = None
		except (UnicodeDecodeError, TypeError):
			filecontent = None

		# check if base64
		if filecontent is not None:
			try:
				_ = base64.b64decode(filecontent, validate=True)
				is_binary = False
			except (base64.binascii.Error, ValueError):
				is_binary = True
		else:
			is_binary = True

		# get file content as text or base64
		if is_binary or filecontent is None:
			filecontent = base64.b64encode(raw_data).decode("utf-8")
			image_data = raw_data
		else:
			image_data = filecontent.encode("utf-8")

		# try to load binary or base64 as image
		exif_json = ""
		try:
			pil_img	= node_helpers.pillow(Image.open, BytesIO(image_data))
			image, mask = load_image(pil_img)

			# get info from standard PNG otherwise fall back to exiftool
			if hasattr(pil_img, "info") and pil_img.info and not "exif" in pil_img.info:
				exif_json = dumps(pil_img.info, indent=4)
		except (UnidentifiedImageError, OSError, ValueError):
			# fallback to black 64x64 tensors
			image	= torch.zeros((64, 64), dtype=torch.float32, device="cpu")
			mask 	= torch.zeros((64, 64), dtype=torch.float32, device="cpu")

		# run exiftool
		if not exif_json and is_binary:
			try:
				with ExifToolHelper() as et:
					exif = et.get_metadata(file_path)[0]
					exif_json = dumps(exif, indent=4)
			except FileNotFoundError: # exiftool not found in path
				pass

		ret = io.NodeOutput([filecontent], [image], [mask], [exif_json or "{}"])
		return ret

	@classmethod
	def fingerprint_inputs(cls, annotated_filepath: str) -> str:
		if not annotated_filepath: return str(time.time()) # https://github.com/comfyanonymous/ComfyUI/issues/11017
		path	= folder_paths.get_annotated_filepath(annotated_filepath)
		m   	= hashlib.sha256()
		with open(path, 'rb') as f:
			m.update(f.read())
		ret = m.digest().hex()
		return ret

	@classmethod
	def validate_inputs(cls, annotated_filepath: str) -> bool | str:
		if not annotated_filepath: return True # https://github.com/comfyanonymous/ComfyUI/issues/11017
		path = folder_paths.get_annotated_filepath(annotated_filepath)
		if not folder_paths.exists_annotated_filepath(path):
			return "Invalid file: {}".format(path)

		return True

# from ComfyUI/nodes.py LoadImage
def load_image(img: Image) -> tuple[torch.tensor, torch.tensor]:
	output_images	= []
	output_masks 	= []
	w, h         	= None, None

	excluded_formats = ['MPO']

	for i in ImageSequence.Iterator(img):
		i = node_helpers.pillow(ImageOps.exif_transpose, i)

		if i.mode == 'I':
			i = i.point(lambda i: i * (1 / 255))
		image = i.convert("RGB")

		if len(output_images) == 0:
			w = image.size[0]
			h = image.size[1]

		if image.size[0] != w or image.size[1] != h:
			continue

		image = np.array(image).astype(np.float32) / 255.0
		image = torch.from_numpy(image)[None,]
		if 'A' in i.getbands():
			mask = np.array(i.getchannel('A')).astype(np.float32) / 255.0
			mask = 1. - torch.from_numpy(mask)
		elif i.mode == 'P' and 'transparency' in i.info:
			mask = np.array(i.convert('RGBA').getchannel('A')).astype(np.float32) / 255.0
			mask = 1. - torch.from_numpy(mask)
		else:
			mask = torch.zeros((64,64), dtype=torch.float32, device="cpu")
		output_images	.append(image)
		output_masks 	.append(mask.unsqueeze(0))

	if len(output_images) > 1 and img.format not in excluded_formats:
		output_image	= torch.cat(output_images	, dim=0)
		output_mask 	= torch.cat(output_masks 	, dim=0)
	else:
		output_image	= output_images[0]
		output_mask 	= output_masks[0]

	return (output_image, output_mask)