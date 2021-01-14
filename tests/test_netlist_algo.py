
from pldl.netlist import create_drawf
from pldl.netlist_algo import min_vertex_cover, min_maximal_matching


def test_min_vertex_cover():
    H = create_drawf()
    weight = dict()
    covset = dict()

    for node in H.modules:
        weight[node] = 1
        covset[node] = False

    rslt = min_vertex_cover(H, weight, covset)
    assert rslt == 6


def test_min_maximal_matching():
    H = create_drawf()
    weight = dict()
    indset = dict()
    depset = dict()

    for net in H.nets:
        weight[net] = 1
        indset[net] = False

    for v in H.modules:
        depset[v] = False

    rslt = min_maximal_matching(H, weight, indset, depset)
    assert rslt == 3
