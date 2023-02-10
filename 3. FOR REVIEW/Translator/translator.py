# Modificaciones:

# Cambiar la URL para poder usar detect_language().


from tkinter import *
from tkinter import ttk, messagebox
import googletrans

import textblob

root = Tk()
root.title("Google Translator")
root.geometry("1080x400")

def label_change():
	c1 = combo1.get()
	c2 = combo2.get()
	label1.configure(text=c1)
	label2.configure(text=c2)
	root.after(1000, label_change)

def translate_now():
	global language
	try:
		text_ = text1.get(1.0, END)
		c3 = combo1.get()
		c4 = combo2.get()
		if text_:
			words = textblob.TextBlob(text_)
			# Leí un comentario en github: I am having the same issue. it worked a week ago, now I'm receiving a 404 error whenever I call detect_language(). Tal vez deba crear mi propia librería con la nueva URL (https://translate.googleapis.com/translate_a/t?anno=3&client=te&format=html&v=1.0&key&tc=1&sr=1&mode=1) e importarla aquí.
			lan = words.detect_language()
			for i, j in language.items():
				if j == c4:
					lan_ = i
			words = words.translate(from_lang=lan, to=str(lan_))
			text2.delete(1.0, END)
			text2.insert(END, words)
	except Exception as e:
		messagebox.showerror("googletrans", "please try again")

# icon
image_icon = PhotoImage(file="Images/google.png")
root.iconphoto(False, image_icon)

# arrow
arrow_image = PhotoImage(file="Images/arrow.png")
smaller_arrow = arrow_image.subsample(4, 4)
image_label = Label(root, image=smaller_arrow, width=150)
image_label.place(x=460, y=50)

language = googletrans.LANGUAGES
languageV = list(language.values())
lang1 = language.keys()

combo1 = ttk.Combobox(root, values=languageV, font="Roboto 14", state="r")
combo1.place(x=110, y=20)
combo1.set("ENGLISH")

label1 = Label(root, text="ENGLISH", font="segoe 30 bold", bg="white", width=18, bd=5, relief=GROOVE)
label1.place(x=10, y=50)

f1 = Frame(root, bg="Black", bd=5)
f1.place(x=10, y=118, width=440, height=210)

text1 = Text(f1, font="Roboto 20", bg="white", relief=GROOVE, wrap=WORD)
text1.place(x=0, y=0, width=430, height=200)

scrollbar1 = Scrollbar(f1)
scrollbar1.pack(side="right", fill="y")

scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

combo2 = ttk.Combobox(root, values=languageV, font="Roboto 14", state="r")
combo2.place(x=730, y=20)
combo2.set("SELECT LANGUAGE")

label2 = Label(root, text="ENGLISH", font="segoe 30 bold", bg="white", width=18, bd=5, relief=GROOVE)
label2.place(x=620, y=50)

f2 = Frame(root, bg="Black", bd=5)
f2.place(x=620, y=118, width=440, height=210)

text2 = Text(f2, font="Roboto 20", bg="white", relief=GROOVE, wrap=WORD)
text2.place(x=0, y=0, width=430, height=200)

scrollbar2 = Scrollbar(f2)
scrollbar2.pack(side="right", fill="y")

scrollbar2.configure(command=text2.yview)
text2.configure(yscrollcommand=scrollbar2.set)

# translate button
translate=Button(root, text="Translate", font="Roboto 15 bold italic", activebackground="purple", cursor="hand2", bd=5, bg="red", fg="white", command=translate_now)
translate.place(x=480, y=250)

label_change()

root.configure(bg="white")

root.mainloop()


'''
	No pude completar este proyecto. Me apareció un error en el último paso. Hice varias pruebas, investigué en varias fuentes y no logré resolverlo. Aquí lo copio para revisarlo en el futuro:

	Exception in Tkinter callback
	Traceback (most recent call last):
	  in http_error_default
	    raise HTTPError(req.full_url, code, msg, hdrs, fp)
	urllib.error.HTTPError: HTTP Error 400: Bad Request

	Aquí encontré una respuesta interesante en Stackoverflow:

	Textblob library uses Google API for translation functionality in the backend. Google has made some changes in the its API recently. Due to this reason TextBlob's translation feature has stopped working. I noticed that by making some minor changes in translate.py file (in your folder where all TextBlob files are located) as mentioned below, we can get rid of this error:

	original code:

	url = "http://translate.google.com/translate_a/t?client=webapp&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss&dt=t&dt=at&ie=UTF-8&oe=UTF-8&otf=2&ssel=0&tsel=0&kc=1"
	
	change above code in translate.py to following:

	url = "http://translate.google.com/translate_a/t?client=te&format=html&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss&dt=t&dt=at&ie=UTF-8&oe=UTF-8&otf=2&ssel=0&tsel=0&kc=1"
	Share

'''