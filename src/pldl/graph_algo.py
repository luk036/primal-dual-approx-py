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
        if coverset[u] or coverset[v]:
            continue
        if gap[u] < gap[v]:
            u, v = v, u  # swap
        coverset[v] = True
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
        dep[u] = True
        for v in G[u]:
            dep[v] = True

    gap = weight.copy()
    total_primal_cost = 0
    total_dual_cost = 0
    for u in G:
        if dep[u]:
            continue
        if indset[u]:  # pre-define indepentant
            coverset(u)
            continue
        min_val = gap[u]
        min_vtx = u
        for v in G[u]:
            if dep[v]:
                continue
            if min_val > gap[v]:
                min_val = gap[v]
                min_vtx = v
        coverset(min_vtx)
        indset[min_vtx] = True
        total_primal_cost += weight[min_vtx]
        total_dual_cost += min_val
        if min_vtx == u:
            continue
        for v in G[u]:
            gap[v] -= min_val

    assert total_dual_cost <= total_primal_cost
    return total_primal_cost
