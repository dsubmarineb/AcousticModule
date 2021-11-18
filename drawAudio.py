import numpy as np
import matplotlib.pyplot as plt
import wave

# 11/08/21 - assumes wave file is 2-channel and 16-bit PCM

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

# Store data in an array and plot over time
def draw(fileName):

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

    # Calculate variables
    frames = len(left)
    duration = frames / samplerate
    sampleperiod = 1 / samplerate

    '''
    # Plot result - in 1 plot
    fig, ax = plt.subplots()
    plotrange = np.arange(0, duration, sampleperiod)
    ax.plot(plotrange, left, label='Left Channel')
    ax.plot(plotrange, right, label='Right Channel')
    ax.set(xlabel='Time (s)', ylabel='Amplitude', 
            title='Amplitude vs Time')
    ax.legend()
    '''

    plotrange = np.arange(0, duration, sampleperiod)
    

    # fig = plt.figure(1)
    # fig, ax = plt.subplots()

    # ax.plot(plotrange, left, label='Left Channel')
    # ax.plot(plotrange, right, label='Right Channel')
    # ax.set_xlabel('Time (s)')
    # ax.set_ylabel('Amplitude')
    # ax.set_title('Amplitude vs Time')
    # ax.legend()
    # ax.set_xlim(0, 8)
    # ax.set_ylim(-9000, 9000)
    # fig.savefig('1.png')

    plt.figure(1)
    plt.plot(plotrange, left, label='Left Channel')
    plt.plot(plotrange, right, label='Right Channel')
    plt.xlabel('Time(s)')
    plt.ylabel('Amplitude')
    plt.legend()
    plt.ylim(-9000, 9000)
    plt.title('Amplitude vs Time')
    plt.savefig('both.png')

    plt.figure(2)
    plt.plot(plotrange, left, label='Left Channel')
    plt.xlabel('Time(s)')
    plt.ylabel('Amplitude')
    plt.ylim(-9000, 9000)   
    plt.title('Left Channel')
    plt.savefig('left.png')


    plt.figure(3)
    plt.plot(plotrange, right, label='Right Channel', color='#ff7f0e')
    plt.xlabel('Time(s)')
    plt.ylabel('Amplitude')
    plt.ylim(-9000, 9000)
    plt.title('Right Channel')
    plt.savefig('right.png')
    

    # Close wave file
    wf.close()
    return

# For debugging:
draw("whistle.wav")