# Anotaciones:

# Agregar este código a la app de imágenes.


import qrcode

title = input("Enter the title of your message: ")
data = input("Enter your message: ")

img = qrcode.make(data = data)

img.save(title+str(".png"))