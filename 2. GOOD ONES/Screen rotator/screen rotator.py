from tkinter import *
import rotatescreen

root = Tk()
root.geometry("500x500")
root.resizable(False, False)
root.title("Screen Rotation")
root.configure(bg="#54c5d1")

def Screen_rotation(enter):
	screen = rotatescreen.get_primary_display()
	if enter =="up":
		screen.set_landscape()
	elif enter == "right":
		screen.set_portrait_flipped()
	elif enter == "down":
		screen.set_landscape_flipped()
	elif enter == "left":
		screen.set_portrait()

# adding background
photo = PhotoImage(file = "background.png")
myimage = Label(image=photo)
myimage.pack(padx=2, pady=2)


# Creating buttons
Button(root, text="Up", command=lambda:Screen_rotation("up"), bg="white", font="arial 18", width=5, cursor="hand2").place(x=200, y=50)
Button(root, text="Right", command=lambda:Screen_rotation("right"), bg="white", font="arial 18", width=5, cursor="hand2").place(x=400, y=230)
Button(root, text="Left", command=lambda:Screen_rotation("left"), bg="white", font="arial 18", width=5, cursor="hand2").place(x=20, y=230)
Button(root, text="Down", command=lambda:Screen_rotation("down"), bg="white", font="arial 18", width=5, cursor="hand2").place(x=205, y=400)


mainloop()
