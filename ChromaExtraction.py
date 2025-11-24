from numpy import reshape, zeros, ceil, log2, array, cos, pi, real, imag, sqrt
from cmath import exp

def SplitToWindows(audio_data_resampled, sample_rate, window_size):
    samples_per_window = int(sample_rate * (window_size / 1000))#integer for slicing
    total_samples = len(audio_data_resampled) #Total amount of samples in data
    num_of_windows = total_samples // samples_per_window

    truncated_audio_data = audio_data_resampled[0:num_of_windows * samples_per_window] #Only keep full windows
    windows = reshape(truncated_audio_data, (num_of_windows, samples_per_window))

    return windows

def padWindow(window):
    window = array(window, dtype=complex)
    N_orig = len(window)
        
    N = 2**int(ceil(log2(N_orig)))

    if N > N_orig:
        window_padded = zeros(N, dtype=complex)
        window_padded[:N_orig] = window
    else:
        window_padded = window.copy()
    
    return(window_padded)

def FastFourierTransform(window):
    if window.size == 0:
        return array([], dtype=complex)
    if window.size == 1:
        return window

    even = FastFourierTransform(window[::2])
    odd  = FastFourierTransform(window[1::2])

    Y = zeros(len(window), dtype=complex)
    for k in range(len(window)//2):
        twiddle = exp(-2j * pi * k / len(window))
        Y[k] = even[k] + twiddle * odd[k]
        Y[k + len(window)//2] = even[k] - twiddle * odd[k]

    return Y

def FrequencyAndMagnitude(Y):
    N = Y.size
    Upper = N//2
    mf =[]
    for n in range(0,Upper):
        Re = real(Y[n])
        Im = imag(Y[n])

        magnitude = sqrt((Re**2)+(Im**2))
        frequency = (n/1024)*16000

        mf.append([frequency,magnitude])
    
    return mf

def ChromaBins(mf):
    chroma = zeros(12)

    for n in range(0, len(mf)):
        if(mf[n][0] <= 0):
            continue
        midi = 69 + (12 * log2(mf[n][0]/440))
        bin = round(midi) % 12
        chroma[bin] = chroma[bin] + mf[n][1]
    
    return chroma