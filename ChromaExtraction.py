import numpy

def SplitToWindows(audio_data_resampled, sample_rate, window_size):
    samples_per_window = int(sample_rate * (window_size / 1000))#integer for slicing
    total_samples = len(audio_data_resampled) #Total amount of samples in data
    num_of_windows = total_samples // samples_per_window

    truncated_audio_data = audio_data_resampled[0:num_of_windows * samples_per_window] #Only keep full windows
    windows = numpy.reshape(truncated_audio_data, (num_of_windows, samples_per_window))

    return windows