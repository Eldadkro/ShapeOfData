# %%
import scipy.sparse as sparse
import scipy.io as sio
import scipy.stats as stats
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from time import time
import pandas as pd
# own code
import libarary.graph_tools as gtl
import libarary.invarients as inva
import libarary.cpp as cpp

# %%
cpp.test()

# %%
G = gtl.read_graph_from_edgelist("networks-random/brain274/bn-mouse_brain_1.edges")
G.number_of_nodes()

# %%
clocks = []
start = time()
dists = gtl.convert_dist_dict_to_narray(dict(nx.all_pairs_dijkstra_path_length(G)),list(G.nodes))
end = time()
clocks.append(end -start)
print("clock convert: ", clocks[-1])
start = time()
q_extend3 = cpp.q_extend_single(dists,3)
end = time()
clocks.append(end -start)
print("clock q_extend3: ", clocks[-1])

start = time()
q_extend5 = cpp.q_extend_single(dists,5)
end = time()
# clocks.append(end -start)
# print("clock q_extend5: ", clocks[-1])
# start = time()
# q_extend7 = cpp.q_extend_single(dists,7)
# end = time()
# clocks.append(end -start)
# print("clock q_extend7: ", clocks[-1])


# %%
G = gtl.read_graph_from_edgelist(
        "networks-random/memalia-big/mammalia-voles-bhp-trapping.edges"
    )
print(G.number_of_nodes())

start = time()
dists = gtl.convert_dist_dict_to_narray(dict(nx.all_pairs_dijkstra_path_length(G)),list(G.nodes))
res= cpp.q_extend_single(dists, 3)
end = time()
print("results: ", res)
print("time: ", end-start)



