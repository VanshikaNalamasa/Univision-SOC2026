# Week 5 — Graph Validation Checklist

1. Every block has at least one input OR one output (not neither)
2. No block connects to itself
3. Output type must match input type of the connected block
4. No cycles exist in the graph (it must be a DAG)
5. All required config fields are filled
6. No orphan blocks (every block is reachable from the start)
7. There is exactly one start block (no input ports)
8. There is at least one end block (no output ports)
9. Topological sort must succeed before execution begins
10. Invalid connections are rejected with a clear error message