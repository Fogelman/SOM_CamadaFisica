#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sounddevice as sd
import matplotlib.pyplot as plt
import json
import numpy as np
import time
from scipy import signal 


fs= 44100
duration = 10
freq = 12000




def record (duration, fs):
	print("iniciando a gravação")
	myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=2)
	sd.wait()

	print(len(myrecording))
	print(myrecording)
	return myrecording[:,0] #return só de um canal do recording


def demodulate (recording, base_freq, fs,duration):
	s, portadora = generateSin(base_freq,1, duration,fs)
	demodulate = portadora*recording
	return demodulate

def filtro(data,samplerate,cutoff_hz = 2000.0):
	nyq_rate = samplerate/2
	width = 5.0/nyq_rate
	ripple_db = 60.0 #dB
	N , beta = signal.kaiserord(ripple_db, width)
	
	taps = signal.firwin(N, cutoff_hz/nyq_rate, window=('kaiser', beta))
	yFiltrado = signal.lfilter(taps, 1.0, data)
	return yFiltrado

def generateSin(freq, amplitude, time, fs):
	n = time*fs
	x = np.linspace(0.0, time, n)
	s = float(amplitude)*np.sin(freq*x*2*np.pi)
	return (x, s)


#plt.close("all") #fecha todos os gráficos
recording = record(duration,fs)
demodulada = demodulate(recording,freq,fs,duration)
filtrada = filtro(demodulada,fs,4000)

print(filtrada)
sd.play(10*filtrada,fs)
sd.wait()