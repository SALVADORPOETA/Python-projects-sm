# Modificaciones:

# Guardar las grabaciones en otra carpeta.


import sounddevice as sound
from scipy.io.wavfile import write
import wavio as wv

freq=44100

duration = int(input("Enter the time in seconds that will last the audio: "))
name = input("Enter the name of the audio: ")
print("Recording...")

recording = sound.rec(int(duration*freq), samplerate = freq, channels = 2)
sound.wait()
write(f"{name}"+".wav", freq, recording)

print("FINISHED!")