# https://people.csail.mit.edu/hubert/pyaudio/docs/
"""PyAudio Example: Play a wave file."""

import pyaudio
import wave
import sys

def blockingHelper(fileName):
    CHUNK = 1024

    wf = wave.open(fileName, 'rb')

    # instantiate PyAudio (1)
    p = pyaudio.PyAudio()

    # open stream (2)
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)

    # read data
    data = wf.readframes(CHUNK)

    # play stream (3)
    while len(data) > 0:
        stream.write(data)
        data = wf.readframes(CHUNK)

    # stop stream (4)
    stream.stop_stream()
    stream.close()
    wf.close()

    # close PyAudio (5)
    p.terminate()