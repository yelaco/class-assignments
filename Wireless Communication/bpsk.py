def bpsk_mod(ak,L):
    """
    Function to modulate an incoming binary stream using BPSK (baseband)
    Parameters:
    ak : input binary data stream (0's and 1's) to modulate
    L : oversampling factor (Tb/Ts)
    Returns:
    (s_bb,t) : tuple of following variables
    s_bb: BPSK modulated signal(baseband) - s_bb(t)
    t : generated time base for the modulated signal
    """
    from scipy.signal import upfirdn
    import numpy as np
    s_bb = upfirdn(h=[1]*L, x=2*ak-1, up = L) # NRZ encoder
    t = np.arange(start = 0,stop = len(ak)*L) #discrete time base
    return (s_bb,t)