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

signal = SawtoothChirp(start = 220,end =440)
wave = signal.make_wave(duration = 1,framerate=10000)
wave.apodize()
wave.make_audio()
sp=wave.make_spectrogram(512).plot(high= 5000)#每个片段的采样数量，这里选用512，这是考虑到采样数量的幂指数时FFT效率更高
decorate(xlabel = 'Time(s)',ylabel = 'Frequency(HZ)')#x轴为时间，y轴为频率
wave.plot()
spect = signal.make_wave()
spect.write('output1.wav')
playsound('output.wav')
plt.show()