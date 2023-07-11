"""Module for calculating the invarients of the paper"""
import math
from itertools import permutations,combinations
import networkx as nx


def choose(n: int, k: int) -> int:
    """calculate the C(n,k)"""
    return math.comb(n, k)


def q_tuple_length(tup: tuple, distances: dict):
    """calculate the length of a q-tuple by summing the distances"""
    length = 0
    for i in range(1, len(tup)):
        length += distances.get(tup[i - 1], {}).get(tup[i], 0)
    return length


def q_extent_single(q: int, G: nx.Graph):
    """
    Given a weighted graph with attribute weights
    calcualte the q_extent with a single process
    """
    edges: int = choose(G.number_of_nodes(), 2)
    lens = dict(nx.all_pairs_dijkstra_path_length(G))
    q_tuples = permutations(G.nodes, q)
    max_q_tuple = 0
    for tup in q_tuples:
        length = q_tuple_length(tup, lens)
        max_q_tuple = max(max_q_tuple, length)
    result = 1 / (edges) * max_q_tuple
    return result


def excess_local(G:nx.Graph, p, x, q):
    """
    calculate the excess of a tirangle of three nodes
    """
    distances = dict(nx.all_pairs_dijkstra_path_length(G))
    if x not in distances[p] or x not in distances[q] or p not in x not in distances[p]:
        return 0
    edges: list[float] = sorted([distances[p][x], distances[x][q], distances[q][p]])
    return edges[2] + edges[1] - edges[0]


def excess_local_with_dists(distances,p,x,q):
    if x not in distances[p] or x not in distances[q] or p not in x not in distances[p]:
        return 0
    edges: list[float] = sorted([distances[p][x], distances[x][q], distances[q][p]])
    return edges[2] + edges[1] - edges[0]

def excess_global(G:nx.Graph):
    """calculate the global excess of a graph"""
    max_excess = 0
    distances = dict(nx.all_pairs_dijkstra_path_length(G))
    for triangle in combinations(G.nodes(),3):
        max_excess = max(max_excess, excess_local_with_dists(distances,*triangle))
    return max_excess


def Haantjes_curvature(G:nx.Graph,p,q,r):
    """calcualte the haantjes curvature"""
    pass

def q_packing(G,q):
    """calcualte the q-packing radius of a graph"""
    pass