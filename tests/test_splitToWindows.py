import numpy
from ChromaExtraction.SplitToWindows import SplitToWindows

def test_splitToWindows():
    fake_Data = numpy.ones(16000)
    fake_sr = 16000
    fake_window_size = 100

    result = SplitToWindows(fake_Data, fake_sr, fake_window_size)

    assert result.shape == (10, 1600)