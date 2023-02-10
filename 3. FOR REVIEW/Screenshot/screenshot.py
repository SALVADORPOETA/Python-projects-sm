# Anotaciones:

# Podría combinar este programa con el screenrecorder.


import pyautogui
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()

canvas1 = tk.Canvas(root, width=150, height = 30)
canvas1.pack()

def takeScreenshot():
	myScreenshot = pyautogui.screenshot()
	file_path = filedialog.asksaveasfilename(defaultextension='.png')
	myScreenshot.save(file_path)

myButton = tk.Button(text='Take Screenshot', command=takeScreenshot, bg='black', fg='white', font=10, cursor="hand2")
canvas1.create_window(75, 10, window=myButton)

root.mainloop()
