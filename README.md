# genpark-weisfeiler-lehman-graph-isomorphism-skill

Agent Skill implementing the **1-Dimensional Weisfeiler-Lehman (1-WL) Graph Coloring Isomorphism Kernel**, identifying topological equivalence and graph invariants.

## Architectural Overview
```mermaid
flowchart TD
    Graph["Input Graph Adjacency"] --> Degree["Initialize Colors via Degree C_0(v)"]
    Degree --> Multiset["Collect & Sort Neighbor Color Multiset"]
    Multiset --> Hash["Hash: C_{k+1}(v) = Hash(C_k(v), Sorted_Neighbors)"]
    Hash --> Hist["Compute Canonical Color Frequency Histogram"]
    Hist --> Compare["Compare Histograms Across Graphs: Equal -> Isomorphic"]
```
