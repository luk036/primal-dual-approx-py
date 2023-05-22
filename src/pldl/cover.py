from collections import deque
# import networkx as nx
import copy
# from .netlist import Netlist
from typing import Generator
from typing import Set, Callable, Union, Optional, Tuple, Deque
from collections.abc import MutableMapping


def pd_cover(
    violate: Callable, weight: MutableMapping, soln: Set
) -> Tuple[Set, Union[int, float]]:
    """Perform primal-dual approximation algorithm for covering problems

    Args:
        violate (Callable): an oracle for return a set of violate elements
        weight (MutableMapping): the weight of element
        soln ([type]): solution set

    Returns:
        Union[int, float]: total primal cost
    """
    total_primal_cost = 0
    total_dual_cost = 0
    gap = copy.copy(weight)
    for S in violate():
        min_vtx = min(S, key=lambda vtx: gap[vtx])
        min_val = gap[min_vtx]
        soln.add(min_vtx)
        total_primal_cost += weight[min_vtx]
        total_dual_cost += min_val
        for vtx in S:
            gap[vtx] -= min_val
    assert total_dual_cost <= total_primal_cost
    return soln, total_primal_cost


def min_vertex_cover(
    gra, weight: MutableMapping, coverset: Optional[Set] = None
) -> Tuple[Set, Union[int, float]]:
    """Perform minimum weighted vertex cover using primal-dual
    approximation algorithm

    Returns:
        [type]: [description]
    """
    if coverset is None:
        coverset = set()

    def violate_graph() -> Generator:
        for utx, vtx in gra.edges():
            if utx in coverset or vtx in coverset:
                continue
            yield [utx, vtx]

    return pd_cover(violate_graph, weight, coverset)


def min_hyper_vertex_cover(
    hgr, weight: MutableMapping, coverset: Optional[Set] = None
) -> Tuple[Set, Union[int, float]]:
    """Perform minimum weighted vertex cover using primal-dual
    approximation algorithm

    Returns:
        [type]: [description]
    """
    if coverset is None:
        coverset = set()

    def violate_netlist() -> Generator:
        for net in hgr.nets:
            if any(vtx in coverset for vtx in hgr.gra[net]):
                continue
            yield hgr.gra[net]

    return pd_cover(violate_netlist, weight, coverset)


def min_cycle_cover(gra, weight: MutableMapping, coverset: Optional[Set] = None
                    ) -> Tuple[Set, Union[int, float]]:
    """Perform minimum cycle cover using primal-dual
    approximation algorithm

    Args:
        gra ([type]): [description]
        weight ([type]): [description]
        coverset ([type]): [description]
    """
    if coverset is None:
        coverset = set()

    def find_cycle():
        for info, parent, child in _generic_bfs_cycle(gra, coverset):
            return _construct_cycle(info, parent, child)

    def violate() -> Generator:
        while True:
            S = find_cycle()
            if S is None:
                break
            yield S

    return pd_cover(violate, weight, coverset)


def min_odd_cycle_cover(
    gra, weight: MutableMapping, coverset: Optional[Set] = None
) -> Tuple[Set, Union[int, float]]:
    """Perform minimum odd cycle cover using primal-dual
    approximation algorithm

    Args:
        gra ([type]): [description]
        weight ([type]): [description]
        coverset ([type]): [description]
    """
    if coverset is None:
        coverset = set()

    def find_odd_cycle():
        for info, parent, child in _generic_bfs_cycle(gra, coverset):
            _, depth_child = info[child]
            _, depth_parent = info[parent]
            if (depth_parent - depth_child) % 2 == 0:
                return _construct_cycle(info, parent, child)

    def violate() -> Generator:
        while True:
            S = find_odd_cycle()
            if S is None:
                break
            yield S

    return pd_cover(violate, weight, coverset)


def _construct_cycle(info, parent, child) -> Deque:
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
    S: Deque = deque()
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


def _generic_bfs_cycle(gra, coverset) -> Generator:
    depth_limit = len(gra)
    neighbors = gra.neighbors
    nodelist = list(gra.nodes())
    # random.shuffle(nodelist)
    for source in nodelist:
        if source in coverset:
            continue
        info = {source: (source, depth_limit)}
        queue = deque([source])
        while queue:
            parent = queue.popleft()
            succ, depth_now = info[parent]
            for child in neighbors(parent):
                if child in coverset:
                    continue
                if child not in info:
                    info[child] = (parent, depth_now - 1)
                    queue.append(child)
                    continue
                if succ == child:
                    continue
                # cycle found
                yield info, parent, child
