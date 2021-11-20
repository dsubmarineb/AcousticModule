# AcousticModule
Python program for having fun with wave file
(11/20/21: works with 16 bit 2-Channel with 44100Hz file - sample audio included)

## Major Functions:
- main.py: call other functions
- blocking.py and callback.py: play wave file
- drawAudio.py: draws amplitude vs time graph
- dft.py: draws amplitude vs frequency graph (DFT)

## List of Python packages:
- numpy:calculate numbers, generate wave for test
- pyaudio: play wave file
- matplotlib: draw plots





#### Log:

10/05/2021
- installed "pyaudio" using "pipwin" because "pip install pyaudio" didn't work
- package is installed in .venv folder which is ignored (.gitignore - environment)

11/17/2021
- play .wav file in blocking mode or callback mode (blocking.py and callback.py)
- draw amplitude over time (drawAudio.py)
- still testing dft (using numpy.fft.fft)

![left](https://user-images.githubusercontent.com/60358639/142357416-9b091f25-1f8c-4d8c-beb6-1ca1889e71ef.png)

*(1) Left Channel*

![right](https://user-images.githubusercontent.com/60358639/142357424-490f588e-2796-480d-8eb2-34fcee0a8139.png)

*(2) Right Channel*

![both](https://user-images.githubusercontent.com/60358639/142357428-e148facb-ad6c-4f2b-84f0-d1f5ce6e1d6d.png)

*(3) Both Channels*

[3 large waves for 3 whistles, and 1 small wave for mouse click]
