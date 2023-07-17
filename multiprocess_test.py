# %%
import pandas as pd
import multiprocessing as mp
import invarients as inva
import graph_tools as gtl
import os
from time import time

def func(iter):
    return "some thing" + str(iter)

if __name__ == "__main__":
    print("main")
    G = gtl.read_graph_from_edgelist(
        "networks-random/memalia-big/mammalia-voles-bhp-trapping.edges"
    )
    g_reptil = gtl.read_graph_from_edgelist(
        "networks-random/net1/reptilia-tortoise-network-pv.edges"
    )

    print("number of processors: ",os.cpu_count())
    start = time()
    reptil_res = inva.q_extent_multi(3, g_reptil)
    end = time()
    print("reptil results: ", reptil_res)
    print("time = "+str(end-start))
    start = time()
    G_res = inva.q_extent_single(3, G)
    end = time()
    print("big G results: ", G_res)
    print("time single = "+str(end-start))
    start = time()
    G_res = inva.q_extent_single(3, G)
    end = time()
    print("big G results: ", G_res)
    print("time multi = "+str(end-start))
    # with mp.Pool(16) as pool:
    #     for res in pool.imap_unordered(func,range(100),10):
    #         print(res)
