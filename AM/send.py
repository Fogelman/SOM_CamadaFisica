import soundfile as sf
import sounddevice as sd
import numpy as np
from scipy import signal 


data, samplerate = sf.read("gravacao.wav")

# sd.play(data)
# sd.wait()

fs= 44100
duration = 5
print(data[:,0])


def normalizar(data):
	# norm1= (data - min(data))/ (max(data) - min(data))
	abs_mod = [np.max(data), np.abs(min(data))]
	norm= data/max(abs_mod)

	return norm

def filtro(data):
	nyq_rate = samplerate/2
	width = 5.0/nyq_rate
	ripple_db = 60.0 #dB
	N , beta = signal.kaiserord(ripple_db, width)
	cutoff_hz = 3000
	taps = signal.firwin(N, cutoff_hz/nyq_rate, window=('kaiser', beta))
	yFiltrado = signal.lfilter(taps, 1.0, data)
	return yFiltrado

def generateSin(freq, amplitude, time, fs):
	n = time*fs
	x = np.linspace(0.0, time, n)
	s = float(amplitude)*np.sin(freq*x*2*np.pi)
	return (x, s)

def playRecording(modulada,fs):
	sd.play(modulada,fs)
	sd.wait()

datanorm= normalizar(data[:,0])
datafilter= filtro(datanorm)
s, portadora = generateSin(12000,1, duration,fs)
modulada = np.multiply(portadora, datafilter)
# modulada= portadora*datanorm
print("SEND")
a = input("TESTANDO")

playRecording(modulada,fs)
print(modulada)
