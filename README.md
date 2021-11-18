# AcousticModule
Help enhance understanding of acoustic wave

10/05/2021
- installed "pyaudio" using "pipwin" because "pip install pyaudio" didn't work
- package is installed in .venv folder which is ignored (.gitignore - environment)

11/17/2021
- play .wav file in blocking mode or callback mode (blocking.py and callback.py)
- draw amplitude over time (drawAudio.py)
- still testing dft (using numpy.fft.fft)

![left](https://user-images.githubusercontent.com/60358639/142357416-9b091f25-1f8c-4d8c-beb6-1ca1889e71ef.png)

(1) Left Channel

![right](https://user-images.githubusercontent.com/60358639/142357424-490f588e-2796-480d-8eb2-34fcee0a8139.png)

(2) Right Channel

![both](https://user-images.githubusercontent.com/60358639/142357428-e148facb-ad6c-4f2b-84f0-d1f5ce6e1d6d.png)

(3) Both Channels

[3 large waves for 3 whistles, and last small wave is mouse-click to end recording]
