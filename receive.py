#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from signalTeste import signalMeu
import sounddevice as sd

import matplotlib.pyplot as plt
import json
import numpy as np

import time

with open ("data.json") as json_file:
	data = json.load(json_file)

signal = signalMeu()
fs= 44100
duration = 1  # seconds
freq = data["freq"]

def subplot_signal (recording,t,fs):
	N  = len(recording)
	T  = 1/fs
	xf = np.linspace(0.0, 1.0/(2.0*T), N)
	plt.figure()
	plt.plot(xf,recording)
	plt.title('Sinal recebido')
	plt.show(block=False)
	plt.draw()
	plt.pause(0.1)



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


		

while True:
	plt.close("all") #fecha todos os gráficos
	recording = record(duration,fs)
	x,y = signal.calcFFT(recording, fs)

	play_recording(recording,fs)

	indexes = signal.calcPeaks(y)
	lista_frequencia, resultado = signal.findFreq(x[indexes],freq,1)
	print(resultado)

	if resultado != None:
		signal.plotFFT(x,y,"Digito {0}".format(resultado))

		subplot_signal(recording,duration,fs)
		
		break


while True:
	pass