#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import signalTeste
import numpy as np
import sounddevice as sd

import matplotlib.pyplot as plt
import json


with open ("data.json") as json_file:
    data = json.load(json_file)


freq = data["freq"]

amplitude = 0.5
periodo = 1 #Em segundos
fs = 44100
signal = signalTeste.signalMeu()
while True:
    print("Digite um número:", end=" ")
    digito = input("")
    
    if (digito.isdigit() and len(digito) == 1 ):
        plt.close("all") 
        total = []
        t1, x1 = signal.generateSin(freq[digito][0],amplitude,periodo,fs)
        t2, x2 = signal.generateSin(freq[digito][1],amplitude,periodo,fs)
        
        total = x1 +x2
        
        plt.figure("Digito {0}".format(digito))
        plt.title('Senoide de {0} hz'.format(freq[digito][0]), fontsize=8)
        ax1 = plt.subplot(311)
        plt.plot(t1, x1)
        plt.title('Senoide de {0} hz'.format(freq[digito][0]), fontsize=8)
        plt.ylabel('Amplitude', fontsize=8)

        plt.setp(ax1.get_xticklabels(), fontsize=6)

        # share x only
        ax2 = plt.subplot(312, sharex=ax1, sharey=ax1)
        plt.plot(t2, x2)
        plt.title('Senoide de {0} hz'.format(freq[digito][1]), fontsize=8)
        plt.ylabel('Amplitude', fontsize=8)

        # make these tick labels invisible
        plt.setp(ax2.get_xticklabels(), fontsize=6)

        # share x and y
        ax3 = plt.subplot(313, sharex=ax1, sharey=ax1)
        plt.plot(t1, total)
        plt.title('Somatória das senoides de {0} hz e {1} hz'.format(freq[digito][0],
        freq[digito][1]), fontsize=8)
        plt.ylabel('Amplitude', fontsize=8)
        
        plt.setp(ax3.get_xticklabels(), fontsize=6)

        plt.xlabel('Tempo (Segundos)', fontsize=8)
        plt.xlim(0.0, 0.025)
        plt.tight_layout()
        plt.show(block=False)

        sd.play(total, fs)
        sd.wait()

        
        
        
        
        
        
        










