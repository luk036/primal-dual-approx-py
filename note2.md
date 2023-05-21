# ☯ Primal-dual approximation algorithms

@luk036

---

## Vertex Cover

- Instance: G = (V, E) 
- Solution: A vertex cover for G, i.e., a subset U 
  such that, for each edge (u,v) ∈ E, at least one of 
  u and v belongs to U
- Measure: Cardinality of the vertex cover, i.e. ∣U∣

---

## Greedy-Vertex-Cover

┌─┬─────────────────────────────────────────┐
│1│U = {}                                   │
│2│do chose v in V with max. degree         │
│3│    U = U + {v}                          │
│4│    remove v and every edge adjacent to v│
│5│until all edges covered                  │
│6│return U                                 │
└─┴─────────────────────────────────────────┘

Requirements:

- Need a heap to maintain max. degree
- Only for unweighted problems.

---

## Weighted Vertex Cover

- Instance: G = (V, E) with non-negative vertex weights w: V ↦ N
- Solution: A vertex cover for G, i.e., a subset U 
  such that, for each edge (u,v) ∈ E, at least one of 
  u and v belongs to U

---

## ILP Formulation of Weighted Vertex Cover

```
            ⎛___        ⎞
    min     ⎜╲   w  ⋅ x ⎟
            ⎜╱    v    v⎟
            ⎜‾‾‾        ⎟
            ⎝i∈V        ⎠
                     
    s.t.    x  + x  ≥ 1, ∀ (u, v) ∈ E      
             u    v          

            x  ∈ {0, 1}, ∀ v ∈ V.      
             v 
```

---

## LP Relaxation of Weighted Vertex Cover

```
            ⎛___        ⎞
    min     ⎜╲   w  ⋅ x ⎟
            ⎜╱    v    v⎟
            ⎜‾‾‾        ⎟
            ⎝i∈V        ⎠
                     
    s.t.    x  + x  ≥ 1, ∀ (u, v) ∈ E      
             u    v          

            0 ≤ x  ≤ 1, ∀ v ∈ V.
                 v    
```

---

## Dual LP of LP Relaxation

```
            ⎛___   ⎞    
    max     ⎜╲   y ⎟    
            ⎜╱    e⎟    
            ⎜‾‾‾   ⎟    
            ⎝e∈E   ⎠    

           ___          
    s.t.   ╲     y  ≤ w , ∀ v ∈ V,
           ╱      e    v
           ‾‾‾          
        e∈adj(v)

        y  ≥ 0, ∀ e ∈ E.
         e              
```

