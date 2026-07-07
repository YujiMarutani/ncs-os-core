# NCS-OS Compiler: assemble_stack
# Structural integration of Sovereignty Layers (L0-L4)

def assemble_stack(layers_json):
    """
    Convert layers.json into IR layer blocks.
    This is a placeholder skeleton; logic will be added later.
    """
    ir_layers = []

    for layer in layers_json.get("layers", []):
        ir_layers.append({
            "id": layer["id"],
            "name": layer["name"],
            "components": layer.get("components", []),
            "notes": layer.get("notes", "")
        })

    return ir_layers
