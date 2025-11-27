import ProcessAudio
import ChromaExtraction
from numpy import reshape, zeros, ceil, log2, array, arange, cos, pi, fft

SampleAudio = [
    "SampleAudio/Classicals.de - Chopin - Albumleaf, B. 151.mp3",
    "SampleAudio/Classicals.de - Chopin - Andantino 'Spring' B. 117.mp3",
    "SampleAudio/Classicals.de - Chopin - Etude Op. 10 no. 12 in C minor 'Revolutionary'.mp3",
    "SampleAudio/Classicals.de - Chopin - Fantasia Impromptu Op. posth. 66.mp3"
]

if __name__ == "__main__":
    #Preprocessing
    processedAudio = ProcessAudio.ProcessAudio(SampleAudio[3])
    windows = ChromaExtraction.SplitToWindows(processedAudio, 16000, 100)
    print(windows.shape)

    #Fast Fourier Transform on windows
    transformed_windows = []
    for i in windows:
        i_padded = ChromaExtraction.padWindow(i)
        n = arange(len(i_padded))
        i_padded *= 0.54 - 0.46 * cos(2 * pi * n / (len(i) - 1)) #Hamming window functions
        transformed_windows.append(ChromaExtraction.FastFourierTransform(i_padded))
        #transformed_windows.append(fft.fft(i_padded, 1024))
    print("completed FFT")

    freq_and_mag = []
    for i in transformed_windows:
        freq_and_mag.append(ChromaExtraction.FrequencyAndMagnitude(i))
    print("Extracted Frequencies and Magnitudes")

    chroma_bins = []
    for i in freq_and_mag:
        chroma_bins.append(ChromaExtraction.ChromaBins(i))
    print("Extracted Chroma Bins")

    chroma_feature = ChromaExtraction.ExtractChroma(chroma_bins)
    print(chroma_feature)