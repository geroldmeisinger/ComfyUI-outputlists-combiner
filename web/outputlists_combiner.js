import { api } from "../../scripts/api.js"
import { app } from "../../scripts/app.js"

app.registerExtension(
{
	name: "OutputListsCombiner",

	async nodeCreated(node)
	{
		if (node.comfyClass !== "StringOutputList") return

		const inspectSlot = node.outputs.findIndex(o => o.name === "inspect_combo")
		if (inspectSlot === -1) return

		node.onConnectionsChange = async function (_, changedOutputId, isConnected, linkInfo)
		{
			if (changedOutputId !== inspectSlot) { return }

			const textWidget = node.widgets.find(w => w.name === "values")
			if (!textWidget) { return }

			if (!isConnected) { return }

			app.graph.removeLink(linkInfo.id)
			app.graph.setDirtyCanvas(true, true)

			const targetNode	= app.graph.getNodeById(linkInfo.target_id)
			const targetInputName	= targetNode.inputs[linkInfo.target_slot].name
			const className	= targetNode.comfyClass

			try
			{
				const info	= await api.fetchApi(`/object_info/${className}`)
				const json	= await info.json()

				const target	= json[className].input.required[targetInputName]
				const allowed	= Array.isArray(target[0]) ? target[0]	: [target[0]]

				textWidget.value = allowed.join("\n")
			}
			catch (e)
			{
				textWidget.value = "Error fetching info: " + e
			}
		}
	}
})
