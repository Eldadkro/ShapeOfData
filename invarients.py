"""Module for calculating the invarients of the paper"""
import math
from itertools import permutations
import networkx as nx



def choose(n: int, k: int) -> int:
    """calculate the C(n,k)"""
    return math.comb(n, k)

def q_tuple_length(tup:tuple, distances:dict)->int:
    """calculate the length of a q-tuple by summing the distances"""
    length = 0
    for i in range(1,len(tup)):
        length += distances.get(tup[i-1],{}).get(tup[i],0)
    return length 

def q_extent_single(q: int, G: nx.Graph):
    """
    Given a weighted graph with attribute weights
    calcualte the q_extent with a single process
    """
    edges: int = choose(G.number_of_edges(), 2)
    lens = dict(nx.all_pairs_dijkstra_path_length(G))
    q_tuples = permutations(G.nodes,q)
    max_q_tuple = 0
    for tup in q_tuples:
        length = q_tuple_length(tup,lens)
        max_q_tuple = max(max_q_tuple,length)
    result = 1/(edges) * max_q_tuple
    return result

