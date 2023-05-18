
from pldl.netlist import create_drawf
from pldl.netlist_algo import min_maximal_matching
from pldl.cover import min_vertex_cover


def test_min_vertex_cover():
    hgr = create_drawf()
    weight = dict()
    covset = set()

    for node in hgr.modules:
        weight[node] = 1

    rslt = min_vertex_cover(hgr, weight, covset)
    assert rslt == 6


def test_min_maximal_matching():
    hgr = create_drawf()
    weight = dict()
    indset = set()
    depset = set()

    for net in hgr.nets:
        weight[net] = 1

    rslt = min_maximal_matching(hgr, weight, indset, depset)
    assert rslt == 3
