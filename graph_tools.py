"""Module providing tools to read and write graphs"""
import networkx as nx

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
        weight = float(split[2])
        edges[tuple(edge)] = weight

    G = nx.Graph()
    G.add_nodes_from(nodes)
    G.add_edges_from(edges.keys())
    return G
