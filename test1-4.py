import os
import matplotlib.pyplot as plt
import thinkdsp as dsp
from thinkdsp import read_wave
from thinkdsp import decorate
from IPython.display import display
from thinkdsp import play_wave
from ipywidgets import interact, fixed
from playsound import playsound

def stretch(wave ,factor):
    wave.ts *=factor
    wave.framerate /= factor

wave = read_wave('c:/Users/asus/Desktop/test1-2/92002__jcveliz__violin-origional.wav')

wave.normalize()
wave.make_audio()
stretch(wave,1)
plt.subplot(121)
wave.plot()

wave.normalize()
wave.make_audio()
stretch(wave,0.5)
plt.subplot(122)
wave.plot()

plt.show()