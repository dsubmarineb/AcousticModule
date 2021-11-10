# Implement DFT Transformation
import numpy as np
import math
import wave


# Separate data into left and right channels
def readData(data):
    left, right = [], []
    for i in range(0,len(data),2):
        snip = data[i:i+2]
        snip = int.from_bytes(snip, byteorder='little')
    
        if snip > pow(2, 15):
            snip -= pow(2, 16)
        if i%4 == 0:
            left.append(snip)
        else:
            right.append(snip)
    return (left,right)


def dft(fileName):

    # Redundant code from drawAudio:
    # - get separate array of left and right chennel data   
                                                   
    # Open wave file
    wf = wave.open(fileName, 'rb')

    # Get variables
    channels    = wf.getnchannels()
    samplewidth = wf.getsampwidth()
    samplerate  = wf.getframerate()

    # Set data chunk size - amount to be handled each read
    frame_count = 1024

    # Read in data and separate into 2 channels
    data = wf.readframes(frame_count)
    left, right = ([], [])
    dataSize = frame_count * samplewidth * channels

    while (len(data) == dataSize): # loop until end of file

        lr = readData(data) 
        left.extend(lr[0])
        right.extend(lr[1])
        data = wf.readframes(frame_count)
    
    x_n = left
    PI = math.pi
    e = math.e
    i = 1j
    N = len(x_n)
    print(N)

    x_k = [0] * len(x_n)
    for k in range(len(x_k)):
        x_k[k] = sum([(x_n[n] * math.cos(2*PI*k*n/N)) for n in range(N)])
        print(x_k[k])
    x_t = left

    x_k = x_t * []
    print('hi')
    
dft("whistle.wav")