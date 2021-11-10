import numpy as np
import matplotlib.pyplot as plt

n = 256
t= np.arange(n)
sp = np.fft.fft(np.sin(t), n)
sp2 = np.fft.fft(np.sin(2*t), n)
sp3 = np.fft.fft(np.sin(3*t), n)
np.fft.fftshift(sp)
print(sp[128])
freq = np.fft.fftfreq(n)
# plt.plot(freq, sp.real, label = "Real")
# plt.plot(freq, sp.imag, label = "Imaginary")
plt.plot(freq, np.abs(sp), label = "sin(t)")
plt.plot(freq, np.abs(sp2), label = "sin(2t)")
plt.plot(freq, np.abs(sp3), label = "sin(3t)")
plt.legend()
plt.show()