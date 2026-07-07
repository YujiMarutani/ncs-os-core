# NCS-OS Compiler: assemble_kernel
# Cognitive Kernel (APIs, Functions, Constraints)

def assemble_kernel(kernel_json):
    """
    Convert kernel.json into IR kernel blocks.
    This is a placeholder skeleton; logic will be added later.
    """

    ir_kernel = {
        "apis": [],
        "functions": [],
        "constraints": []
    }

    kernel = kernel_json.get("kernel", {})

    # APIs
    for api in kernel.get("apis", []):
        ir_kernel["apis"].append({
            "id": api.get("id", ""),
            "name": api.get("name", ""),
            "input": api.get("input", []),
            "output": api.get("output", []),
            "notes": api.get("notes", "")
        })

    # Functions
    for fn in kernel.get("functions", []):
        ir_kernel["functions"].append({
            "id": fn.get("id", ""),
            "name": fn.get("name", ""),
            "description": fn.get("description", ""),
            "notes": fn.get("notes", "")
        })

    # Constraints
    for const in kernel.get("constraints", []):
        ir_kernel["constraints"].append({
            "id": const.get("id", ""),
            "name": const.get("name", ""),
            "description": const.get("description", ""),
            "notes": const.get("notes", "")
        })

    return ir_kernel
