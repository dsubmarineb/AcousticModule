# Note for activating virtual environment:
# Authorize venv: Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
# Activate venv: .\.venv\Scripts\activate

import callback as cb
import blocking as bl
import drawAudio as da



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

# Prompt user for input file name
fileName = input("Enter file name: ")
if fileName == '':
    fileName = "whistle.wav"
'''
# Playing using blocking mode
print("Playing using blocking mode")
bl.blockingHelper(fileName)

# Play file using callback mode
print("Playing using callback mode")s
cb.callbackHelper(fileName)
'''
# Drawing plots of the file
da.draw(fileName)


