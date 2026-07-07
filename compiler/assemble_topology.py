# NCS-OS Compiler: assemble_topology
# Structural Topology (Layer geometry, nodes, edges, domains)

def assemble_topology(topology_json):
    """
    Convert topology.json into IR topology blocks.
    This is a placeholder skeleton; logic will be added later.
    """

    ir_topology = {
        "layers": [],
        "edges": [],
        "domains": []
    }

    # Layers
    for layer in topology_json.get("layers", []):
        ir_topology["layers"].append({
            "id": layer.get("id", ""),
            "geometry": layer.get("geometry", ""),
            "nodes": layer.get("nodes", []),
            "notes": layer.get("notes", "")
        })

    # Edges
    for edge in topology_json.get("edges", []):
        ir_topology["edges"].append({
            "from": edge.get("from", ""),
            "to": edge.get("to", ""),
            "type": edge.get("type", ""),
            "description": edge.get("description", ""),
            "notes": edge.get("notes", "")
        })

    # Domains
    for domain in topology_json.get("domains", []):
        ir_topology["domains"].append({
            "id": domain.get("id", ""),
            "layers": domain.get("layers", []),
            "description": domain.get("description", ""),
            "notes": domain.get("notes", "")
        })

    return ir_topology
