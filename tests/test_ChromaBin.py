import os
import sys
import numpy as np

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from ChromaExtraction import ChromaBins

"""Test chroma for single note A4"""
def test_ChromaBin():
    mf = [
        [440.0, 1.0]
    ]

    chroma = ChromaBins(mf)

    expected_bin = 9
    assert chroma[expected_bin] == 1.0
    assert np.sum(chroma) == 1.0