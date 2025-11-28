import numpy as np

"""
Calculates the chroma bins by turning Frequencies into MIDI values and summing their magnitude to create a chroma vector
across each window
"""
def ChromaBins(mf):
    chroma = np.zeros(12)

    for n in range(0, len(mf)):
        if(mf[n][0] <= 0):
            continue
        midi = 69 + (12 * np.log2(mf[n][0]/440))
        bin = round(midi) % 12
        chroma[bin] = chroma[bin] + mf[n][1]
    
    return chroma