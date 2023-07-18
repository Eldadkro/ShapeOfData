"""Module: ctypes_test.py"""
import ctypes
import pathlib

if __name__ == "__main__":
    # Load the shared library into ctypes
    p = pathlib.Path().absolute() / "libtest.so"
    c_lib = ctypes.CDLL(p)
    c_lib.display()
