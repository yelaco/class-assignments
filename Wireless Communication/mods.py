import matplotlib.pylab as plt
import numpy as np
from bfsk import bfsk_mod
from bpsk import bpsk_mod


if __name__ == "__main__":
    bits = np.random.randint(2, size=100000)
    mod = input("Choose Modulation Type: ")
    freq_b = int(input("Input baseband frequency (Hz): "))
    freq_s = int(input("Input sampling frequency (Hz): "))
    freq_c = None
    s_bb = None
    t = None
    L = 16

    match mod.upper():
        case "ASK":
            modulated_signal, time_base = bask_mod()
        case "FSK":
            modulated_signal, time_base = bfsk_mod()
        case "PSK":
            freq_c = 800
            (s_bb, t) = bpsk_mod(bits, L)
        case _:
            print("Modulation type doesn't exist")
            exit(1)
    
    s = s_bb*np.cos(2*np.pi*freq_c*t/freq_s)
    fig1, axs = plt.subplots(2, 2)
    axs[0, 0].plot(t,s_bb) # baseband wfm zoomed to first 10 bits
    axs[0, 0].set_xlabel('t(s)');axs[0, 1].set_ylabel(r'$s_{bb}(t)$-baseband')
    axs[0, 1].plot(t,s) # transmitted wfm zoomed to first 10 bits
    axs[0, 1].set_xlabel('t(s)');axs[0, 1].set_ylabel('s(t)-with carrier')
    axs[0, 0].set_xlim(0,10*L);axs[0, 1].set_xlim(0,10*L)


        