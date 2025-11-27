from numpy import reshape, zeros, ceil, log2, array, cos, pi, real, imag, sqrt
from cmath import exp

"""
Splits audio-time series into windows

Calculates the amount amount of samples per window given the window size in ms.
This number is used to divide the total number of samples in the data in order to obtain the number
of windows needed

The audio data is then reshaped to match the window format.
"""
def SplitToWindows(audio_data_resampled, sample_rate, window_size):
    samples_per_window = int(sample_rate * (window_size / 1000))#integer for slicing
    total_samples = len(audio_data_resampled) #Total amount of samples in data
    num_of_windows = total_samples // samples_per_window

    truncated_audio_data = audio_data_resampled[0:num_of_windows * samples_per_window] #Only keep full windows
    windows = reshape(truncated_audio_data, (num_of_windows, samples_per_window))

    return windows

"""
Pads windows so that they are a size = 2^n 
This is to ensure the recursive step in FFT executes correctly
"""
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

"""
Fast Fourier Transform:
Performs Cooley-Tukey 2-radix FFT to produce a frequency bin on each window represented as a complex array
"""
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

"""
Calculates Frequency and Magnitude from the complex frequency bins created in FFT
Maps each frequency to it's respetive magnitude.
"""
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

"""
Calculates the chroma bins by turning Frequencies into MIDI values and summing their magnitude to create a chroma vector
across each window
"""
def ChromaBins(mf):
    chroma = zeros(12)

    for n in range(0, len(mf)):
        if(mf[n][0] <= 0):
            continue
        midi = 69 + (12 * log2(mf[n][0]/440))
        bin = round(midi) % 12
        chroma[bin] = chroma[bin] + mf[n][1]
    
    return chroma

"""
Averages all Chroma Bins across each window into one global chroma feature
"""
def ExtractChroma(chroma_bins):
    chroma_feature = zeros(12)

    for chroma_vec in chroma_bins:
        chroma_feature += chroma_vec
    if len(chroma_bins) > 0:
        chroma_feature /= len(chroma_bins)
    return chroma_feature