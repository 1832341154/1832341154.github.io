import os
import  matplotlib.pyplot as plt
from thinkdsp import Signal, Spectrum
from thinkdsp import TriangleSignal
from thinkdsp import decorate
from playsound import playsound

signal = TriangleSignal(440)   #频率设置为440HZ
segment = signal.make_wave(duration=0.01 ,framerate=10000)#波形时长0.01s,帧数10000
plt.subplot (311)
segment.plot()

spectrum = segment.make_spectrum() 
spectrum.hs[0]
plt.subplot(312)
spectrum.make_wave().plot()

spectrum = segment.make_spectrum() 
spectrum.hs[0]=100
plt.subplot(313)
spectrum.make_wave().plot()
plt.show()