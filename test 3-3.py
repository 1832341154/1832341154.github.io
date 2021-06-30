import os
import  matplotlib.pyplot as plt
import numpy as np
from thinkdsp import Signal
from thinkdsp import SawtoothSignal
from thinkdsp import decorate
from playsound import playsound
from thinkdsp import Chirp
from thinkdsp import normalize,unbias

PI2 = 2 * np.pi

class SawtoothChirp(Chirp):
    """Represents a sawtooth signal with varying frequency."""

    def evaluate(self, ts):
        freqs = np.linspace(self.start, self.end, len(ts))
        dts = np.diff(ts, prepend=0)
        dphis = PI2 * freqs * dts
        phases = np.cumsum(dphis)
        cycles = phases / PI2
        frac, _ = np.modf(cycles)
        ys =  normalize(unbias(frac), self.amp)
        return ys


plt.subplot(211)
signal = SawtoothChirp(start =500,end = 1000)   #频率从500HZ扫到1000HZ
wavel = signal.make_wave(duration=1,framerate = 20000)
wavel.make_audio()
wavel.make_spectrum().plot()
decorate(xlabel = 'Frequency(Hz)')

plt.subplot(212)
signal = SawtoothChirp(start =2500,end = 3000)  #频率从2500HZ扫到3000HZ
wavel = signal.make_wave(duration=1,framerate = 20000) #1s抽样20000次
wavel.make_audio()
wavel.make_spectrum().plot()    #生成频谱图
decorate(xlabel = 'Frequency(Hz)')
plt.show()
