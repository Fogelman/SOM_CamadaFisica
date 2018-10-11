#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import signalTeste
import numpy as np
import sounddevice as sd

import json

freq = {
    "1":[697,1209],
    "2":[697,1336],
    "3":[697,1477],
    "4":[770,1209],
    "5":[770,1336],
    "6":[770,1477],
    "7":[852,1209],
    "8":[852,1336],
    "9":[852,1477],
    "0":[941,1336],

}
amplitude = 0.5
periodo = 1 #Em segundos
fs = 44100
signal = signalTeste.signalMeu()

digito = input("Digite um numero: ")
total = []


x1 = signal.generateSin(freq[digito][0],amplitude,periodo,fs)[1]
x2 = signal.generateSin(freq[digito][1],amplitude,periodo,fs)[1]

total = x1 +x2

sd.play(total, fs)
sd.wait()

