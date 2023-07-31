"""Module that tests the code"""
#%%
import sys
import os

# Add parent_directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

#packeges
import math
import itertools
import networkx as nx


#my code
import libarary.invarients as inva
import libarary.graph_tools as glt

class TestInvarientsComplete:

    G:nx.Graph = nx.read_edgelist("tests/networks/net1.edges")
    
    distances = dict(nx.all_pairs_dijkstra_path_length(G))
    def test_choose(self):
        assert inva.choose(3,2) == 3

    def test_q_tuple_length(self):
        g = self.G
        tup = ('3','5','9')
        assert inva.q_tuple_length(tup, self.distances) == 2, self.distances['3']

    def test_q_extent_single(self):
        assert inva.q_extent_single(3, self.G) == (2/inva.choose(self.G.number_of_nodes(),2))

    def test_excess_local(self):
        assert inva.excess_local(self.G,'3','5','9') == 1
    
    def test_max_path_length(self):
        tup = ('3','5','9')
        assert inva.max_path_length(tup,self.distances) == 1

    def test_q_packing(self):
        assert inva.q_packing(self.G,3) == 0.5


class TestInvarientsLine:
    G:nx.Graph = nx.read_edgelist("tests/networks/net2.edges")
    distances = dict(nx.all_pairs_dijkstra_path_length(G))  

    def test_q_tuple_length_3(self):
        g = self.G
        tup = ('0','1','2')
        assert inva.q_tuple_length(tup, self.distances) == 2

    def test_q_tuple_length_diam(self):
        g = self.G
        tup = ('0','4')
        assert inva.q_tuple_length(tup, self.distances) == 4

    def test_excess_local(self):
        assert inva.excess_local(self.G,'4','2','0') == 4

    def test_max_path_length(self):
        tup = ('0','3','4')
        assert inva.max_path_length(tup,self.distances) == 4
    
    def test_q_packing(self):
        assert inva.q_packing(self.G,3) == 1

# #%%
# import networkx as nx
# G:nx.Graph = nx.read_edgelist("networks/net1.edges") 
# %%
