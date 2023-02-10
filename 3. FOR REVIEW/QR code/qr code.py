# Modificaciones:

# Crear una ventana que me permita escoger la imagen qr desde el explorador.
# Crear una interfaz que me permita escoger la opción de crear un mensaje en un código qr como en la primera parte de este código.
# Agregar estas funcionalidades al programa de imágenes.


'''
import pyqrcode

text="hello here "

qr = pyqrcode.create(text)
qr.png("abc.png", scale=6)

'''

from pyzbar.pyzbar import decode

from PIL import Image

d = decode(Image.open("abc.png"))

print(d[0].data.decode("ascii"))
