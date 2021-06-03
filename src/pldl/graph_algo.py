# -*- coding: utf-8 -*-
"""
Minimum vertex cover for weighed graphs.
1. Support Lazy evalution
"""


def min_odd_cycle_cover(G, weight, coverset):
    """ @todo """
    pass


def min_vertex_cover(G, weight, coverset):
    """Perform minimum weighted vertex cover using primal-dual
    approximation algorithm

    Returns:
        [type]: [description]
    """
    total_dual_cost = 0  # for assertion
    total_primal_cost = 0
    gap = weight.copy()

    for u, v in G.edges():
        if u in coverset or v in coverset:
            continue
        if gap[u] < gap[v]:
            u, v = v, u  # swap
        coverset.add(v)
        total_dual_cost += gap[v]
        total_primal_cost += weight[v]
        gap[u] -= gap[v]
        gap[v] = 0

    assert total_dual_cost <= total_primal_cost
    assert total_primal_cost <= 2 * total_dual_cost
    return total_primal_cost


def min_maximal_independant_set(G, weight, indset, dep):
    """Perform minimum weighted maximal independant using primal-dual
    approximation algorithm

    Returns:
        [type]: [description]
    """
    def coverset(u):
        dep.add(u)
        for v in G[u]:
            dep.add(v)

    gap = weight.copy()
    total_primal_cost = 0
    total_dual_cost = 0
    for u in G:
        if u in dep:
            continue
        if u in indset:  # pre-define indepentant
            coverset(u)
            continue
        min_val = gap[u]
        min_vtx = u
        for v in G[u]:
            if v in dep:
                continue
            if min_val > gap[v]:
                min_val = gap[v]
                min_vtx = v
        coverset(min_vtx)
        indset.add(min_vtx)
        total_primal_cost += weight[min_vtx]
        total_dual_cost += min_val
        if min_vtx == u:
            continue
        for v in G[u]:
            gap[v] -= min_val

    assert total_dual_cost <= total_primal_cost
    return total_primal_cost
