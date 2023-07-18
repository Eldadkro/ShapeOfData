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

dists = gtl.convert_dist_dict_to_narray(dict(nx.all_pairs_dijkstra_path_length(G)),G.nodes)
