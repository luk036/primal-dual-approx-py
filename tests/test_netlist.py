from pldl.netlist import create_drawf, create_test_netlist


def test_netlist():
    hyprgraph = create_test_netlist()
    assert hyprgraph.number_of_modules() == 3
    assert hyprgraph.number_of_nets() == 3
    assert hyprgraph.number_of_nodes() == 6
    assert hyprgraph.number_of_pins() == 6
    assert hyprgraph.get_max_degree() == 3
    assert hyprgraph.get_max_net_degree() == 3
    # assert not hyprgraph.has_fixed_modules
    # assert hyprgraph.get_module_weight_by_id(0) == 533
    assert isinstance(hyprgraph.module_weight, dict)


def test_drawf():
    hyprgraph = create_drawf()
    assert hyprgraph.number_of_modules() == 7
    assert hyprgraph.number_of_nets() == 6
    assert hyprgraph.number_of_pins() == 14
    assert hyprgraph.get_max_degree() == 3
    assert hyprgraph.get_max_net_degree() == 3
    # assert not hyprgraph.has_fixed_modules
    # assert hyprgraph.get_module_weight_by_id(1) == 3


def test_json():
    from networkx.readwrite import json_graph
    import json

    hyprgraph = create_drawf()
    data = json_graph.node_link_data(hyprgraph.gra)
    with open("testcases/drawf.json", "w") as fw:
        json.dump(data, fw, indent=1)
    with open("testcases/drawf.json", "r") as fr:
        data2 = json.load(fr)
    gra = json_graph.node_link_graph(data2)
    assert gra.number_of_nodes() == 13
    assert gra.graph["num_modules"] == 7
    assert gra.graph["num_nets"] == 6
    assert gra.graph["num_pads"] == 3


def test_json2():
    from networkx.readwrite import json_graph
    import json

    with open("testcases/p1.json", "r") as fr:
        data = json.load(fr)
    gra = json_graph.node_link_graph(data)
    assert gra.number_of_nodes() == 1735
    assert gra.graph["num_modules"] == 833
    assert gra.graph["num_nets"] == 902
    assert gra.graph["num_pads"] == 81
