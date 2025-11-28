import numpy as np
from numpy.testing import assert_array_almost_equal
from ChromaExtraction.FFT import FastFourierTransform

def test_fft_empty():
    result = FastFourierTransform(np.array([]))
    expected = np.array([], dtype=complex)
    assert_array_almost_equal(result, expected)

def test_fft_single_element():
    result = FastFourierTransform(np.array([5+2j]))
    expected = np.array([5+2j])
    assert_array_almost_equal(result, expected)

def test_fft_real_input():
    x = np.array([1, 2, 3, 4], dtype=complex)
    result = FastFourierTransform(x)
    expected = np.fft.fft(x)
    assert_array_almost_equal(result, expected)