# NCS-OS Renderer: apply_style
# Apply style.json (colors, fonts, layout, signature) to IR

def apply_style(ir, style_json):
    """
    Apply style specification to IR.
    This is a placeholder skeleton; logic will be added later.
    """

    styled_ir = {
        "meta": ir.get("meta", {}),
        "stack": ir.get("stack", []),
        "cascade": ir.get("cascade", {}),
        "kernel": ir.get("kernel", {}),
        "topology": ir.get("topology", {}),
        "style": {
            "colors": style_json.get("colors", {}),
            "fonts": style_json.get("fonts", {}),
            "layout": style_json.get("layout", {}),
            "signature": style_json.get("signature", {})
        }
    }

    return styled_ir
