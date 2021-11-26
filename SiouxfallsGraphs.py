import numpy as np
from dyntapy.demand import od_graph_from_matrix
from numpy import genfromtxt
from dyntapy.networks.get_networks import get_toy_network
from dyntapy.sta.assignment import StaticAssignment
from dyntapy.sta.assignment_methods import DUE, SUN
from dyntapy.visualization import show_network, show_demand
from dyntapy.settings import _Visualization


def Siouxfallsfullgraph(g):
    my_data = genfromtxt('SiouxFalls_od.csv', delimiter=',', skip_header=1)
    od = my_data.copy()
    od_table = np.zeros((g.number_of_nodes(), g.number_of_nodes()), dtype=np.float32)
    for (i, j, val) in od:
        od_table[int(i - 1), int(j - 1)] = val

    node_x = [x for _, x in g.nodes.data('x_coord')]
    node_y = [y for _, y in g.nodes.data('y_coord')]
    od_graph = od_graph_from_matrix(od_table, node_x, node_y)
    return od_graph

def Siouxfalls1odgraph(g,o,d):
    my_data = genfromtxt('SiouxFalls_od.csv', delimiter=',', skip_header=1)
    od = my_data.copy()
    od_table = np.zeros((g.number_of_nodes(), g.number_of_nodes()), dtype=np.float32)
    for (i, j, val) in od:
        if int(i-1) == o and int(j-1) == d:
            od_table[int(i - 1), int(j - 1)] = val*150

    node_x = [x for _, x in g.nodes.data('x_coord')]
    node_y = [y for _, y in g.nodes.data('y_coord')]
    od_graph = od_graph_from_matrix(od_table, node_x, node_y)
    return od_graph


if __name__ == '__main__':
    _Visualization.link_keys =['link_id', 'length', 'capacity', 'free_speed', 'flow']
    g = get_toy_network('siouxfalls')
    edge_data = [(_, _, data) for _, _, data in g.edges.data()]
    sorted_edges = sorted(edge_data, key=lambda t: t[2]['link_id'])
    lengths = np.array([d['length'] for (_, _, d) in sorted_edges], dtype=np.float32)
    freespeeds = np.array([d['free_speed'] for (_, _, d) in sorted_edges], dtype=np.float32)
    freeflowCost = lengths / freespeeds
    show_network(g, notebook=False, toy_network=True, link_kwargs={'FreeFlowCosts': freeflowCost})

    g_od = Siouxfalls1odgraph(g, 0, 20)
    # show_demand(g_od, toy_network=True, notebook=False,)

    obj = StaticAssignment(g, g_od)
    path = np.array([0, 3, 9, 29, 37, 50])
    show_network(g, notebook=False, show_nodes=False, toy_network=True, highlight_links=path, link_kwargs={'FreeFlowCosts': freeflowCost})

    flows, costs = DUE(obj, 'dial_b')
    show_network(g, flows, notebook=False, show_nodes=False, toy_network=True, link_kwargs={'costs': costs, 'FreeFlowCosts': freeflowCost})

    flows, costs = SUN(obj)
    show_network(g, flows, notebook=False, show_nodes=False, toy_network=True, link_kwargs={'FreeFlowCosts': freeflowCost})
