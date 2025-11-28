import numpy as np
"""
Pads windows so that they are a size = 2^n 
This is to ensure the recursive step in FFT executes correctly
"""
def padWindow(window):
    window = np.array(window, dtype=complex)
    N_orig = len(window)
        
    N = 2**int(np.ceil(np.log2(N_orig)))

    if N > N_orig:
        window_padded = np.zeros(N, dtype=complex)
        window_padded[:N_orig] = window
    else:
        window_padded = window.copy()
    
    return(window_padded)