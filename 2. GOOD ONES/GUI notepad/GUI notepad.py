from tkinter import *
from tkinter import filedialog
from tkinter import messagebox


root = Tk()
root.geometry("600x600+500+50")
root.title("Notepad")
root.config(bg='lightblue')
root.resizable(False, False)


def save_file():

	save = messagebox.askquestion("Save", "Do you wanna save file?")
	if save == "yes":
		open_file = filedialog.asksaveasfile(mode = 'w', defaultextension = '.txt')
		if open_file is None:
			return
		text = str(entry.get(1.0, END))
		open_file.write(text)
		open_file.close()
	else:
		pass


def open_file():

	try:
		file = filedialog.askopenfile(mode = 'r', filetype = [('text files', '*.txt')])
		if file is not None:
			content = file.read()
		entry.insert(INSERT, content)
	except:
		pass


def reset():

	entry.delete(1.0, END)


b1 = Button(root, width='20', height='2', bg='#fff', text='save file', command=save_file, cursor="hand2").place(x=50, y=10)
b2 = Button(root, width='20', height='2', bg='#fff', text='open file', command=open_file, cursor="hand2").place(x=230, y=10)
b3 = Button(root, width='20', height='2', bg='#fff', text='reset', command=reset, cursor="hand2").place(x=410, y=10)

entry = Text(root, height='33', width='72', wrap=WORD)
entry.place(x=10, y=60)




root.mainloop()