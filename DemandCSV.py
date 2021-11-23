import numpy as np
from dyntapy.demand import od_graph_from_matrix
from numpy import genfromtxt
from dyntapy.networks.get_networks import get_toy_network
from dyntapy.sta.assignment import StaticAssignment
from dyntapy.sta.assignment_methods import DUN, DUE, SUN, SUE
from dyntapy.visualization import show_network

g = get_toy_network('siouxfalls')

my_data = genfromtxt('SiouxFalls_od.csv', delimiter=',', skip_header=1)
od = my_data.copy()
od_table = np.zeros((g.number_of_nodes(), g.number_of_nodes()), dtype=np.float32)
for (i, j, val) in od:
    od_table[int(i-1), int(j-1)] = val

od_graph = od_graph_from_matrix(od_table, g.nodes.data('x_coord'), g.nodes.data('y_coord'))

obj = StaticAssignment(g, od_graph)

# DUE assignments

flows, costs = DUE(obj, 'dial_b')
show_network(g, flows, notebook=False, show_nodes=False, toy_network=True)
print(f'DUE {method=} ran successfully')