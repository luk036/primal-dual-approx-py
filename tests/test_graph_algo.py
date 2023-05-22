from pldl.netlist import create_drawf
from pldl.graph_algo import min_vertex_cover_fast, min_maximal_independant_set
from pldl.cover import min_vertex_cover, min_cycle_cover, min_odd_cycle_cover


def test_min_vertex_cover():
    hgr = create_drawf()
    weight = dict()

    for node in hgr.gra:
        weight[node] = 1
        # covset[node] = False

    _, rslt = min_vertex_cover(hgr.gra, weight)
    assert rslt == 9


def test_min_vertex_cover_fast():
    hgr = create_drawf()
    weight = dict()

    for node in hgr.gra:
        weight[node] = 1
        # covset[node] = False

    _, rslt = min_vertex_cover_fast(hgr.gra, weight)
    assert rslt == 8


def test_min_maximal_independant_set():
    hgr = create_drawf()
    weight = dict()

    for node in hgr.gra:
        weight[node] = 1

    _, rslt = min_maximal_independant_set(hgr.gra, weight)
    assert rslt == 7


def test_min_cycle_cover():
    hgr = create_drawf()
    weight = dict()

    for node in hgr.gra:
        weight[node] = 1
        # covset[node] = False

    _, rslt = min_cycle_cover(hgr.gra, weight)
    assert rslt == 3


def test_min_odd_cycle_cover():
    hgr = create_drawf()
    weight = dict()

    for node in hgr.gra:
        weight[node] = 1
        # covset[node] = False

    _, rslt = min_odd_cycle_cover(hgr.gra, weight)
    assert rslt == 0
