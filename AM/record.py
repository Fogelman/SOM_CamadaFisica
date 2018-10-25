import sounddevice as sd
import soundfile as sf
import np

print("iniciando a gravação")
fs= 44100
duration = 5
myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=2)
myrecording = np.ndarray.flatten(myrecording)
sd.wait()

sf.write("gravacao.wav", myrecording, fs)

