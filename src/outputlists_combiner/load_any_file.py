import base64
import hashlib
from io import BytesIO

import chardet
import folder_paths
import node_helpers
import numpy as np
import torch
from comfy_api.latest import io
from PIL import Image, ImageOps, ImageSequence, UnidentifiedImageError


class LoadAnyFile(io.ComfyNode):
	@classmethod
	def define_schema(cls) -> io.Schema:
		ret = io.Schema(
			description	= """Load any text or binary file and provide the file content as string or base64 string and additionally try to load it as a `IMAGE`.
""",
			node_id	= "LoadAnyFile",
			display_name	= "Load Any File",
			category	= "Utility",
			inputs	= [
				io.String.Input("annotated_filepath", tooltip="Base directory defaults to input directory. Use suffix `[input]` `[output]` or `[temp]` to specify a different ComfyUI user directory."),
			],
			outputs	= [
				io.String	.Output("string"	, display_name="string"	, is_output_list=False, tooltip="File content for text files, base64 for binary files."),
				io.Image	.Output("image"	, display_name="image"	, is_output_list=False, tooltip="Image batch tensor."),
				io.Mask	.Output("mask"	, display_name="mask"	, is_output_list=False, tooltip="Mask batch tensor."),
			],
		)
		return ret

	@classmethod
	def load_image(self, image_data: str | BytesIO) -> tuple[torch.tensor, torch.tensor]:
		img = node_helpers.pillow(Image.open, image_data)

		# from ComfyUI/nodes.py LoadImage
		output_images	= []
		output_masks	= []
		w, h	= None, None

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
			output_masks	.append(mask.unsqueeze(0))

		if len(output_images) > 1 and img.format not in excluded_formats:
			output_image	= torch.cat(output_images	, dim=0)
			output_mask	= torch.cat(output_masks	, dim=0)
		else:
			output_image	= output_images[0]
			output_mask	= output_masks[0]

		return (output_image, output_mask)

	@classmethod
	def execute(self, annotated_filepath: str) -> io.NodeOutput:
		file_path = folder_paths.get_annotated_filepath(annotated_filepath)

		with open(file_path, "rb") as f:
			raw_data = f.read()

		# check if binary
		try:
			result	= chardet.detect(raw_data)
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
		try:
			image, mask = self.load_image(BytesIO(image_data))
		except (UnidentifiedImageError, OSError, ValueError):
			# fallback to black 64x64 tensors
			image	= torch.zeros((64, 64), dtype=torch.float32, device="cpu")
			mask	= torch.zeros((64, 64), dtype=torch.float32, device="cpu")

		ret = io.NodeOutput(filecontent, image, mask)
		return ret

	@classmethod
	def fingerprint_inputs(cls, annotated_filepath: str) -> str:
		path	= folder_paths.get_annotated_filepath(annotated_filepath)
		m	= hashlib.sha256()
		with open(path, 'rb') as f:
			m.update(f.read())
		ret = m.digest().hex()
		return ret

	@classmethod
	def validate_inputs(cls, annotated_filepath: str) -> bool | str:
		path = folder_paths.get_annotated_filepath(annotated_filepath)
		if not folder_paths.exists_annotated_filepath(path):
			return "Invalid file: {}".format(path)

		return True
