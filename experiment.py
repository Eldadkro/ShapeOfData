import numpy as np
import libarary.cpp as cpp
import networkx as nx
from time import time
import libarary.graph_tools as gtl
from collections import defaultdict


def test(G: nx.Graph):
    # print("|V| = ", G.number_of_nodes())
    res = {}
    clocks = []
    start = time()
    # convert
    dists = gtl.convert_dist_dict_to_narray(
        dict(nx.all_pairs_dijkstra_path_length(G)), list(G.nodes)
    )
    end = time()
    clocks.append(end - start)
    # print("clock convert: ", clocks[-1])
    # q-extend3
    res["q_ext3_multi"] = cpp.q_extend_multi(dists, 3)
    end = time()
    clocks.append(end - start)
    # print("clock q_extend 3 multi: ", clocks[-1], res["q_ext3_multi"] )
    # q-extend4
    start = time()
    res["q_ext4_multi"] = cpp.q_extend_multi(dists, 4)
    end = time()
    clocks.append(end - start)
    # print("clock q_extend 4 multi: ", clocks[-1], res["q_ext4_multi"])
    # excess
    start = time()
    res["excess"] = cpp.excess_global_single(dists)
    end = time()
    clocks.append(end - start)
    # print("clock excess_global single: ", clocks[-1], res["excess"])
    # q-packing3
    start = time()
    res["q_packing3_multi"] = cpp.q_packing_multi(dists, 3)
    end = time()
    clocks.append(end - start)
    # print("clock q_packing 3 ,multi: ", clocks[-1], res["q_packing3_multi"])
    # q-packing4
    start = time()
    res["q_packing4_multi"] = cpp.q_packing_multi(dists, 4)
    end = time()
    clocks.append(end - start)
    # print("clock q_packing 4 ,multi: ", clocks[-1], res["q_packing4_multi"])
    return res


def convert_res(res:dict) ->dict : 
    new_res = {}
    new_res["q-extend3"] = res["q_ext3_multi"]
    new_res["q-extend4"] = res["q_ext4_multi"]
    new_res["excess"] = res["excess"]
    new_res["q-packing3"] = res["q_packing3_multi"]
    new_res["q-packing4"] = res["q_packing4_multi"]
    return new_res

def block_exp(block: np.array):
    """gets a block and runs the convert the block to a usable graph and runs the expemenint
    on it"""
    weight_matrix = gtl.convert_block_to_weighted_graph(block)
    G = nx.from_numpy_array(weight_matrix)
    return test(G)


def img_exp(img: np.array, block_size=11) -> dict:
    """image experiment tnat splits the picture to blocks and return a dict
    with the results of the blocks invarients"""
    m, n = img.shape
    print(m, n)
    res = defaultdict(lambda: [])
    i=0
    for y in range(0, m - block_size, block_size):
        for x in range(0, n - block_size, block_size):
            block = img[y : y + block_size, x : x + block_size]
            block_res = block_exp(block)
            for key in block_res.keys():
                res[key].append(block_res[key])
            i += 1
            if i % 10 == 0:
                print(i)
            
    return convert_res(res)

