from tkinter import *

root = Tk()
root.geometry("400x400")
root.title("Hello World")

e = Entry(root, font=("arial", 20), fg="black")
e.place(x=40, y=80, height=50, width=200)

def hello_world():
	e.insert(0, "Hello World!!!")

button1 = Button(root, text="Hello", font="arial 12", fg="white", bg="green", bd=0, height=2, width=10, cursor="hand2", command=hello_world, activebackground="green").place(x=100, y=200) 

root.mainloop()







