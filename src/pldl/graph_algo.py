# -*- coding: utf-8 -*-
"""
Minimum vertex cover for weighed graphs.
1. Support Lazy evalution
"""
import networkx as nx
from typing import Union, Set
from collections.abc import MutableSequence
import copy

def min_vertex_cover_fast(gra: nx.Graph, weight: MutableSequence,
                          coverset: Set) -> Union[int, float]:
    """Perform minimum weighted vertex cover using primal-dual
    approximation algorithm

    Args:
        gra ([type]): [description]
        weight (MutableSequence): [description]
        coverset (set): [description]

    Returns:
        Union[int, float]: [description]
    """
    total_dual_cost = 0  # for assertion
    total_primal_cost = 0
    gap = copy.copy(weight)

    for utx in gra:
        for vtx in gra[utx]:
            if utx in coverset or vtx in coverset:
                continue
            if gap[utx] < gap[vtx]:
                utx, vtx = vtx, utx  # swap
            coverset.add(vtx)
            total_dual_cost += gap[vtx]
            total_primal_cost += weight[vtx]
            gap[utx] -= gap[vtx]
            gap[vtx] = 0

    assert total_dual_cost <= total_primal_cost
    return total_primal_cost


def min_maximal_independant_set(gra, weight: MutableSequence, indset: Set,
                                dep: Set) -> Union[int, float]:
    """Perform minimum weighted maximal independant using primal-dual

    Args:
        gra (nx.Graph): a undirected graph
        weight (MutableSequence): weight of vertex
        indset (set): [description]
        dep (set): [description]

    Returns:
        Union[int, float]: total primal cost
    """
    def coverset(utx):
        dep.add(utx)
        for vtx in gra[utx]:
            dep.add(vtx)

    gap = copy.copy(weight)
    total_primal_cost = 0
    total_dual_cost = 0
    for utx in gra:
        if utx in dep:
            continue
        if utx in indset:  # pre-define indepentant
            # coverset(utx)
            continue
        min_val = gap[utx]
        min_vtx = utx
        for vtx in gra[utx]:
            if vtx in dep:
                continue
            if min_val > gap[vtx]:
                min_val = gap[vtx]
                min_vtx = vtx
        indset.add(min_vtx)
        coverset(min_vtx)
        total_primal_cost += weight[min_vtx]
        total_dual_cost += min_val
        if min_vtx == utx:
            continue
        for vtx in gra[utx]:
            gap[vtx] -= min_val

    assert total_dual_cost <= total_primal_cost
    return total_primal_cost
