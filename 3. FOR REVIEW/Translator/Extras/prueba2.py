'''
from textblob import TextBlob

blob = TextBlob("Buongiorno!")
print(blob.translate(to='en'))

'''

from textblob import TextBlob 

blob = TextBlob("Buongiorno!")
if (blob.detect_language() != 'en'):
    blob.translate(to='en')

'''
from textblob import TextBlob

blob = TextBlob('TextBlob is a great tool for developers')
print(blob.translate(to='hi'))

'''