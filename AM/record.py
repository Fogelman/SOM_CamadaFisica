import sounddevice as sd
import soundfile as sf

print("iniciando a gravação")
fs= 44100
duration = 5
myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=2)
sd.wait()

sf.write("gravacao.wav", myrecording, fs)

