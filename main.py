import ProcessAudio
import ChromaExtraction

SampleAudio = [
    "SampleAudio/Classicals.de - Chopin - Albumleaf, B. 151.mp3",
    "SampleAudio/Classicals.de - Chopin - Andantino 'Spring' B. 117.mp3",
    "SampleAudio/Classicals.de - Chopin - Etude Op. 10 no. 12 in C minor 'Revolutionary'.mp3",
    "SampleAudio/Classicals.de - Chopin - Fantasia Impromptu Op. posth. 66.mp3"
]

if __name__ == "__main__":
    processedAudio = ProcessAudio.ProcessAudio(SampleAudio[1])
    windows = ChromaExtraction.SplitToWindows(processedAudio, 16000, 100)
    print(windows)