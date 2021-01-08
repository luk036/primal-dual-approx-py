
from pldl.netlist import create_drawf
from pldl.graph_algo import min_vertex_cover, min_maximal_independant_set


def test_min_vertex_cover():
    H = create_drawf()
    weight = dict()
    covset = dict()

    for node in H.G:
        weight[node] = 1
        covset[node] = False

    rslt = min_vertex_cover(H.G, weight, covset)
    assert rslt == 8


def test_min_maximal_independant_set():
    H = create_drawf()
    weight = dict()
    indset = dict()
    depset = dict()

    for node in H.G:
        weight[node] = 1
        indset[node] = False
        depset[node] = False

    rslt = min_maximal_independant_set(H.G, weight, indset, depset)
    assert rslt == 7
