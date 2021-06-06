# -*- coding: utf-8 -*-
"""
Minimum vertex cover for weighed graphs.
1. Support Lazy evalution
"""
from collections import deque
from typing import Callable, Union


def min_vertex_cover_fast(G, weight: Union[list, dict],
                          coverset: set) -> Union[int, float]:
    """Perform minimum weighted vertex cover using primal-dual
    approximation algorithm

    Args:
        G ([type]): [description]
        weight (Union[list, dict]): [description]
        coverset (set): [description]

    Returns:
        Union[int, float]: [description]
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


def min_maximal_independant_set(G, weight: Union[list, dict], indset: set,
                                dep: set) -> Union[int, float]:
    """Perform minimum weighted maximal independant using primal-dual

    Args:
        G ([nx.Graph]): a undirected graph
        weight (Union[list, dict]): weight of vertex
        indset (set): [description]
        dep (set): [description]

    Returns:
        Union[int, float]: total primal cost
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
        indset.add(min_vtx)
        coverset(min_vtx)
        total_primal_cost += weight[min_vtx]
        total_dual_cost += min_val
        if min_vtx == u:
            continue
        for v in G[u]:
            gap[v] -= min_val

    assert total_dual_cost <= total_primal_cost
    return total_primal_cost


def pd_cover(Voilate: Callable, weight: Union[list, dict],
             soln: set) -> Union[int, float]:
    """Perform primal-dual approximation algorithm for covering problems

    Args:
        Voilate (Callable): an oracle for return a set of Voilate elements
        weight (Union[list, dict]): the weight of element
        soln ([type]): solution set

    Returns:
        Union[int, float]: total primal cost
    """
    gap = weight.copy()
    total_primal_cost = 0
    total_dual_cost = 0
    for S in Voilate():
        min_vtx = min(S, key=lambda v: gap[v])
        min_val = gap[min_vtx]
        soln.add(min_vtx)
        total_primal_cost += weight[min_vtx]
        total_dual_cost += min_val
        for v in S:
            gap[v] -= min_val
    assert total_dual_cost <= total_primal_cost
    return total_primal_cost


def min_vertex_cover(G, weight, coverset):
    """Perform minimum weighted vertex cover using primal-dual
    approximation algorithm

    Returns:
        [type]: [description]
    """
    def voilate():
        for u, v in G.edges():
            if u in coverset or v in coverset:
                continue
            yield [u, v]

    return pd_cover(voilate, weight, coverset)


def generic_bfs_edges(G, source, covered):
    depth_limit = len(G)
    info = {source: (source, depth_limit)}
    neighbors = G.neighbors
    queue = deque([(source, depth_limit)])
    while queue:
        parent, depth_now = queue.popleft()
        for child in neighbors(parent):
            if covered(child):
                continue
            if child not in info:
                info[child] = (parent, depth_now - 1)
                queue.append((child, depth_now - 1))
                continue
            succ, dlimit = info[child]
            if succ != parent:  # cycle found
                pass


def min_cycle_cover(G, weight, covset, dep):
    """Perform minimum cycle cover using primal-dual
    approximation algorithm

    Returns:
        [type]: [description]
    """
    def coverset(u):
        dep.add(u)
        for v in G[u]:
            dep.add(v)

    def voilate():
        for u in G:
            if u in dep:
                continue
            if u in covset:  # pre-define indepentant
                coverset(u)
                continue
            S = [u]
            for v in G[u]:
                if v in dep:
                    continue
                S += [v]
            yield S

    return pd_cover(voilate, weight, covset)


def min_odd_cycle_cover(G, weight, coverset):
    """ @todo """
    pass
