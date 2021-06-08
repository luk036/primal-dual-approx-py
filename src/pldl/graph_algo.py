# -*- coding: utf-8 -*-
"""
Minimum vertex cover for weighed graphs.
1. Support Lazy evalution
"""
from collections import deque
from typing import Callable, Union
# import random


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
    return total_primal_cost


def min_maximal_independant_set(G, weight: Union[list, dict], indset: set,
                                dep: set) -> Union[int, float]:
    """Perform minimum weighted maximal independant using primal-dual

    Args:
        G (nx.Graph): a undirected graph
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
            # coverset(u)
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


def pd_cover(Violate: Callable, weight: Union[list, dict],
             soln: set) -> Union[int, float]:
    """Perform primal-dual approximation algorithm for covering problems

    Args:
        Violate (Callable): an oracle for return a set of Violate elements
        weight (Union[list, dict]): the weight of element
        soln ([type]): solution set

    Returns:
        Union[int, float]: total primal cost
    """
    gap = weight.copy()
    total_primal_cost = 0
    total_dual_cost = 0
    for S in Violate():
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
    def violate():
        for u, v in G.edges():
            if u in coverset or v in coverset:
                continue
            yield [u, v]

    return pd_cover(violate, weight, coverset)


def _construct_cycle(info, parent, child):
    """[summary]

    Args:
        info ([type]): [description]
        parent ([type]): [description]
        child ([type]): [description]

    Returns:
        [type]: [description]
    """
    _, depth_now = info[parent]
    _, depth_child = info[child]
    if depth_now < depth_child:
        node_a, depth_a = parent, depth_now
        node_b, depth_b = child, depth_child
    else:
        node_a, depth_a = child, depth_child
        node_b, depth_b = parent, depth_now
    S = deque()
    while depth_a < depth_b:
        S.append(node_a)
        node_a, depth_a = info[node_a]
    # depth_now == depth
    while node_a != node_b:
        S.append(node_a)
        S.appendleft(node_b)
        node_a, _ = info[node_a]
        node_b, _ = info[node_b]
    S.appendleft(node_b)
    return S


def _generic_bfs_cycle(G, covered):
    depth_limit = len(G)
    neighbors = G.neighbors
    nodelist = list(G.nodes())
    # random.shuffle(nodelist)
    for source in nodelist:
        if source in covered:
            continue
        info = {source: (source, depth_limit)}
        queue = deque([source])
        while queue:
            parent = queue.popleft()
            succ, depth_now = info[parent]
            for child in neighbors(parent):
                if child in covered:
                    continue
                if child not in info:
                    info[child] = (parent, depth_now - 1)
                    queue.append(child)
                    continue
                if succ == child:
                    continue
                # cycle found
                yield info, parent, child


def min_cycle_cover(G, weight, covered):
    """Perform minimum cycle cover using primal-dual
    approximation algorithm

    Args:
        G ([type]): [description]
        weight ([type]): [description]
        covered ([type]): [description]
    """
    def find_cycle():
        for info, parent, child in _generic_bfs_cycle(G, covered):
            return _construct_cycle(info, parent, child)

    def violate():
        while True:
            S = find_cycle()
            if S is None:
                break
            yield S

    return pd_cover(violate, weight, covered)


def min_odd_cycle_cover(G, weight, covered):
    """Perform minimum odd cycle cover using primal-dual
    approximation algorithm

    Args:
        G ([type]): [description]
        weight ([type]): [description]
        covered ([type]): [description]
    """
    def find_odd_cycle():
        for info, parent, child in _generic_bfs_cycle(G, covered):
            _, depth_child = info[child]
            _, depth_parent = info[parent]
            if (depth_parent - depth_child) % 2 == 0:
                return _construct_cycle(info, parent, child)

    def violate():
        while True:
            S = find_odd_cycle()
            if S is None:
                break
            yield S

    return pd_cover(violate, weight, covered)
