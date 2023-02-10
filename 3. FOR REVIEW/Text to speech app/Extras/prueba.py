import pyttsx3
import os


engine = pyttsx3.init()
engine.getProperty('rate')
engine.getProperty('volume')
voices= engine.getProperty('voices')
engine.setProperty('rate', 50)
engine.setProperty('volume', 0.25)
engine.setProperty('voices', voices[1].id)
engine.say("something")
engine.runAndWait()