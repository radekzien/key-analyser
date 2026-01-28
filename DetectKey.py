import numpy as np
from numpy.linalg import norm
from KeyProfiles import krumhansl_profiles, own_profiles

#Index positions == index posiitons of key profiles in krumhansl/own profiles
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

#Calcualtes vector similarity between chroma and each key
def cosine_sim(chroma, key):
    similarity = np.dot(chroma, key) / (norm(chroma) * norm(key))

    return similarity

"""
Goes through each of the 24 key profiles, calculating the cosine similarity between each profile
and the chroma. Each similairty is put into an array. The index of the max value is found, and then
this index is used to retrieve the key based on the array of key names.
"""
def detectKey(chroma):
    similarities = []
    for i in own_profiles.profiles.values():
        similarities.append(cosine_sim(chroma, i))

    similarities = np.array(similarities)

    key_index = np.argmax(similarities)
    key = keys[key_index]
    return(key)
