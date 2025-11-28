import numpy as np

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
    windows = np.reshape(truncated_audio_data, (num_of_windows, samples_per_window))

    return windows