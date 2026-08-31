from comfy_api.latest import io

from .util import *

wormholes = {}

class WormholeGet(io.ComfyNode):
	@classmethod
	def define_schema(cls) -> io.Schema:
		ret = io.Schema(
			description	= "Wormhole Get",
			node_id	= "WormholeGet",
			display_name	= "Wormhole GET",
			category	= CATEGORY,
			inputs	= [
				io.AnyType	.Input("signal"	, display_name="signal", tooltip=""),
				io.String	.Input("name"	, display_name="name"	, tooltip=""),
				io.AnyType	.Input("init"	, display_name="init"	, tooltip="")
			],
			outputs=[
				io.AnyType.Output("value", display_name="value", tooltip=""),
			],
		)
		return ret

	@classmethod
	def execute(cls, signal: any, name: str, init: any) -> io.NodeOutput:
		global wormholes
		ret = wormholes.get(name, init)
		return io.NodeOutput(ret)

class WormholeSet(io.ComfyNode):
	@classmethod
	def define_schema(cls) -> io.Schema:
		ret = io.Schema(
			description	= "Wormhole Set",
			node_id	= "WormholeSet",
			display_name	= "Wormhole SET",
			category	= CATEGORY,
			inputs	= [
				io.String	.Input("name"	, display_name="name"	, tooltip=""),
				io.AnyType	.Input("value"	, display_name="value"	, tooltip="")
			],
			outputs=[
				io.AnyType.Output("value", display_name="value", tooltip=""),
			],
		)
		return ret

	@classmethod
	def execute(cls, name: str, value: any) -> io.NodeOutput:
		global wormholes
		wormholes[name] = value
		return io.NodeOutput(value)
