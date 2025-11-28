import librosa
from scipy import signal

def ProcessAudio(filePath):
    #Load file and convert into frequency-time series
    audio_data,sr = librosa.load(filePath)

    #Calculate Wn value for filtering
    wn = 5000/(sr/2)
    b,a = signal.butter(6, wn, 'low', False)
    
    #Apply filter
    audio_data_filtered = signal.lfilter(b, a, audio_data)

    #Resample to 16kHz
    audio_data_resampled = librosa.resample(audio_data_filtered, orig_sr=sr, target_sr=16000)
    
    return audio_data_resampled