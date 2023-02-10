# Modificaciones:

# Guardar los textos en una carpeta diferente de la actual.

import pywhatkit as kit

text = input("Type your text: ")
name = input("Type the name of your document: ")

kit.text_to_handwriting(text, name+str(".png"), [0, 250, 154]) 

print("Finished")