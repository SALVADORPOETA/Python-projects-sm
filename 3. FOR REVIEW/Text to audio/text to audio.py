# Modificaciones:

# Poder crear nuevos textos con el programa en ejecución.
# Poder ponerle espacios al nombre del audio.

from gtts import gTTS 
import os

name = input("Enter the name of the audio (no spaces): ")

try:

	f = open("Sample.txt") # Poder crear nuevos textos con el programa en ejecución.
	x = f.read()


	language = 'en'

	audio = gTTS(text=x, slow=False)

	audio.save(name+str(".wav")) 

	os.system(name+str(".wav"))

	print("Finished")

except:

	pass