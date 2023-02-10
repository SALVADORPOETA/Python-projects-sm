import cv2

image = cv2.imread("Penguins.jpg")
grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
invert = cv2.bitwise_not(grey)
blur = cv2.GaussianBlur(invert, (21, 21), 0)
invertblur = cv2.bitwise_not(blur)

sketch = cv2.divide(grey,invertblur, scale=260)
cv2.imwrite("sketch.png", sketch)

# Puedo intentar crear una ventana que me permita navegar en el Explorador de Windows y escoger la imagen que yo quiera.