import numpy


def SplitToWindows(audio_data_resampled, sample_rate, window_size):
    samples_per_window = int(sample_rate * (window_size / 1000))
    total_samples = len(audio_data_resampled)
    num_of_windows = int(total_samples // samples_per_window)

    x = num_of_windows * samples_per_window
    truncated_audio_data = audio_data_resampled[0:x]
    windows = numpy.reshape(truncated_audio_data, (num_of_windows, samples_per_window))

    return windows