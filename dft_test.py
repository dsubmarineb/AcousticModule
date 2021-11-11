import numpy as np
import matplotlib.pyplot as plt

n = 5
t= np.arange(0, n, 0.01)
f_t = np.sin(2*np.pi*t)

sp = np.fft.fft(f_t)
freq = np.fft.fftfreq(t.shape[-1])*100

fig, axs = plt.subplots(2)
axs[0].plot(t, f_t)
axs[1].plot(freq, abs(sp))

plt.show()

'''
Note:

Showing FFT of f_t in 1/100 scale -> step size in t is 0.01
For function f_t = sin(2PI*t), I expect a peak at 1 (not 0.01)
I want to perform DFT on 0 through 1 at 0.01 interval (looking at 0.01 Hz, 0.02 Hz, ... , 1.0 Hz)


'''