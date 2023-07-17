"""Module for calculating the invarients of the paper"""
import math
from itertools import permutations, combinations
import networkx as nx
import multiprocessing as mp
import os

NUM_OF_PROCESSES = os.cpu_count()
CHUNK_SIZE = 1024**2 * 32


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
    calculate the q_extent with a single process
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


def q_extent_multi(q: int, G: nx.Graph):
    edges: int = choose(G.number_of_nodes(), 2)
    lens = dict(nx.all_pairs_dijkstra_path_length(G))
    q_tuples = permutations(G.nodes, q)
    ltuples = math.perm(G.number_of_nodes(), q)
    lens_gen = (lens for i in range(ltuples))
    args = zip(q_tuples, lens_gen)
    max_tup_length = 0
    with mp.Pool(NUM_OF_PROCESSES) as pool:
        chunk = 0
        end = ltuples // (CHUNK_SIZE)
        if ltuples % (CHUNK_SIZE) != 0:
            end += 1
        while chunk < end:
            unpacked_args = []
            for arg, _ in zip(args, range(CHUNK_SIZE)):
                unpacked_args.append(arg)
            max_chunck = max(
                pool.starmap(q_tuple_length, unpacked_args, CHUNK_SIZE // 32)
            )

            max_tup_length = max(max_tup_length, max_chunck)
            chunk += 1
    return max_tup_length


def excess_local(G: nx.Graph, p, x, q):
    """
    calculate the excess of a tirangle of three nodes
    """
    distances = dict(nx.all_pairs_dijkstra_path_length(G))
    if x not in distances[p] or q not in distances[x] or q not in distances[p]:
        return 0
    edges: list[float] = sorted([distances[p][x], distances[x][q], distances[p][q]])
    return edges[2] + edges[1] - edges[0]


def excess_local_with_dists(distances, p, x, q):
    if x not in distances[p] or q not in distances[x] or q not in distances[p]:
        return 0
    edges: list[float] = sorted([distances[p][x], distances[x][q], distances[p][q]])
    return edges[2] + edges[1] - edges[0]


def excess_global(G: nx.Graph):
    """calculate the global excess of a graph"""
    max_excess = 0
    distances = dict(nx.all_pairs_dijkstra_path_length(G))
    for triangle in combinations(G.nodes(), 3):
        max_excess = max(max_excess, excess_local_with_dists(distances, *triangle))
    return max_excess


def Haantjes_curvature(G: nx.Graph, p, q, r):
    """calcualte the haantjes curvature"""
    pass


def max_path_length(node_subset: tuple, distances: dict):
    """calculate the radius of a subset of nodes given a distance matrix"""
    max_dist = 0
    for i in range(1, len(node_subset)):
        for j in range(0, i):
            max_dist = max(max_dist, distances[node_subset[i]][node_subset[j]])
    return max_dist


def q_packing(G: nx.Graph, q):
    """calcualte the q-packing radius of a graph"""
    distances = dict(nx.all_pairs_dijkstra_path_length(G))
    min_radius = 0
    for tup in combinations(G.nodes(), q):
        min_radius = min(min_radius, max_path_length(tup, distances))
    return min_radius
