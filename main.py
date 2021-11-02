# Note for activating virtual environment:
# Authorize venv: Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
# Activate venv: .\.venv\Scripts\activate

import pyaudio
import wave
import callback as cb
import time
import blocking as bl



'''
Overall steps:
1. prompt user for input or select audio input mode (assume input is .wav file)
2. read in audio file
3. plot audio file in matplotlib
    3-1. plot amplitude vs time
    3-2. plot amplitude vs frequency (Fourier transform)
    * Q. How can I represent change in Fourier Transform over time?
4. ???
'''

fileName = input("Enter file name: ")
if fileName == '':
    fileName = "whistle.wav"

cb.callbackHelper(fileName)
bl.blockingHelper(fileName)




