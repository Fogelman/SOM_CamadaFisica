#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import signalTeste
import numpy as np
import sounddevice as sd

import matplotlib.pyplot as plt
from scipy.fftpack import fft
from scipy import signal as window
import peakutils
import json



with open ("data.json") as json_file:
    data = json.load(json_file)

signal = signalTeste.signalMeu()
fs= 44100
duration = 2  # seconds
freq = data["freq"]

def record (duration, fs):
    print("iniciando a gravação")
    myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=2)
    sd.wait()

    print(len(myrecording))
    print(myrecording)
    return myrecording[:,0] #return só de um canal do recording


def play_recording (recording, fs):
    sd.play(recording,fs)
    sd.wait()

def plotFFT(x,y):
    indexes = peakutils.indexes(y, thres=0.5, min_dist=30)
    print(x[indexes], y[indexes])

    # point = [x[indexes][0],y[indexes][0]]
    plt.figure()
    plt.plot(x, y)
    for i in range(len(x[indexes])):
        plt.plot(x[indexes][i],y[indexes][i],'ro')  
    plt.show()
    plt.title('Fourier')

recording = record(duration,fs)
x,y = signal.calcFFT(recording, fs)
# play_recording(recording,fs)
plotFFT(x,y)