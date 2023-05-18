# -*- coding: utf-8 -*-
"""
Minimum vertex cover for weighed graphs.
1. Support Lazy evalution
"""
from typing import Union
# import random


def min_vertex_cover_fast(gra, weight: Union[list, dict],
                          coverset: set) -> Union[int, float]:
    """Perform minimum weighted vertex cover using primal-dual
    approximation algorithm

    Args:
        gra ([type]): [description]
        weight (Union[list, dict]): [description]
        coverset (set): [description]

    Returns:
        Union[int, float]: [description]
    """
    total_dual_cost = 0  # for assertion
    total_primal_cost = 0
    gap = weight.copy()

    for u, vtx in gra.edges():
        if u in coverset or vtx in coverset:
            continue
        if gap[u] < gap[vtx]:
            u, vtx = vtx, u  # swap
        coverset.add(vtx)
        total_dual_cost += gap[vtx]
        total_primal_cost += weight[vtx]
        gap[u] -= gap[vtx]
        gap[vtx] = 0

    assert total_dual_cost <= total_primal_cost
    return total_primal_cost


def min_maximal_independant_set(gra, weight: Union[list, dict], indset: set,
                                dep: set) -> Union[int, float]:
    """Perform minimum weighted maximal independant using primal-dual

    Args:
        gra (nx.Graph): a undirected graph
        weight (Union[list, dict]): weight of vertex
        indset (set): [description]
        dep (set): [description]

    Returns:
        Union[int, float]: total primal cost
    """
    def coverset(u):
        dep.add(u)
        for vtx in gra[u]:
            dep.add(vtx)

    gap = weight.copy()
    total_primal_cost = 0
    total_dual_cost = 0
    for u in gra:
        if u in dep:
            continue
        if u in indset:  # pre-define indepentant
            # coverset(u)
            continue
        min_val = gap[u]
        min_vtx = u
        for vtx in gra[u]:
            if vtx in dep:
                continue
            if min_val > gap[vtx]:
                min_val = gap[vtx]
                min_vtx = vtx
        indset.add(min_vtx)
        coverset(min_vtx)
        total_primal_cost += weight[min_vtx]
        total_dual_cost += min_val
        if min_vtx == u:
            continue
        for vtx in gra[u]:
            gap[vtx] -= min_val

    assert total_dual_cost <= total_primal_cost
    return total_primal_cost
