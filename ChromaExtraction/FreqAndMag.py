import numpy as np

"""
Calculates Frequency and Magnitude from the complex frequency bins created in FFT
Maps each frequency to it's respetive magnitude.
"""
def FrequencyAndMagnitude(Y):
    N = Y.size
    Upper = N//2
    mf =[]
    for n in range(0,Upper):
        Re = np.real(Y[n])
        Im = np.imag(Y[n])

        magnitude = np.sqrt((Re**2)+(Im**2))
        frequency = (n/1024)*16000

        mf.append([frequency,magnitude])
    
    return mf