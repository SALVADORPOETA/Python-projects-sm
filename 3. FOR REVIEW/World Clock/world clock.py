# Anotaciones:

# Solucioné el problema de los relojes. Pero no sé por qué funciona. Investigar si puede funcionar con otro nombre distinto al de clock4.


from datetime import datetime
import pytz
from tkinter import *
import time

root = Tk()

root.geometry("1100x400+100+200")
image_ico = PhotoImage(file="Images/world.png")
root.iconphoto(False, image_ico)
root.title("World clock")

def times():
	home1=pytz.timezone("Asia/kolkata")
	local_time1=datetime.now(home1)
	current_time1=local_time1.strftime("%a %H:%M:%S")
	clock1.config(text=current_time1)
	name1.config(text="India")
	#clock1.after(200, times)

	home2=pytz.timezone("America/New_York")
	local_time2=datetime.now(home2)
	current_time2=local_time2.strftime("%a %H:%M:%S")
	clock2.config(text=current_time2)
	name2.config(text="New York")
	#clock2.after(200, times)

	home3=pytz.timezone("Europe/London")
	local_time3=datetime.now(home3)
	current_time3=local_time3.strftime("%a %H:%M:%S")
	clock3.config(text=current_time3)
	name3.config(text="London")
	#clock3.after(200, times)

	home4=pytz.timezone("Asia/Tokyo")
	local_time4=datetime.now(home4)
	current_time4=local_time4.strftime("%a %H:%M:%S")
	clock4.config(text=current_time4)
	name4.config(text="Tokyo")
	clock4.after(200, times)


#first time zone
f1 = Frame(root, bd=5)
f1.place(x=10, y=118, width=220, height=150)
name1=Label(f1, font=("Helvetica", 30, "bold"))
name1.place(x=50, y=10)

logo1 = PhotoImage(file="Images/in.png")
image_label1 = Label(root, image=logo1)
image_label1.place(x=20, y=150)

clock1 = Label(f1, font=("Helvetica", 20))
clock1.place(x=5, y=80)

# second time zone
f2 = Frame(root, bd=5)
f2.place(x=300, y=118, width=220, height=150)
name2=Label(f2, font=("Helvetica", 30, "bold"))
name2.place(x=30, y=10)

logo2 = PhotoImage(file="Images/us.png")
image_label2 = Label(root, image=logo2)
image_label2.place(x=290, y=150)

clock2 = Label(f2, font=("Helvetica", 20))
clock2.place(x=5, y=80)

# third time zone
f3 = Frame(root, bd=5)
f3.place(x=600, y=118, width=220, height=150)
name3=Label(f3, font=("Helvetica", 30, "bold"))
name3.place(x=50, y=10)

logo3 = PhotoImage(file="Images/gb.png")
image_label3 = Label(root, image=logo3)
image_label3.place(x=600, y=150)

clock3 = Label(f3, font=("Helvetica", 20))
clock3.place(x=5, y=80)

# fourth time zone
f4 = Frame(root, bd=5)
f4.place(x=900, y=118, width=220, height=150)
name4=Label(f4, font=("Helvetica", 30, "bold"))
name4.place(x=50, y=10)

logo4 = PhotoImage(file="Images/jp.png")
image_label4 = Label(root, image=logo4)
image_label4.place(x=900, y=150)

clock4 = Label(f4, font=("Helvetica", 20))
clock4.place(x=5, y=80)

times()

root.mainloop()