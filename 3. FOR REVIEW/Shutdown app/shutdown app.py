# Modificaciones:

# Agregar askquestion para comprobar que el usuario quiera llevar a cabo las acciones determinadas en todas las funciones.
# Solucionar el error de que no reconoce el shutdown.


from tkinter import *
import os


root = Tk()
root.title("Shutdown App")
root.geometry("400x580+900+50")


def restarttime():
	os.system("shutdown /r /t 30")


def restart():
	os.system("shutdown /r /t 1")


def shutdown():
	os.system("shutdown /s /t 1")


def logout():
	os.system("shutdown -l")


# first button
restart_time_button = PhotoImage(file="restart time.png").subsample(2, 2)
first_button = Button(root, image=restart_time_button, borderwidth=0, cursor="hand2", command=restarttime)
first_button.place(x=10, y=10)

# second button
close_button = PhotoImage(file="close.png").subsample(2, 2)

second_button = Button(root, image=close_button, borderwidth=0, cursor="hand2", command=root.destroy)
second_button.place(x=200, y=10) 

# third button
restart_button = PhotoImage(file="restart.png").subsample(2, 2)

third_button = Button(root, image=restart_button, borderwidth=0, cursor="hand2", command=restart)
third_button.place(x=10, y=200)

# fourth button
shutdown_button = PhotoImage(file="shutdown.png").subsample(2, 2)

fourth_button = Button(root, image=shutdown_button, borderwidth=0, cursor="hand2", command=shutdown)
fourth_button.place(x=200, y=200) 

# fifth button
logout_button = PhotoImage(file="logout.png").subsample(2, 2)

fifth_button = Button(root, image=logout_button, borderwidth=0, cursor="hand2", command=logout)
fifth_button.place(x=10, y=400) 




root.mainloop()
