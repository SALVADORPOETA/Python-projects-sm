from googletrans import Translator

translator = Translator()

mystory = '''Tell me who doesn't love baby yoda from mandolarian?'''

out = translator.translate(mystory, dest='hi')

print(out.text)