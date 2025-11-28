import numpy as np
from ChromaExtraction.PadWindow import padWindow

def test_padWindow():
    fakeWindow = np.ones(5)
    result = padWindow(fakeWindow)

    expected = np.array([1,1,1,1,1,0,0,0], dtype=complex) #Padded with zero to size 8 as 8 is a power of 2
    assert np.array_equal(result, expected)