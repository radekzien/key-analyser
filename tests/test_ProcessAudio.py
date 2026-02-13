import librosa
import sys
import os
import numpy as np
from unittest.mock import patch

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from Pipeline.ProcessAudio import ProcessAudio

def test_ProcessAudioWithSound():
    sample_file = librosa.example("trumpet") #Test with audio sample

    result = ProcessAudio(sample_file)
    assert isinstance(result, np.ndarray) #Test output
    assert len(result) > 0



@patch("ProcessAudio.librosa.load")
@patch("ProcessAudio.librosa.resample")
@patch("ProcessAudio.signal.lfilter")
def test_ProcessAudio(mock_lfilter, mock_resample, mock_load): #UNIT TEST

    #Mock values
    fake_audio = np.ones(44100)
    mock_load.return_value = (fake_audio, 44100)
    mock_lfilter.return_value = fake_audio * 0.5
    mock_resample.return_value = np.ones(16000) * 0.25

    result = ProcessAudio("dummy.wav")

    mock_load.assert_called_once_with("dummy.wav")
    mock_lfilter.assert_called_once()
    mock_resample.assert_called_once_with(mock_lfilter.return_value, orig_sr=44100, target_sr=16000)
    assert isinstance(result, np.ndarray)
    assert result.shape == (16000,)
    assert np.allclose(result, 0.25)

