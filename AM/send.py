import soundfile as sf
import sounddevice as sd
import numpy as np
from scipy import signal 


data, samplerate = sf.read("gravacao.wav")

# sd.play(data)
# sd.wait()

fs= 44100

print(data[:,0])


def normalizar(data):
	# norm1= (data - min(data))/ (max(data) - min(data))
	abs_mod = [max(data), abs(min(data))]
	norm= data/max(abs_mod)

	return norm

def filtro(data):
	nyq_rate = samplerate/2
	width = 5.0/nyq_rate
	ripple_db = 60.0 #dB
	N , beta = signal.kaiserord(ripple_db, width)
	cutoff_hz = 1500.0
	taps = signal.firwin(N, cutoff_hz/nyq_rate, window=('kaiser', beta))
	yFiltrado = signal.lfilter(taps, 1.0, data)
	return yFiltrado

def generateSin(freq, amplitude, time, fs):
	n = time*fs
	x = np.linspace(0.0, time, n)
	s = float(amplitude)*np.sin(freq*x*2*np.pi)
	return (x, s)


datanorm= normalizar(data[:,0])
# print(datanorm)
# print(np.max(datanorm))
# print(np.min(datanorm))

datafilter= filtro(datanorm)
# print(datafilter)

s, portadora = generateSin(2000,3, 5,fs)
# sd.play(portadora,fs)
# sd.wait()

modulada= portadora* datafilter

print(modulada)
sd.play(modulada, fs)
sd.wait()
