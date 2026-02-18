import numpy as np
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from Pipeline.DetectKey import detectKey
from KeyProfiles import krumhansl_profiles

def test_detectKey():
    chroma_to_test = list(krumhansl_profiles.profiles.values())[0]
    
    assert detectKey(chroma_to_test) == "C major"