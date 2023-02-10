# Modificar:

# Crear una ventana para navegar por el Explorador de Windows y escoger la carpeta que quiera.


from PyPDF2 import PdfFileMerger
import os

pdf = PdfFileMerger()

for file in os.listdir():
	if file.endswith(".pdf"):
		pdf.append(file)

pdf.write("Merge.pdf")
pdf.close()
print("Merge completed!!!")