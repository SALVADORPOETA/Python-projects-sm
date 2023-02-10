# Anotaciones:

# Probar este programa cuando tenga mi celular encendido.


'''
import pywhatkit

pywhatkit.sendwhatmsg(" +52 2291744012", "Saludos, humano. \nEsta es una prueba de un bot de whatsapp", 14, 6)

# lets explain the code
# sendwhatsmsg(phone no: str, message: str, time_hour: int, time__min: int, wait_time: int=10)

'''

import pywhatkit

phone = input("Enter phone number: ")
message = input("Enter message: ")
hour = int(input("Enter hour to deliver: "))
minute = int(input("Enter minute to deliver: ")

pywhatkit.sendwhatmsg(phone, message, hour, minute)
