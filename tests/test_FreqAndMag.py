import numpy as np
from ChromaExtraction.FreqAndMag import FrequencyAndMagnitude

"""Correctly detects frequency of a known sine wave"""
def test_FreqAndMag():
    fs = 16000
    N = 1024
    t = np.arange(N) / fs

    f_test = 1000
    x = np.sin(2 * np.pi * f_test * t)

    Y = np.fft.fft(x)

    result = np.array(FrequencyAndMagnitude(Y))
    freqs = result[:, 0]
    mags = result[:, 1]

    peak_freq = freqs[np.argmax(mags)]

    assert abs(peak_freq - f_test) < 20