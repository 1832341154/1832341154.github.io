import os                    #库文件
import matplotlib.pyplot as plt
import thinkdsp as dsp
from thinkdsp import read_wave
from thinkdsp import decorate
from IPython.display import display
from thinkdsp import play_wave
from ipywidgets import interact, fixed
from playsound import playsound

wave = read_wave('c:/Users/asus/Desktop/test1-2/92002__jcveliz__violin-origional.wav')
wave.normalize()
wave.make_audio()
plt.subplot(331)     #读取音频文件
wave.plot()    

segment = wave.segment(start =1.1,duration = 0.3)
segment.make_audio()
plt.subplot(332)     #开始时间1.1秒，持续时间0.3秒
segment.plot()  

segment = wave.segment(start =1.1,duration =0.005)
segment.make_audio()
plt.subplot(333)     #开始时间1.1秒，持续时间0.005秒
segment.plot()

segment = wave.segment(start =1.1,duration = 1.0)
spectrum = segment.make_spectrum()
plt.subplot(334)     #开始时间1.1秒，持续时间1.0秒
spectrum.plot(high=7000)
plt.subplot(335)     #图示频率范围7000HZ
spectrum.plot(high=1000) #图示频率范围1000HZ

segment = wave.segment(start =1.1,duration =1.0)
spectrum = segment.make_spectrum()
plt.subplot(336)
spectrum.low_pass(cutoff = 1000)  #所有高于1000的频率都衰减掉
# spectrum.high_pass(cutoff = 3000)
spectrum.plot(high=7000)
print(spectrum.peaks()[:30])     #峰值按降序打印频谱中的最高点及其频率
spect = spectrum.make_wave()
spect.write('output.wav')
playsound('output.wav')
##play_wave(filename='output.wav')

segment = wave.segment(start =1.1,duration =1.0)
spectrum = segment.make_spectrum()
plt.subplot(337)               #消除频率为3000~5000之间的音频信号
spectrum.band_stop(3000,5000)
spectrum.make_wave().make_audio()
spectrum.plot(high = 7000)


plt.show()

