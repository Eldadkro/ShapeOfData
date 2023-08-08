"""Module: ctypes_test.py"""
import ctypes
import pathlib
import numpy as np
from numpy.ctypeslib import ndpointer
import os
import math


def q_extend_single(dists: np.array, q: int):
    n = len(dists)
    p = os.path.dirname(__file__) + "/libinvarientscpp.so"
    c_lib = ctypes.CDLL(p)
    c_q_extend_single = c_lib.q_extend_single
    c_q_extend_single.argtypes = [
        ndpointer(ctypes.c_double, flags="C_CONTIGUOUS"),
        ctypes.c_size_t,
        ctypes.c_size_t,
    ]
    c_q_extend_single.restype = ctypes.c_double
    return c_q_extend_single(dists, n, q) / math.comb(n, 2)

def q_extend_multi(dists: np.array, q: int):
    n = len(dists)
    p = os.path.dirname(__file__) + "/libinvarientscpp.so"
    c_lib = ctypes.CDLL(p)
    c_q_extend_multi = c_lib.q_extend_multi
    c_q_extend_multi.argtypes = [
        ndpointer(ctypes.c_double, flags="C_CONTIGUOUS"),
        ctypes.c_size_t,
        ctypes.c_size_t,
    ]
    c_q_extend_multi.restype = ctypes.c_double
    return c_q_extend_multi(dists, n, q) / math.comb(n, 2)


def excess_global_single(dists: np.array):
    n = len(dists)
    p = os.path.dirname(__file__) + "/libinvarientscpp.so"
    c_lib = ctypes.CDLL(p)
    c_excess_global = c_lib.excess_global_single
    c_excess_global.argtypes = [
        ndpointer(ctypes.c_double, flags="C_CONTIGUOUS"),
        ctypes.c_size_t,
    ]
    c_excess_global.restype = ctypes.c_double
    return c_excess_global(dists, n)


def q_packing_single(dists: np.array, q: int):
    n = len(dists)
    p = os.path.dirname(__file__) + "/libinvarientscpp.so"
    c_lib = ctypes.CDLL(p)
    q_packing_single = c_lib.q_packing_single
    q_packing_single.argtypes = [
        ndpointer(ctypes.c_double, flags="C_CONTIGUOUS"),
        ctypes.c_size_t,
        ctypes.c_size_t,
    ]
    q_packing_single.restype = ctypes.c_double
    return q_packing_single(dists, n, q)

def q_packing_multi(dists: np.array, q: int):
    n = len(dists)
    p = os.path.dirname(__file__) + "/libinvarientscpp.so"
    c_lib = ctypes.CDLL(p)
    q_packing_multi = c_lib.q_packing_multi
    q_packing_multi.argtypes = [
        ndpointer(ctypes.c_double, flags="C_CONTIGUOUS"),
        ctypes.c_size_t,
        ctypes.c_size_t,
    ]
    q_packing_multi.restype = ctypes.c_double
    return q_packing_multi(dists, n, q)



def test():
    p = os.path.dirname(__file__) + "/libinvarientscpp.so"
    c_lib = ctypes.CDLL(p)
    c_lib.test()


def print_dists(matrix):
    p = os.path.dirname(__file__) + "/libinvarientscpp.so"
    c_lib = ctypes.CDLL(p)
    c_print_dists = c_lib.print_dists
    c_print_dists.argtypes = [
        ndpointer(ctypes.c_double, flags="C_CONTIGUOUS"),
        ctypes.c_size_t,
    ]
    c_print_dists(matrix, len(matrix))


if __name__ == "__main__":
    dists = np.array([[0, 2, 1], [2, 0, 1], [1, 1, 0]], dtype="double")
    print_dists(dists)
    print(q_extend_single(dists, 2))
