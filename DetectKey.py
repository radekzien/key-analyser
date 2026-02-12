import numpy as np
from numpy.linalg import norm
from KeyProfiles import own_profiles

#Index positions == index posiitons of key profiles in krumhansl/own profiles
keys = {
    "C major" : ["F Major", "G Major", "A Minor"],
    "C# major/Db major" : ["F#/Gb Major", "Ab Major", "Bb Minor"],
    "D major" : ["G Major", "A Major", "B Minor"],
    "Eb major" : ["Ab Major", "Bb Major", "C Minor"],
    "E major/Fb major" : ["A Major", "B Major", "C#/Db Minor"],
    "F major" : ["Bb Major", "C Major", "D Minor"],
    "F# major/Gb major" : ["B Major", "C#/Db Major", "Eb Minor"],
    "G major" : ["C Major", "D Major", "E Minor"],
    "Ab major" : ["C#/Db Major", "Eb Major", "F Minor"],
    "A major" : ["D Major", "E Major", "F#/Gb Minor"],
    "Bb major" : ["Eb Major" , "F Major", "G Minor"],
    "B major" : ["E Major", "F#/Gb Major", "Ab Minor"],

    "C minor" : ["F Minor", "G Major", "Eb Major"],
    "C# minor/Db minor" : ["F#/Gb Minor", "Ab Major", "E Major"],
    "D minor" : ["G Minor", "A Major", "F Major"],
    "Eb minor" : ["Ab Minor", "Bb Major", "Gb Major"],
    "E minor/Fb minor" : ["A Minor", "B Major", "G Major"],
    "F minor" : ["Bb Minor", "C Major", "Ab Major"],
    "F# minor/Gb minor" : ["B Minor", "C#/Db Major", "A Major"],
    "G minor" : ["C Minor", "D Major", "Bb Major"],
    "Ab minor" : ["Db Minor", "Eb Major", "Cb Major"],
    "A minor" : ["D Minor", "E Major", "C Major"],
    "Bb minor" : ["Eb Minor", "F Major", "Db Major"],
    "B minor" : ["E Minor", "F#/Gb Major", "D Major"]
}

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
