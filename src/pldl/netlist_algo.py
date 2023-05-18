"""
Minimum vertex cover for weighted netlist.
"""


def min_maximal_matching(hgr, weight, matchset, dep):
    """Perform minimum weighted maximal matching using primal-dual
    approximation algorithm

    Returns:
        [type]: [description]
    """
    def cover(net):
        for vtx in hgr.gra[net]:
            dep.add(vtx)

    def any_of_dep(net):
        return any(vtx in dep for vtx in hgr.gra[net])

    gap = weight.copy()
    total_primal_cost = 0
    total_dual_cost = 0
    for net in hgr.nets:
        if any_of_dep(net):
            continue
        if net in matchset:  # pre-define matching
            # cover(net)
            continue
        min_val = gap[net]
        min_net = net
        for vtx in hgr.gra[net]:
            for net2 in hgr.gra[vtx]:
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
        for vtx in hgr.gra[net]:
            for net2 in hgr.gra[vtx]:
                # if net2 == net:
                #     continue
                gap[net2] -= min_val

    assert total_dual_cost <= total_primal_cost
    return total_primal_cost
