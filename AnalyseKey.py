import ProcessAudio
import DetectKey
from ChromaExtraction import (
    ChromaBins,
    ExtractChroma,
    FastFourierTransform,
    FrequencyAndMagnitude,
    padWindow,
    SplitToWindows
)
import numpy as np
def AnalyseKey(audioFile):
    #Preprocessing
    processedAudio = ProcessAudio.ProcessAudio(audioFile)
    windows = SplitToWindows(processedAudio, 16000, 750)

    #Fast Fourier Transform on windows
    transformed_windows = []
    for i in windows:
        i_padded = padWindow(i)
        n = np.arange(len(i_padded))
        i_padded *= 0.54 - 0.46 * np.cos(2 * np.pi * n / (len(i_padded)-1)) #Hamming window functions
        transformed_windows.append(FastFourierTransform(i_padded))

    freq_and_mag = []
    for i in transformed_windows:
        freq_and_mag.append(FrequencyAndMagnitude(i))

    chroma_bins = []
    for i in freq_and_mag:
        chroma_bins.append(ChromaBins(i))

    chroma_feature = ExtractChroma(chroma_bins)
    
    return(DetectKey.detectKey(chroma_feature))