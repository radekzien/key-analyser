import os
import sys
import numpy as np

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from ChromaExtraction import ExtractChroma

def test_ChromaExtraction():
    chromaBins = [np.array([1,2,3,4,5,6,7,8,9,10,11,12])]
    expected  = np.array([1,2,3,4,5,6,7,8,9,10,11,12])

    result = ExtractChroma(chromaBins)

    assert np.array_equal(result, expected)