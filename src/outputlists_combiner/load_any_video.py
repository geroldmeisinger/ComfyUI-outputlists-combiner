import os
import time

import folder_paths
from comfy_api.latest import InputImpl, io

from .util import *


# duplicate of nodes_video.py LoadVideo except it fixes https://github.com/comfyanonymous/ComfyUI/issues/11017
class LoadAnyVideo(io.ComfyNode):
	@classmethod
	def define_schema(cls):
		return io.Schema(
			node_id="LoadAnyVideo",
			search_aliases=["import any video", "open any video", "video any file"],
			display_name="Load Any Video",
			category=CATEGORY,
			inputs=[
				io.String.Input("file"),
			],
			outputs=[
				io.Video.Output(),
			],
		)

	@classmethod
	def execute(cls, file) -> io.NodeOutput:
		video_path = folder_paths.get_annotated_filepath(file)
		return io.NodeOutput(InputImpl.VideoFromFile(video_path))

	@classmethod
	def fingerprint_inputs(s, file):
		if not file: return str(time.time()) # https://github.com/comfyanonymous/ComfyUI/issues/11017

		video_path = folder_paths.get_annotated_filepath(file)
		mod_time = os.path.getmtime(video_path)
		# Instead of hashing the file, we can just use the modification time to avoid
		# rehashing large files.
		return mod_time

	@classmethod
	def validate_inputs(s, file):
		if not file: return True # https://github.com/comfyanonymous/ComfyUI/issues/11017

		if not folder_paths.exists_annotated_filepath(file):
			return "Invalid video file: {}".format(file)

		return True
