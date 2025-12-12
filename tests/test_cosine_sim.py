import numpy as np
from numpy.linalg import norm
import sys
import os
import pytest

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from DetectKey import cosine_sim

def test_cosine():
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])

    expected = np.dot(a, b) / (norm(a) * norm(b))
    assert pytest.approx(cosine_sim(a, b), rel=1e-6) == expected