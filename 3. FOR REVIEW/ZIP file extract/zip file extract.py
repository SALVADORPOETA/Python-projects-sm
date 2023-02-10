# Modificaciones:

# Definir la dirección en la que se van a extraer los archivos. Con el programa activo.


from zipfile import ZipFile

file = input("Enter path of zip file: ")

with ZipFile(file, "r") as zip:
	zip.printdir()
	zip.extractall()
	print("Task is completed") 