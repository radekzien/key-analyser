from numpy import reshape, zeros, ceil, log2, array, arange, cos, pi
from cmath import exp

def SplitToWindows(audio_data_resampled, sample_rate, window_size):
    samples_per_window = int(sample_rate * (window_size / 1000))#integer for slicing
    total_samples = len(audio_data_resampled) #Total amount of samples in data
    num_of_windows = total_samples // samples_per_window

    truncated_audio_data = audio_data_resampled[0:num_of_windows * samples_per_window] #Only keep full windows
    windows = reshape(truncated_audio_data, (num_of_windows, samples_per_window))

    return windows

def FastFourierTransform(window):
    window = array(window, dtype=complex)
    N_orig = len(window)

    if N_orig == 0:
        return array([], dtype=complex)
    if N_orig == 1:
        return window
    
    N = 2**int(ceil(log2(N_orig)))

    if N > N_orig:
        window_padded = zeros(N, dtype=complex)
        window_padded[:N_orig] = window
    else:
        window_padded = window.copy()

    even = FastFourierTransform(window_padded[::2])
    odd  = FastFourierTransform(window_padded[1::2])

    Y = zeros(len(window_padded), dtype=complex)
    for k in range(len(window_padded)//2):
        twiddle = exp(-2j * pi * k / len(window_padded))
        Y[k] = even[k] + twiddle * odd[k]
        Y[k + len(window_padded)//2] = even[k] - twiddle * odd[k]

    return Y