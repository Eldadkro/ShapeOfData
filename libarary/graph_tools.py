"""Module providing tools to read and write graphs"""
import networkx as nx
import numpy as np

def read_graph_from_edgelist(path:str, delimiter=" ") -> nx.Graph:
    """reads a graph from .edge file"""
    f = open(path, "r", encoding="utf_8")
    edges = {}
    nodes = set()
    for line in f:
        split = line.split(delimiter)
        edge = [int(split[0]), int(split[1])]
        edge.sort()
        nodes.add(edge[0])
        nodes.add(edge[1])
        if (len(split) >= 3):
            weight = float(split[2])
        else:
            weight = float
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
    dists_matrix = np.zeros((len(nodes),len(nodes)),dtype='double')
    for source,targets in dists_dict.items():
        for target,weight in targets.items():
            dists_matrix[nodes_indecies[source]][nodes_indecies[target]] = weight
    return dists_matrix

def convert_block_to_weighted_graph(block:np.array) -> np.array:
    """takes a block of usually 11x11 pixels and creates a weighted graph with weightes>=0 and return the
    assosiation matrix"""
    m,n = block.shape
    weight_matrix = np.zeros((block.shape[0]*block.shape[1], block.shape[0]*block.shape[1]), dtype="double")
    #horizontal 
    for y in range(0,m):
        for x in range(0,n-1):
            index = y*m + x
            edge_weight = abs(block[y,x] - block[y,x+1])
            weight_matrix[index, index + 1] = edge_weight
            weight_matrix[index + 1, index] = edge_weight

    #vectical 
    for y in range(0,m-1):
        for x in range(0,n):
            i1 = y*m + x
            i2 = (y+1)*m + x
            edge_weight = abs(block[y,x] - block[y+1,x])
            weight_matrix[i1,i2] = edge_weight
            weight_matrix[i2,i1] = edge_weight
    return weight_matrix

