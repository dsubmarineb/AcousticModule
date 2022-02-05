import numpy as np
import matplotlib.pyplot as plt

n = 5
t= np.arange(0, n, 0.01)
f_t = np.sin(2*np.pi*t)
f_t2 = np.sin(1.5*2*np.pi*t)
f_t3 = np.sin(2*2*np.pi*t)

# applying from fftfreq definition
n = f_t.size
timestep = 0.01
sp = np.fft.fft(f_t)
freq = np.fft.fftfreq(t.shape[-1], d=0.01)

sp2 = np.fft.fft(f_t2)
sp3 = np.fft.fft(f_t3)

fig, axs = plt.subplots(2)
axs[0].plot(t, f_t)
axs[0].plot(t, f_t2)
axs[0].plot(t, f_t3)
axs[1].plot(freq, abs(sp))
axs[1].plot(freq, abs(sp2))
axs[1].plot(freq, abs(sp3))
axs[1].set(xlim=(-5, 5), xticks=np.arange(-5,5))

plt.show()