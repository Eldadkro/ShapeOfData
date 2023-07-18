"""Module providing tools to read and write graphs"""
import networkx as nx
import numpy as np

def read_graph_from_edgelist(path:str) -> nx.Graph:
    """reads a graph from .edge file"""
    f = open(path, "r", encoding="utf_8")
    edges = {}
    nodes = set()
    for line in f:
        split = line.split(" ")
        edge = [int(split[0]), int(split[1])]
        edge.sort()
        nodes.add(edge[0])
        nodes.add(edge[1])
        #TODO
        weight = float(1)
        edges[tuple(edge)] = weight

    G = nx.Graph()
    G.add_nodes_from(nodes)
    G.add_edges_from(edges.keys())
    return G


def convert_dist_dict_to_narray(dists_dict:dict, nodes:list) -> np.array:
    """takes a set of nodes and dists dictionary and return a dense matrix of distances"""
    nodes_indecies = dict()
    for i,node in enumerate(nodes):
        nodes_indecies[node] = i
    dists_matrix = np.zeros((len(nodes),len(nodes)))
    for source,targets in dists_dict.items():
        for target,weight in targets.items():
            dists_matrix[nodes_indecies[source]][nodes_indecies[target]] = weight
    return dists_matrix


