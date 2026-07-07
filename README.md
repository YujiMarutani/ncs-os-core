## Infographic Rendering Pipeline

All NCS‑OS figures in the manuscript are generated via a deterministic, JSON‑driven pipeline:

1. **JSON Modules** (`modules/`)  
   Sovereignty layers, cascades, kernel logic, topology, and style are defined as modular JSON.

2. **Compiler** (`compiler/`)  
   The modules are merged into a unified Infographic Intermediate Representation (IR).

3. **Renderer** (`renderer/`)  
   The IR is converted into SVG diagrams and exported as PNG for manuscript inclusion.

4. **Manuscript Integration** (`manuscript/`)  
   All figures are automatically embedded into the LaTeX manuscript.

For full technical details, see:

- `specification/infographic-standard.md`
