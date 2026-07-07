# NCS-OS Compiler: compile_all_modules
# Unified IR generation for all modules (stack, cascade, kernel, topology)

import json
from assemble_stack import assemble_stack
from assemble_cascade import assemble_cascade
from assemble_kernel import assemble_kernel
from assemble_topology import assemble_topology

def load_json(path):
    """Utility loader for JSON files."""
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def compile_all_modules():
    """
    Integrate all module JSON files into a unified IR.
    This is a placeholder skeleton; logic will be added later.
    """

    # Load module JSONs
    layers_json   = load_json("modules/layers.json")
    flows_json    = load_json("modules/flows.json")
    kernel_json   = load_json("modules/kernel.json")
    topology_json = load_json("modules/topology.json")

    # Assemble IR components
    ir = {
        "meta": {
            "version": "1.0",
            "description": "Unified IR for NCS-OS infographic generation",
            "doi": "10.5281/zenodo.21237672"
        },
        "stack":   assemble_stack(layers_json),
        "cascade": assemble_cascade(flows_json),
        "kernel":  assemble_kernel(kernel_json),
        "topology": assemble_topology(topology_json),
        "figures": []
    }

    return ir

if __name__ == "__main__":
    ir = compile_all_modules()
    print(json.dumps(ir, indent=2, ensure_ascii=False))
