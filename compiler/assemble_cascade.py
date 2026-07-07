# NCS-OS Compiler: assemble_cascade
# Sovereignty Cascades (Bottom-Up and Top-Down)

def assemble_cascade(flows_json):
    """
    Convert flows.json into IR cascade blocks.
    This is a placeholder skeleton; logic will be added later.
    """

    ir_cascade = {
        "bottom_up": [],
        "top_down": []
    }

    # Bottom-Up Cascade
    for flow in flows_json.get("bottom_up", []):
        ir_cascade["bottom_up"].append({
            "from": flow["from"],
            "to": flow["to"],
            "type": flow.get("type", ""),
            "description": flow.get("description", ""),
            "notes": flow.get("notes", "")
        })

    # Top-Down Cascade
    for flow in flows_json.get("top_down", []):
        ir_cascade["top_down"].append({
            "from": flow["from"],
            "to": flow["to"],
            "type": flow.get("type", ""),
            "description": flow.get("description", ""),
            "notes": flow.get("notes", "")
        })

    return ir_cascade
