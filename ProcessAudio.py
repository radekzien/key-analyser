import librosa
from scipy import signal
def ProcessAudio(filePath):
    #Load file and convert into frequency-time series
    audio_data,sr = librosa.load(filePath)
    print(f"Raw data: {audio_data.shape}")
    print(sr)

    #Calculate Wn value for filtering
    wn = 5000/(sr/2)
    b,a = signal.butter(6, wn, 'low', False)
    
    #Apply filter
    audio_data_filtered = signal.lfilter(b, a, audio_data)
    print(f"Filtered data: {audio_data_filtered.shape}")

    #Resample to 16kHz
    audio_data_resampled = librosa.resample(audio_data_filtered, orig_sr=sr, target_sr=16000)
    print(f"Resampled data: {audio_data_resampled.shape}")
    
    return audio_data_resampled

if __name__ == '__main__':
    ProcessAudio("SampleAudio/Classicals.de - Chopin - Etude Op. 10 no. 12 in C minor 'Revolutionary'.mp3")