# Modificar:

# "me" 
# parámetro ip

import geocoder

g = geocoder.ip("me")

print("Your Latitude and Longitude is", g.latlng)

'''
Se supone que me tendría que dar la dirección exacta de donde estoy, pero me dio una dirección en el centro de mi ciudad. No sé si es porque la laptop ya es de uso y me está dando la dirección de sus antiguos dueños o es otra razón.

Se supone que si le cambio el parámetro ip("me") por la ip que me dio el ejercicio de encontrar mi IP, me tendría que dar las coordenadas de mi ubicación, pero en vez de eso me da unos corchetes vacíos.

'''