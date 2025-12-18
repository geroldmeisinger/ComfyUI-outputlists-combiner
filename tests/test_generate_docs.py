# #!/usr/bin/env python

import os
import sys
from pathlib import Path

repo_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, repo_dir)

from src.outputlists_combiner import *


def generate_table(rows):
	if not rows: return []

	lines = [
		"| Name\t| Type\t| Description\t|",
		"| ---\t| ---\t| ---\t|",
	]

	for name, type, tooltip in rows:
		tooltip = tooltip.replace("\n", " ").strip() if tooltip else ""
		lines.append(f"| `{name}`\t| `{type}`\t| {tooltip}\t|")

	lines.append("")
	return lines

def test_generate_docs():
	nodes = [
		StringOutputList(),
		NumberOutputList(),
		JSONOutputList(),
		SpreadsheetOutputList(),
		CombineOutputLists(),
		XyzGridPlot(),
		FormattedString(),
		ConvertNumberToIntFloatStr(),
		LoadAnyFile(),
		#KSamplerImmediateSave(),
	]

	toc_lines	= ["- [Nodes](#nodes)"]
	nodes_lines = []
	for node in nodes:
		schema	= node.define_schema()
		node_name	= schema.display_name or schema.node_id

		toc_lines.append(f"\t[{node_name}](#{schema.node_id})")

		nodes_lines.append(f"## {node_name}\n")
		#md_lines.append("### Description\n")
		nodes_lines.append(f"![{node_name}](/media/{schema.node_id}.png)\n\n(workflow included)\n")
		nodes_lines.append((schema.description or "").strip())

		# Inputs
		nodes_lines.append("### Inputs\n")
		input_rows = []
		for input in schema.inputs or []:
			type	= "COMBO" if input.io_type.startswith("[") else input.io_type
			tooltip	= getattr(input, "tooltip", "").replace(INPUTLIST_NOTE, "").strip()
			input_rows.append((input.display_name or input.id, type, tooltip))
		nodes_lines.extend(generate_table(input_rows))

		# Outputs
		nodes_lines.append("### Outputs\n")
		output_rows = []
		for out in schema.outputs or []:
			type	= "COMBO" if isinstance(out.io_type, list) else out.io_type
			tooltip	= getattr(out, "tooltip", "").replace(OUTPUTLIST_NOTE, "").strip()
			output_rows.append((out.display_name or out.id, type, tooltip))
		nodes_lines.extend(generate_table(output_rows))

	# Ensure output directory exists
	#output_path.parent.mkdir(parents=True, exist_ok=True)

	# Write markdown file
	header	= "<!--- Auto-generated from src_README.md! Don't edit this file! Edit src_README.md instead! -->"
	toc_text	= "\n".join(toc_lines)
	nodes_text = "\n".join(nodes_lines)
	print(nodes_text)
	readme_src	= Path(f"{repo_dir}/src_README.md").read_text()
	readme	= readme_src.replace("{HEADER}", header).replace('- [Nodes](#nodes)', toc_text).replace('{NODES}', nodes_text)
	Path(f"{repo_dir}/README.md").write_text(readme, encoding="utf-8")
