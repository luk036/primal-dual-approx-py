# ☯ Primal-dual approximation algorithms

## Key points

- Ref: Goemans and Williamson
- For large scale **weighted** problems.
- Optimal solution is not required.
  - e.g. subproblem of a complex problem
- Demand a quick solution
  - e.g. bipartite matching problem
    - Polynomial-time solvable, but 
    - Network flow algorithm requires O(N⋅M) 
- Dual problem is "easier" to **solve** 
  - e.g. without sorting
  - counter-example: facility location problems
- Extensible for hypergraph versions.
- Often give you a performance ratio as a bonus.
- Often give you a lower bound as a bonus.

## Examples

- Vertex Cover

- Clustering in multi-level circuit partitioning
    - minimum weighted maximal matching

- Double patterning complement with E-beam
    - graph bipartization
    - minimum odd-cycle cover problem

- Dobule patterning wiht DSA (directed self-assembly)
    - Set-cover problem:

       o     o o    o     o
       o     o o    o       o
                    o

- Packing???

## Algorithms

- randomize algorithms (fast, simple, and concurrent)
- greedy algorithm (requires at least sorting)
- primal-dual (fast)

---

## Greedy-Vertex-Cover

Input: G = (V, E)
Output: vertex cover U
1. U = {}
2. do chose v in V with max. degree
3.   U = U + {v}
4.   remove v and every edge adjacent to v
5. until all edges covered
6. return U

Requirements:
- Need a heap to maintain max. degree
- Only for unweighted problems.

---

## Input/Output

Input: G = (V, E) with non-negative vertex weights w: V ↦ N
Output: vertex cover U

---

## ILP formulation of Vertex Cover

```
            ⎛___        ⎞
    min     ⎜╲   w  ⋅ x ⎟
            ⎜╱    v    v⎟
            ⎜‾‾‾        ⎟
            ⎝i∈V        ⎠
                     
    s.t.    x  + x  ≥ 1, ∀ (u, v) ∈ E      
             u    v          

            x  ∈ {0, 1}, ∀ v ∈ V      
             v 
```



