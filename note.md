# ☯ Primal-dual approximation algorithms

@luk036

---

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

---

## Examples

- Vertex Cover

- Clustering in multi-level circuit partitioning
    - minimum weighted maximal matching

- Double patterning complement with E-beam
    - graph bipartization
    - minimum odd-cycle cover problem

- Double patterning with DSA (directed self-assembly)
    - Set-cover problem:

```
       o     o o    o     o
       o     o o    o       o
                    o
```

---

## Algorithms

- randomize algorithms (fast, simple, and concurrent)
- greedy algorithm (requires at least sorting)
- primal-dual (fast)




```
    b  c  d  e
    #--o--#--o
    |  | /|
    o  |/ |
    a  #--o
       e  f

   a       b        e       g
   o-------#-----*--o-------#
                 |  |
              ,--)--'
              |  |
              |  `--.
              |     |
   o-------#--*-----o-------#
   c       d        f       h


    b  c  d  e
    o--o--o--o
    |  | /|
    o  |/ |
    a  o--o
       e  f
```
