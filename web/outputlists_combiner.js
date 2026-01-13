const { applyTextReplacements } = window.comfyAPI.utils
const { app } = window.comfyAPI.app
const { api } = window.comfyAPI.api

app.registerExtension(
{
	name: "OutputListsCombiner",

	async beforeRegisterNodeDef(node)
	{
		if (node.comfyClass === "FormattedString")
		{
			node.prototype.onNodeCreated = function()
			{
				const widget = this.widgets.find(w => w.name === "fstring")
				widget.serializeValue = () => {
					console.log(widget.value)
					const ret = applyTextReplacements(app, widget.value)
					return ret
				}
			}
		}
	},

	async nodeCreated(node)
	{
		if (node.comfyClass === "StringOutputList")
		{
			// add support for inspect_combo
			const inspectSlot = node.outputs.findIndex(o => o.name === "inspect_combo")
			if (inspectSlot === -1) { return }

			node.onConnectionsChange = async function (_, changedOutputId, isConnected, linkInfo)
			{
				if (changedOutputId !== inspectSlot	) { return }
				if (!isConnected	) { return }

				const valuesWidget	= node.widgets.find(w => w.name === "values")
				const separatorWidget	= node.widgets.find(w => w.name === "separator")
				if (!valuesWidget || !separatorWidget) { return }

				app.graph.removeLink(linkInfo.id)

				const targetNode	= app.graph.getNodeById(linkInfo.target_id)
				const targetInputSlot	= targetNode.inputs[linkInfo.target_slot]
				const targetInputName	= targetInputSlot.name
				const targetClassName	= targetNode.comfyClass

				// Auto-connect "value" output to the target input
				const valueOutputIndex	= node.outputs.findIndex(o => o.name === "value")
				node.connect(valueOutputIndex, targetNode, linkInfo.target_slot)

				try
				{
					const info	= await api.fetchApi(`/object_info/${targetClassName}`)
					const json	= await info.json()

					const target	= json[targetClassName].input?.required?.[targetInputName] ?? json[targetClassName].input?.optional?.[targetInputName]
					const values	= target[0] === "COMBO" ? target[1].options : Array.isArray(target[0]) ? target[0] : [target[0]]
					const sep	= separatorWidget.value.replace(/\\n/g, "\n").replace(/\\t/g, "\t") // respect escape sequences

					valuesWidget.value = values.join(sep)
				}
				catch (e)
				{
					console.error("OutputListsCombiner: " + e)
				}
			}
		}

		if (node.comfyClass === "JSONOutputList")
		{
			node.onExecuted = function (ui)
			{
				const jsonWidget = node.widgets.find(w => w.name === "json")
				if (!jsonWidget) { return }
				jsonWidget.value = ui.obj
			}
		}
	},
})
