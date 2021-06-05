import os
import matplotlib.pyplot as plt
import thinkdsp as dsp
from thinkdsp import Spectrogram, read_wave
from thinkdsp import decorate
from IPython.display import display
from thinkdsp import play_wave
from ipywidgets import interact, fixed
from thinkdsp import SinSignal
from playsound import playsound

signal = SinSignal(freq=400,amp = 1.0)#频率400HZ，幅度为0.25
plt.subplot(231)
plt.title("signal 1")
signal.plot()

signal = SinSignal(freq=600,amp = 0.50)#频率600HZ，幅度为0.50
plt.subplot(232)
plt.title("signal 2")
signal.plot()

signal = SinSignal(freq=200,amp = 0.25)#频率200HZ，幅度为0.25
plt.subplot(233)
plt.title("signal 3")
signal.plot()

signal = (SinSignal(freq = 400,amp = 1.0)+  
          SinSignal(freq = 600,amp = 0.50)+ 
          SinSignal(freq = 200,amp = 0.25)) #将三段信号合成一段信号

spect = signal.make_wave()
spect.write('output1.wav')
playsound('output1.wav')
plt.subplot(234)
plt.title("signal 4")
signal.plot()

wave2 = signal.make_wave(duration = 1)
wave2.apodize()
wave2.make_audio()
Spectrum = wave2.make_spectrum()
plt.subplot(235)
plt.title("framerate 4-1")
Spectrum.plot(high=2000)

##如果我们加上一个不是200赫兹倍数的分量，我们会听到一个不同的音调。
signal += SinSignal(freq = 450)
signal.make_wave().make_audio()
plt.subplot(236)
plt.title("signal 5")
signal.plot()

plt.show()
