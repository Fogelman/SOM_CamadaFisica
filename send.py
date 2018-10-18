#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from signalTeste import signalMeu
import numpy as np
import sounddevice as sd

import matplotlib.pyplot as plt
import json

import pygame
pygame.init()


with open ("data.json") as json_file:
    data = json.load(json_file)


freq = data["freq"]
amplitude = 0.5
periodo = 3 #Em segundos
fs = 44100
signal = signalMeu()


def subplot_signal (x1,t1,x2,t2,total,digito):
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

digito = "a"
while True:
    


    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_0:
                digito = "0"
            elif event.key == pygame.K_1:
                digito = "1"
            elif event.key == pygame.K_2:
                digito = "2"
            elif event.key == pygame.K_3:
                digito = "3"
            elif event.key == pygame.K_4:
                digito = "4"
            elif event.key == pygame.K_5:
                digito = "5"
            elif event.key == pygame.K_6:
                digito = "6"
            elif event.key == pygame.K_7:
                digito = "7"
            elif event.key == pygame.K_8:
                digito = "8"
            elif event.key == pygame.K_9:
                digito = "9"



    if (digito.isdigit() and len(digito) == 1 ):
        print("O digito a ser enviado é: {0}".format(digito))
        plt.close("all") 
        total = []
        t1, x1 = signal.generateSin(freq[digito][0],amplitude*4,periodo,fs)
        t2, x2 = signal.generateSin(freq[digito][1],amplitude,periodo,fs)
        
        total = x1 +x2
        
       
        x_fft, y_fft = signal.calcFFT(total,fs)

        # signal.plotFFT(x_fft,y_fft,"FFT digito {0}".format(digito))
        subplot_signal(x1,t1,x2,t2,total,digito)


        indexes = signal.calcPeaks(y_fft)
        print(signal.findFreq(x_fft[indexes],freq,1))

        sd.play(total, fs)
        sd.wait()

        digito = "a" #Reseta os digitos para não tocar



        
        
        
        
        
        
        










