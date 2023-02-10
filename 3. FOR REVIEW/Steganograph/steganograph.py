# Modificar:

# ask for the name of the image


from tkinter import *
from tkinter import filedialog
import tkinter as tk 
from PIL import Image, ImageTk
import os
from stegano import lsb #pip3 install stegano
from tkinter import messagebox

root = Tk()
root.title("Steganography - Hide a secret Text Message in an Image")
root.geometry("700x500+550+100")
root.resizable(False, False)
root.configure(bg="#2f4155")


def showimage():
	global filename
	try:
		filename = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select Image File", filetypes=(("PNG file", "*.png"), ("JPG File", "*.jpg"), ("All file", "*.txt")))
		img = Image.open(filename)
		img = ImageTk.PhotoImage(img)
		lbl.configure(image=img, width=250, height=250)
		lbl.image = img
	except:
		pass

def Hide():
	global secret
	savemsg = messagebox.askquestion("save message", "Do you want to save your message?")
	if savemsg == "yes":
		message = text1.get(1.0, END)
		secret = lsb.hide(str(filename), message)
		messagebox.showinfo("Done!", "The message has been hidden. \nNow, save the image!")
	else:
		pass
		
def Show():
	try:
		clear_message = lsb.reveal(filename)
		text1.delete(1.0, END)
		text1.insert(END, clear_message)
	except:
		messagebox.showinfo("info", "There is no hidden message")


def save():
	try:
		saveimg = messagebox.askquestion("Save image", "Do you want to save this image?")
		if saveimg == "yes":
			# ask for the name of the image
			secret.save("hidden.png")
			messagebox.showinfo("Done!", "The image has been saved")
		else:
			pass
	except:
		messagebox.showerror("Error", "This image can't be saved without a message")


# icon
image_icon = PhotoImage(file="logo.jpg")
root.iconphoto(False, image_icon)

# logo
logo = PhotoImage(file="logo.png")
Label(root, image=logo, bg="#2f4155").place(x=10, y=0)

Label(root, text="CYBER SCIENCE", bg="#2d4155", fg="white", font="arial 25 bold").place(x=100, y=20)

# first Frame
f1 = Frame(root, bd=3, bg="black", width=340, height=280, relief=GROOVE)
f1.place(x=10, y=80)

lbl = Label(f1, bg="black")
lbl.place(x=40, y=10)

# Second Frame
f2 = Frame(root, bd=3, width=340, height=280, bg="white", relief=GROOVE)
f2.place(x=350, y=80)

text1 = Text(f2, font="Roboto 20", bg="white", fg="black", relief=GROOVE, wrap=WORD)
text1.place(x=0, y=0, width=320, height=295)

scrollbar1=Scrollbar(f2)
scrollbar1.place(x=320, y=0, height=277)

scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

# Third Frame
f3 = Frame(root, bd=3, bg="#2f4155", width=330, height=100, relief=GROOVE)
f3.place(x=10, y=370)

Button(f3, text="Open Image", width=10, height=2, font="arial 14 bold", cursor="hand2", command=showimage).place(x=20, y=30)
Button(f3, text="Save Image", width=10, height=2, font="arial 14 bold", cursor="hand2", command=save).place(x=180, y=30)
Label(f3, text="Picture, Image, Photo File", bg="#2f4155", fg="yellow").place(x=20, y=5)

# Fourth Frame
f4 = Frame(root, bd=3, bg="#2f4155", width=330, height=100, relief=GROOVE)
f4.place(x=360, y=370)

Button(f4, text="Hide Data", width=10, height=2, font="arial 14 bold", cursor="hand2", command=Hide).place(x=20, y=30)
Button(f4, text="Show Data", width=10, height=2, font="arial 14 bold", cursor="hand2", command=Show).place(x=180, y=30)
Label(f4, text="Picture, Image, Photo File", bg="#2f4155", fg="yellow").place(x=20, y=5)


root.mainloop()
