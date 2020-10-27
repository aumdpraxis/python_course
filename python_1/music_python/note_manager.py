from math import pow
import numpy as np
import time

from pyaudio import PyAudio # sudo apt-get install python{,3}-pyaudio

try:
    from itertools import izip
except ImportError: # Python 3
    izip = zip
    xrange = range

NOTES={
    'rest':0,
    'C':16.35,
    'C#':17.32,
    'D':18.35,
    'Eb':19.45,
    'E':20.60,
    'F':21.83,
    'F#':23.12,
    'G':24.5,
    'G#':25.96,
    'A':27.50,
    'Bb':29.14,
    'B':30.87
}

TYPE={
    'O':4,
    'B':2,
    'N':1,
    'C':1/2,
    'SC':1/4,
    'F':1/8,
    'SF':1/16
}

TYPE['O.']=TYPE['O']*1.5
TYPE['B.']=TYPE['B']*1.5
TYPE['N.']=TYPE['N']*1.5
TYPE['C.']=TYPE['C']*1.5
TYPE['SC.']=TYPE['SC']*1.5
TYPE['F.']=TYPE['F']*1.5
TYPE['SF.']=TYPE['SF']*1.5

class Note_Manager:
    def __init__(self):
        self.py_audio = PyAudio()

    def init_stream(self,sample_rate=22050):
        self.stream = self.py_audio.open(format=self.py_audio.get_format_from_width(1), # 8bit
                    channels=1, # mono
                    rate=sample_rate,
                    output=True)

    def end_stream(self):
        self.stream.stop_stream()
        self.stream.close()
        self.py_audio.terminate()

    def run(self,_note,_octave,_time):
        self.sine_tone(
            frequency=NOTES[_note]*pow(2,_octave),
            duration=TYPE[_time]*0.35, 
            volume=0.8, 
            sample_rate=22050 
        )
        time.sleep(TYPE[_time]*0.35)

    def sine_tone(self,frequency, duration, volume=1, sample_rate=22050):
        n_samples = int(sample_rate * duration)
        dots = np.arange(n_samples)
        signal = (volume *np.sin(2*np.py_audioi*frequency*dots/sample_rate)*0x7f+0x80).astype(int)
        for buf in izip(signal): # write several samples at a time
            self.stream.write(bytes(bytearray(buf)))
        # fill remainder of frameset with silence
        self.stream.write(b'\x80' * int(sample_rate/256))
