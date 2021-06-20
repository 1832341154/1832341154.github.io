import os
import  matplotlib.pyplot as plt
from thinkdsp import Signal, Spectrum
from thinkdsp import TriangleSignal
from thinkdsp import SquareSignal
from thinkdsp import SawtoothSignal
from thinkdsp import decorate
from playsound import playsound

def filter_spectrum(spectrum):
    spectrum.hs[1:] /= spectrum.fs[1:]
    spectrum.hs[0] = 0
    
signal1 = TriangleSignal(440).make_wave(duration=0.5)  #频率设置为440HZ#波形时长0.01s,帧数10000
signal1.make_audio()
signal2 = SquareSignal(440).make_wave(duration=0.5) 
signal2.make_audio()
signal3 = SawtoothSignal(440).make_wave(duration=0.5) 
signal3.make_audio()

plt.subplot(311) #显示三角波频谱
Spectrum = signal1.make_spectrum()
Spectrum.plot(high = 10000,color = 'red')
filter_spectrum(Spectrum)
Spectrum.scale(440)
Spectrum.plot(high = 10000)
decorate(xlabel = 'Frequency1(HZ)')

plt.subplot(312) #显示方波频谱
Spectrum = signal2.make_spectrum()
Spectrum.plot(high = 10000,color = 'red')
filter_spectrum(Spectrum)
Spectrum.scale(440)
Spectrum.plot(high = 10000)
decorate(xlabel = 'Frequency2(HZ)')

plt.subplot(313) #显示锯齿波频谱
Spectrum = signal3.make_spectrum()
Spectrum.plot(high = 10000,color = 'red')
filter_spectrum(Spectrum)
Spectrum.scale(440)
Spectrum.plot(high = 10000)
decorate(xlabel = 'Frequency3(HZ)')

plt.show()
