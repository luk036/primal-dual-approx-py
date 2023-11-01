# -*- coding: utf-8 -*-
"""
Minimum vertex cover for weighed graphs.
1. Support Lazy evalution
"""
from typing import Set, Union, Tuple, Optional
from typing import MutableMapping
import copy


def min_vertex_cover_fast(
    gra, weight: MutableMapping, coverset: Optional[Set] = None
) -> Tuple[Set, Union[int, float]]:
    """Perform minimum weighted vertex cover using primal-dual
    approximation algorithm

    Args:
        gra (nx.Graph): [description]
        weight (MutableMapping): [description]
        coverset (set): [description]

    Returns:
        Union[int, float]: [description]

    .. svgbob::
       :align: center

        b  c  d  e
        #--o--#--o
        |  | /|     ({b, d, e}, 3)
        o  |/ |
        a  #--o
           e  f

    Examples:
        >>> import networkx as nx
        >>> from pldl.graph_algo import min_vertex_cover_fast
        >>> gra = nx.Graph()
        >>> gra.add_edges_from([(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (2, 4), (3, 4)])
        >>> weight = {0: 1, 1: 1, 2: 1, 3: 1, 4: 1}
        >>> coverset = set()
        >>> min_vertex_cover_fast(gra, weight, coverset)
        ({0, 1, 2, 3}, 4)
    """
    if coverset is None:
        coverset = set()

    total_dual_cost = 0  # for assertion
    total_primal_cost = 0
    gap = copy.copy(weight)

    for utx, vtx in gra.edges():
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
    return coverset, total_primal_cost


def min_maximal_independant_set(
    gra, weight: MutableMapping, indset: Optional[Set] = None, dep: Optional[Set] = None
) -> Tuple[Set, Union[int, float]]:
    """Perform minimum weighted maximal independant set using primal-dual

    Args:
        gra (nx.Graph): a undirected graph
        weight (MutableMapping): weight of vertex
        indset (set): [description]
        dep (set): [description]

    Returns:
        Union[int, float]: total primal cost

    Examples:
        >>> import networkx as nx
        >>> from pldl.graph_algo import min_maximal_independant_set
        >>> gra = nx.Graph()
        >>> gra.add_edges_from([(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (2, 4), (3, 4)])
        >>> weight = {0: 1, 1: 1, 2: 1, 3: 1, 4: 1}
        >>> indset = set()
        >>> dep = set()
        >>> min_maximal_independant_set(gra, weight, indset, dep)
        ({0, 3}, 2)
    """
    if indset is None:
        indset = set()
    if dep is None:
        dep = set()

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
    return indset, total_primal_cost
