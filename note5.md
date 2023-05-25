# ☯ Primal-dual approximation algorithms (5)

@luk036

---

## Example 1: Weighted Maximal Matching

- Instance: G = (V, E) with non-negative vertex weights w: V ↦ N

```
 b===c───d===g
 │   │  ╱│
 │   │ ╱ │
 │   │╱  │
 a   e===f
```

---

## ILP Formulation of Weighted Maximal Matching

```
            ⎛___        ⎞
    min     ⎜╲   w  ⋅ x ⎟
            ⎜╱    e    e⎟
            ⎜‾‾‾        ⎟
            ⎝e∈E        ⎠
           ___          
    s.t.   ╲   x  ≤ 1 , ∀ v ∈ V,
           ╱    e    
           ‾‾‾          
         e∈adj(v)
                    ___         
            x  +    ╲     x  ≥ 1,   ∀ e ∈ E,
             e      ╱      f    
                    ‾‾‾         
                 f∈adj(e)       

            x  ∈ {0, 1}, ∀ v ∈ V.      
             v 
```

---

## LP Relaxation of Weighted Maximal Matching

```
            ⎛___        ⎞
    min     ⎜╲   w  ⋅ x ⎟
            ⎜╱    e    e⎟
            ⎜‾‾‾        ⎟
            ⎝e∈E        ⎠
           ___          
    s.t.   ╲   x  ≤ 1 , ∀ v ∈ V,
           ╱    e    
           ‾‾‾          
         e∈adj(v)
                    ___         
            x  +    ╲     x  ≥ 1,   ∀ e ∈ E,
             e      ╱      f    
                    ‾‾‾         
                 f∈adj(e)       

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
