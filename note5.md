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
                    ___     ___         
            x  +    ╲       ╲    x  ≥ 1,   ∀ e ∈ E,
             e      ╱       ╱     f    
                    ‾‾‾     ‾‾‾         
                 v∈adj(e) f∈adj(v)      

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
                    ___     ___         
            x  +    ╲       ╲    x  ≥ 1,   ∀ e ∈ E,
             e      ╱       ╱     f    
                    ‾‾‾     ‾‾‾         
                 v∈adj(e) f∈adj(v)      

            0 ≤ x  ≤ 1, ∀ v ∈ V.
                 v    
```

---

## Dual LP of LP Relaxation

```
            ___        ___         
    max     ╲   y  -   ╲    z  
            ╱    e     ╱     v    
            ‾‾‾        ‾‾‾         
            e∈E        v∈V      

               ___ ⎛       ___     ⎞    
    s.t.   y + ╲   ⎜-z  +  ╲    y  ⎟  ≤ w ,   ∀ e ∈ E,
            e  ╱   ⎜  v    ╱     f ⎟     e
               ‾‾‾ ⎝       ‾‾‾     ⎠    
             v∈adj(e)   f∈adj(v)      

            y  ≥ 0, ∀ e ∈ E.
             e              

            z  ≥ 0, ∀ v ∈ V.
             v              
```
