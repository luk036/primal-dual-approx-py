
from pldl.netlist import create_drawf
from pldl.netlist_algo import min_maximal_matching
from pldl.cover import min_hyper_vertex_cover


def test_min_vertex_cover():
    hgr = create_drawf()
    weight = dict()

    for node in hgr.modules:
        weight[node] = 1

    _, rslt = min_hyper_vertex_cover(hgr, weight)
    assert rslt == 6


def test_min_maximal_matching():
    hgr = create_drawf()
    weight = dict()

    for net in hgr.nets:
        weight[net] = 1

    _, rslt = min_maximal_matching(hgr, weight)
    assert rslt == 3
