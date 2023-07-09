"""Module that tests the code"""

import sys
import os

# Add parent_directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import invarients as inva
import graph_tools as glt



def test_answer():
    assert 3 == 3