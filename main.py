import ProcessAudio
import ChromaExtraction
from numpy import reshape, zeros, ceil, log2, array, arange, cos, pi

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
        n = arange(len(i))
        i *= 0.54 - 0.46 * cos(2 * pi * n / (len(i) - 1)) #Hamming window functions
        transformed_windows.append(ChromaExtraction.FastFourierTransform(i))
    print("completed FFT")