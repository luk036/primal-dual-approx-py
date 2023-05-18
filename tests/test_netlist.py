
from pldl.netlist import create_drawf, create_test_netlist


def test_netlist():
    hgr = create_test_netlist()
    assert hgr.number_of_modules() == 3
    assert hgr.number_of_nets() == 3
    assert hgr.number_of_nodes() == 6
    assert hgr.number_of_pins() == 6
    assert hgr.get_max_degree() == 3
    assert hgr.get_max_net_degree() == 3
    # assert not hgr.has_fixed_modules
    # assert hgr.get_module_weight_by_id(0) == 533
    assert isinstance(hgr.module_weight, dict)


def test_drawf():
    hgr = create_drawf()
    assert hgr.number_of_modules() == 7
    assert hgr.number_of_nets() == 6
    assert hgr.number_of_pins() == 14
    assert hgr.get_max_degree() == 3
    assert hgr.get_max_net_degree() == 3
    # assert not hgr.has_fixed_modules
    # assert hgr.get_module_weight_by_id(1) == 3


def test_json():
    from networkx.readwrite import json_graph
    import json
    hgr = create_drawf()
    data = json_graph.node_link_data(hgr.gra)
    with open('testcases/drawf.json', 'w') as fw:
        json.dump(data, fw, indent=1)
    with open('testcases/drawf.json', 'r') as fr:
        data2 = json.load(fr)
    gra = json_graph.node_link_graph(data2)
    assert gra.number_of_nodes() == 13
    assert gra.graph['num_modules'] == 7
    assert gra.graph['num_nets'] == 6
    assert gra.graph['num_pads'] == 3


def test_json2():
    from networkx.readwrite import json_graph
    import json
    with open('testcases/p1.json', 'r') as fr:
        data = json.load(fr)
    gra = json_graph.node_link_graph(data)
    assert gra.number_of_nodes() == 1735
    assert gra.graph['num_modules'] == 833
    assert gra.graph['num_nets'] == 902
    assert gra.graph['num_pads'] == 81
