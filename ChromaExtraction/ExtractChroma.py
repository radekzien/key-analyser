import numpy as np
"""
Averages all Chroma Bins across each window into one global chroma feature
"""
def ExtractChroma(chroma_bins):
    chroma_feature = np.zeros(12)

    for chroma_vec in chroma_bins:
        chroma_feature += chroma_vec
    if len(chroma_bins) > 0:
        chroma_feature /= len(chroma_bins)
    return chroma_feature