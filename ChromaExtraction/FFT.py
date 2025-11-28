import numpy as np

"""
Fast Fourier Transform:
Performs Cooley-Tukey 2-radix FFT using an iterative approach which utilisies bit reversal permutation
to produce a frequency bin on each window represented as a complex array
"""
def FastFourierTransform(window):
    N = window.shape[0]
    window_reordered = np.zeros(N, dtype=complex)

    if N < 1:
        return np.array([], dtype=complex)

    bits = int(np.log2(N))
    rev_indices = np.array([int(f'{i:0{bits}b}'[::-1], 2) for i in range(N)])#Reverse bits
    window_reordered = window[rev_indices]

    length = 2
    while length <= N:
        half = length // 2
        twiddle = np.exp(-2j * np.pi * np.arange(half) / length)
        for i in range(0, N, length):
            even = window_reordered[i:i+half]
            odd  = window_reordered[i+half:i+length] * twiddle
            window_reordered[i:i+length] = np.concatenate([even + odd, even - odd])
        length *= 2

    return window_reordered