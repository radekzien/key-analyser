from ChromaExtraction.ChromaBins import ChromaBins
import numpy as np

"""Test chroma for single note A4"""
def test_ChromaBins():
    mf = [
        [440.0, 1.0]
    ]

    chroma = ChromaBins(mf)

    expected_bin = 9
    assert chroma[expected_bin] == 1.0
    assert np.sum(chroma) == 1.0