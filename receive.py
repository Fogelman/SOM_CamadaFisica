#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import signalTeste
import numpy as np
import sounddevice as sd


fs= 3500

duration = 2  # seconds
myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=2)

sd.wait()

sd.play(myrecording,fs)
print(myrecording)

sd.wait()