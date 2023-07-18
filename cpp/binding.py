"""Module: ctypes_test.py"""
import ctypes
import pathlib
import numpy as np
from numpy.ctypeslib import ndpointer
import os


def q_extend_single(dists: np.array, q: int):
    n = len(dists)
    p = os.path.dirname(__file__)+  "/libinvarientscpp.so"
    c_lib = ctypes.CDLL(p)
    c_q_extend_single = c_lib.q_extend_single
    c_q_extend_single.argtypes = [
        ndpointer(ctypes.c_double, flags="C_CONTIGUOUS"),
        ctypes.c_size_t,
        ctypes.c_size_t,
    ]
    c_q_extend_single.restype = ctypes.c_double
    c_q_extend_single(dists, n, q)

def direc():
    pass

if __name__ == "__main__":
    # Load the shared library into ctypes
    pass
