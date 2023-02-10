from PIL import Image 

img = Image.open("Hydrangeas.jpg")

image = img.convert("RGB")

image.save("PDF File.pdf")

# Puedo intentar crear una ventana que me permita navegar en el Explorador de Windows y escoger la imagen que quiera.

