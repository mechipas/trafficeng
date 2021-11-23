import numpy as np
from dyntapy.demand import od_graph_from_matrix
from numpy import genfromtxt
from dyntapy.networks.get_networks import get_toy_network
g = get_toy_network('siouxfalls')

my_data = genfromtxt('SiouxFalls_od.csv', delimiter=',', skip_header=1)
od = my_data.copy()
od[:, (0, 1)] -= 1


g_od = od_graph_from_matrix(od, g.nodes.data('x_coord'), g.nodes.data('y_coord'))
