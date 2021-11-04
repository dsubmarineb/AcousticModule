import numpy as np
import matplotlib.pyplot as plt
import wave

def realDraw(data):
    left = []
    right = []
    for i in range(0,len(data),2):
        snip = data[i:i+2]
        snip = int.from_bytes(snip, byteorder='little')

        if i%4 == 0:
            left.append(snip)
        else:
            right.append(snip)
    return (left,right)

def draw(fileName):
    wf = wave.open(fileName, 'rb')

    frame_count = 1024
    data = wf.readframes(frame_count)
    print(len(data)/4==frame_count)
    left, right = ([], [])
    while (len(data)==frame_count*4):

        lr = realDraw(data)
        left.append
    # left.append(lr[0])
    # right.append(lr[1])
    left = lr[0]
    right = lr[1]

    print(lr)
    print(left)
    fig, ax = plt.subplots()
    ax.plot(range(0,len(left)), left)
    ax.plot(range(0,len(right)), right)

    plt.show()

    wf.close()
    return

draw("whistle.wav")