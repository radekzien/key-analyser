import librosa
import sys
import os
import numpy as np
from unittest.mock import patch

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from ProcessAudio import ProcessAudio

def test_ProcessAudio():
    sample_file = librosa.example("trumpet")

    result = ProcessAudio(sample_file)
    assert isinstance(result, np.ndarray)
    assert len(result) > 0

