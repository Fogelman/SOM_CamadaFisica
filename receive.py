#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import signalTeste
import numpy as np
import sounddevice as sd


import matplotlib.pyplot as plt
from scipy.fftpack import fft
from scipy import signal as window
import peakutils



signal = signalTeste.signalMeu()
fs= 44100

duration = 2  # seconds
myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=2)

sd.wait()

sd.play(myrecording,fs)
print(myrecording)

sd.wait()


myrecording = myrecording[:,0]
print(len(myrecording))
print(myrecording)
# signal.plotFFT(myrecording,fs)
x,y = signal.calcFFT(myrecording, fs)
indexes = peakutils.indexes(y, thres=0.5, min_dist=30)
peaks_x = peakutils.interpolate(x, y, ind=indexes)
print(peaks_x)
print(x[indexes], y[indexes])

point = [x[indexes][0],y[indexes][0]]
plt.figure()
plt.plot(x, y)
plt.plot(x[indexes][0],y[indexes][0])    
plt.show()
plt.title('Fourier')



