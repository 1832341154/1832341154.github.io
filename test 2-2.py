import os
import  matplotlib.pyplot as plt
from matplotlib.pyplot import xlabel
from thinkdsp import TriangleSignal
from thinkdsp import SquareSignal
from thinkdsp import decorate
from thinkdsp import SawtoothSignal


sawtooth = SawtoothSignal().make_wave(duration = 0.5,framerate = 40000)
sawtooth.make_audio()
square = SquareSignal(amp=0.5).make_wave(duration= 0.5,framerate=40000)
plt.subplot(211)
sawtooth.make_spectrum().plot(color='green')  #锯齿波频谱用绿色标注
square.make_spectrum().plot(color='red')      #方波频谱用红色标注
decorate(xlabel = 'Frequency1(Hz)')
#与方波相比，锯齿波的衰减类似，但它包含偶数谐波和奇数谐波。注意，我必须削减方波的振幅，使它们具有可比性。
sawtooth = SawtoothSignal().make_wave(duration = 0.5,framerate = 40000)
sawtooth.make_audio()
triange = TriangleSignal(amp=0.79).make_wave(duration= 0.5,framerate=40000)
plt.subplot(212)
sawtooth.make_spectrum().plot(color='green')
triange.make_spectrum().plot(color='blue')    #三角波频谱用蓝色标注
decorate(xlabel = 'Frequency2(Hz)')
#与三角波相比，锯齿波的衰减相对缓慢
plt.show()