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

SampleAudio = [
    "SampleAudio/Classicals.de - Chopin - Albumleaf, B. 151.mp3", #B Major
    "SampleAudio/Classicals.de - Chopin - Andantino 'Spring' B. 117.mp3",
    "SampleAudio/Classicals.de - Chopin - Etude Op. 10 no. 12 in C minor 'Revolutionary'.mp3", #C Minor
    "SampleAudio/Classicals.de - Chopin - Fantasia Impromptu Op. posth. 66.mp3",
]

if __name__ == "__main__":
    #Preprocessing
    processedAudio = ProcessAudio.ProcessAudio(SampleAudio[0])
    windows = SplitToWindows(processedAudio, 16000, 500)
    print(windows.shape)

    #Fast Fourier Transform on windows
    transformed_windows = []
    for i in windows:
        i_padded = padWindow(i)
        n = np.arange(len(i_padded))
        i_padded *= 0.54 - 0.46 * np.cos(2 * np.pi * n / (len(i_padded)-1)) #Hamming window functions
        transformed_windows.append(FastFourierTransform(i_padded))
    print("completed FFT")

    freq_and_mag = []
    for i in transformed_windows:
        freq_and_mag.append(FrequencyAndMagnitude(i))
    print("Extracted Frequencies and Magnitudes")

    chroma_bins = []
    for i in freq_and_mag:
        chroma_bins.append(ChromaBins(i))
    print("Extracted Chroma Bins")

    chroma_feature = ExtractChroma(chroma_bins)
    
    print(DetectKey.detectKey(chroma_feature))