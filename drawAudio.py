import numpy as np
import matplotlib
import wave

def draw(fileName):

    wf = wave.open(fileName, 'rb')

    print(wf)
    print(wf.getfp())

    frame_count = 1024
    data = wf.readframes(frame_count)
    print(type(data))
    print(len(data))
    print(data)
    data = wf.readframes(frame_count)
    print(data)
    
    wf.close()
    return