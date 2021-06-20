import os
import  matplotlib.pyplot as plt
from thinkdsp import Signal
from thinkdsp import SquareSignal
from thinkdsp import decorate
from playsound import playsound

Signal = SquareSignal(1500).make_wave(duration=1,framerate=10000)
plt.subplot(211)
Signal.make_spectrum().plot()
decorate(xlabel='Frequency(Hz)')

signal = SquareSignal(1500)   
duration = signal.period*3   #时域输出三个周期
segment = signal.make_wave(duration ,framerate=10000)#
plt.subplot (212)
spect = signal.make_wave()
spect.write('output1.wav')
playsound('output1.wav')
segment.plot()   #输出方波波形
decorate(xlabel='Time(s)')

plt.show()