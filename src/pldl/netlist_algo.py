"""
Minimum vertex cover for weighed netlist.
"""


def min_maximal_matching(H, weight, matchset, dep):
    """Perform minimum weighted maximal matching using primal-dual
    approximation algorithm

    Returns:
        [type]: [description]
    """
    def cover(net):
        for v in H.G[net]:
            dep.add(v)

    def any_of_dep(net):
        return any(v in dep for v in H.G[net])

    gap = weight.copy()
    total_primal_cost = 0
    total_dual_cost = 0
    for net in H.nets:
        if any_of_dep(net):
            continue
        if net in matchset:  # pre-define matching
            cover(net)
            continue
        min_val = gap[net]
        min_net = net
        for v in H.G[net]:
            for net2 in H.G[v]:
                if any_of_dep(net2):
                    continue
                if min_val > gap[net2]:
                    min_val = gap[net2]
                    min_net = net2
        cover(min_net)
        matchset.add(min_net)
        total_primal_cost += weight[min_net]
        total_dual_cost += min_val
        if min_net == net:
            continue
        gap[net] -= min_val
        for v in H[net]:
            for net2 in H.G[v]:
                # if net2 == net:
                #     continue
                gap[net2] -= min_val

    assert total_dual_cost <= total_primal_cost
    return total_primal_cost


def pd_cover(Voilate, weight, soln):
    """Perform primal-dual approximation algorithm

    Returns:
        [type]: [description]
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


def min_vertex_cover(H, weight, coverset):
    """Perform minimum weighted vertex cover using primal-dual
    approximation algorithm

    Returns:
        [type]: [description]
    """
    def voilate():
        for net in H.nets:
            if any(v in coverset for v in H.G[net]):
                continue
            yield H.G[net]

    return pd_cover(voilate, weight, coverset)
