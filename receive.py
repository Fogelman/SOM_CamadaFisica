#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from signalTeste import signalMeu
import sounddevice as sd

import matplotlib.pyplot as plt
import json



with open ("data.json") as json_file:
    data = json.load(json_file)

signal = signalMeu()
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

plt.close("all") #fecha todos os gráficos
recording = record(duration,fs)
x,y = signal.calcFFT(recording, fs)
# play_recording(recording,fs)
signal.plotFFT(x,y)