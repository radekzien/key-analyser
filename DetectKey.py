import numpy as np
from numpy.linalg import norm
from KeyProfiles import krumhansl_profiles, own_profiles

keys = [
    "C major",
    "C# major/Db major",
    "D major",
    "Eb major",
    "E major/Fb major",
    "F major",
    "F# major/Gb major",
    "G major",
    "Ab major",
    "A major",
    "Bb major",
    "B major",
    "C minor",
    "C# minor/Db minor",
    "D minor",
    "Eb minor",
    "E minor/Fb minor",
    "F minor",
    "F# minor/Gb minor",
    "G minor",
    "Ab minor",
    "A minor",
    "Bb minor",
    "B minor"
]

def cosine_sim(chroma, key):
    similarity = np.dot(chroma, key) / (norm(chroma) * norm(key))

    return similarity

def detectKey(chroma):
    similarities = []
    for i in krumhansl_profiles.profiles.values():
        similarities.append(cosine_sim(chroma, i))

    similarities = np.array(similarities)

    key_index = np.argmax(similarities)
    key = keys[key_index]
    return(key)
