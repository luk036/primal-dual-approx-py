# ☯ Primal-dual approximation algorithms (3)

@luk036

---

## Example 1: Weighted Vertex Cover for Hypergraph

- Instance: H = (V, E) with non-negative vertex weights w: V ↦ N
- Solution: A vertex cover for H, i.e., a subset U such that, for each edge e ∈ E, at least one of adj(e) belongs to U

```
    a───►c───┬─►e───►g
           ┌─┼──┘
           │ └──┐
    b───►d─┴───►f───►h
```

---

## ILP Formulation of Weighted Vertex Cover

```
            ⎛___        ⎞
    min     ⎜╲   w  ⋅ x ⎟
            ⎜╱    v    v⎟
            ⎜‾‾‾        ⎟
            ⎝v∈V        ⎠

           ___
    s.t.   ╲   x  ≥ 1 , ∀ e ∈ E,
           ╱    v
           ‾‾‾
        v∈adj(e)

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
            ⎝v∈V        ⎠

           ___
    s.t.   ╲   x  ≥ 1 , ∀ e ∈ E,
           ╱    v
           ‾‾‾
        v∈adj(e)

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
    s.t.   ╲   y  ≤ w , ∀ v ∈ V,
           ╱    e    v
           ‾‾‾
        e∈adj(v)

            y  ≥ 0, ∀ e ∈ E.
             e
```

---

## Example 2: Weighted Cycle Cover

- Instance: G = (V, E) with non-negative vertex weights w: V ↦ N
- Define: a cycle c is a subset of V ... , C is a set of all cycles
- Solution: A vertex cover for G, i.e., a subset U such that, for each cycle c ∈ C, at least one of vertices belongs to U

```
 b───c───d───g
 │   │  ╱│
 │   │ ╱ │
 │   │╱  │
 a   e───f
```

---

## ILP Formulation of Weighted Vertex Cover

```
            ⎛___        ⎞
    min     ⎜╲   w  ⋅ x ⎟
            ⎜╱    v    v⎟
            ⎜‾‾‾        ⎟
            ⎝v∈V        ⎠
           ___
    s.t.   ╲   x  ≥ 1 , ∀ c ∈ C,
           ╱    v
           ‾‾‾
           v∈c

            x  ∈ {0, 1}, ∀ v ∈ V.
             v
```

---

## LP Relaxation of Weighted Cycle Cover

```
            ⎛___        ⎞
    min     ⎜╲   w  ⋅ x ⎟
            ⎜╱    v    v⎟
            ⎜‾‾‾        ⎟
            ⎝v∈V        ⎠

           ___
    s.t.   ╲   x  ≥ 1 , ∀ c ∈ C,
           ╱    v
           ‾‾‾
           v∈c

            0 ≤ x  ≤ 1, ∀ v ∈ V.
                 v
```

---

## Dual LP of LP Relaxation

```
            ⎛___   ⎞
    max     ⎜╲   y ⎟
            ⎜╱    c⎟
            ⎜‾‾‾   ⎟
            ⎝c∈C   ⎠
           ___
    s.t.   ╲   y  ≤ w , ∀ v ∈ V,
           ╱    c    v
           ‾‾‾
          c: v∈c

            y  ≥ 0, ∀ c ∈ C.
             c
```
