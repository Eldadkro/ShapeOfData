import scipy.sparse as sparse
import scipy.io as sio
import scipy.stats as stats
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from time import time
# own code
import graph_tools as gtl
import invarients as inva
import cpp


G = gtl.read_graph_from_edgelist("networks-random/brain274/bn-mouse_brain_1.edges")
# G = gtl.read_graph_from_edgelist("networks-random/mamalia-primate-18/graph.edges")
d =dict(nx.all_pairs_dijkstra_path_length(G))
for node in d.keys():
    print(node)
dists = gtl.convert_dist_dict_to_narray(d,G.nodes)
print(dists[0,:])
print(dists.shape)
print(cpp.q_extend_single(dists,2))