import sys
import os

# Add parent_directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

#packeges
import math
import itertools
import networkx as nx
import numpy as np


#my code
import libarary.invarients as inva
import libarary.graph_tools as glt
import libarary.cpp as cpp

class TestBindingsComplete:

    G:nx.Graph = nx.read_edgelist("tests/networks/net1.edges")
    distances = dict(nx.all_pairs_dijkstra_path_length(G))
    M = glt.convert_dist_dict_to_narray(distances,G.nodes)

    def test_q_extent_single(self):
        
        assert cpp.q_extend_single(self.M, 3) == (2/inva.choose(self.G.number_of_nodes(),2))

    def test_q_packing(self):
        assert cpp.q_packing_single(self.M,3) == 0.5

    def test_excess_global(self):
        assert cpp.excess_global_single(self.M) == 1

    def test_q_extent_single(self):
        assert cpp.q_extend_multi(self.M, 3) == (2/inva.choose(self.G.number_of_nodes(),2))
    



class TestBindingsLine:
    G:nx.Graph = nx.read_edgelist("tests/networks/net2.edges")
    distances = dict(nx.all_pairs_dijkstra_path_length(G))  
    M = glt.convert_dist_dict_to_narray(distances,G.nodes)

    def test_q_extent_single(self):
        assert cpp.q_extend_single(self.M, 2) == (4/inva.choose(self.G.number_of_nodes(),2))

    def test_q_packing(self):
        assert cpp.q_packing_single(self.M,2) == 0.5

    def test_excess_global(self):
        assert cpp.excess_global_single(self.M) == 6