# Modificaciones:

# Cambiar la fuente de color.
# Abrir el explorador de windows.
# Hacer interfaz.

from PIL import Image, ImageFont, ImageDraw

img = input("Enter the name of the image to open: ")
textimg = input("Enter the text: ")
savename = input("Save file as: ")


my_image = Image.open(img)
title_font = ImageFont.truetype("arial.ttf", 50)
title_text = textimg
image_editable=ImageDraw.Draw(my_image)
image_editable.text((300, 300), title_text, (235, 230, 212), font = title_font)
my_image.save(savename+str(".jpg"))

print("Finished")