import os
import  matplotlib.pyplot as plt
import numpy as np
from thinkdsp import read_wave
from thinkdsp import Signal
from thinkdsp import SawtoothSignal
from thinkdsp import decorate
from playsound import playsound
from thinkdsp import Chirp
from thinkdsp import normalize,unbias

wave = read_wave('C:/Users/asus/Desktop/test5/72475__rockwehrmann__glissup02.wav')
wave.normalize()
wave.make_audio()
#读取音频文件
wave.make_spectrogram(512).plot(high= 5000)#每个片段的采样数量，这里选用512，这是考虑到采样数量的幂指数时FFT效率更高
decorate(xlabel = 'Time(s)',ylabel = 'Frequency(HZ)')#x轴为时间，y轴为频率
wave.plot()   
plt.show() 