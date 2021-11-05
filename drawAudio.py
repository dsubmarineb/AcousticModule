import numpy as np
import matplotlib.pyplot as plt
import wave

def readData(data):
    left = []
    right = []
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

def draw(fileName):
    wf = wave.open(fileName, 'rb')

    channels = wf.getnchannels()
    samplewidth = wf.getsampwidth()
    samplerate = wf.getframerate()
    frames = wf.getnframes()

    frame_count = 1024

    data = wf.readframes(frame_count)
    left, right = ([], [])
    while (len(data)==frame_count*samplewidth*channels):

        lr = readData(data) 
        left.extend(lr[0])
        right.extend(lr[1])
        data = wf.readframes(frame_count)
        # print(len(data))

    fig, ax = plt.subplots()

    ax.plot(left, label='Left Channel', linewidth=0.1)
    ax.plot(right, label='Right Channel', linewidth=0.1)
    ax.set(xlabel='Frames', ylabel='Amplitude', 
            title='Amplitude vs Time')
    ax.legend()

    plt.show()

    wf.close()
    return

# draw("whistle.wav")