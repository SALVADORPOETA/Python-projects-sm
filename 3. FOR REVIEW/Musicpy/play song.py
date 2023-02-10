# Modificaciones:

# Resolver el Error 261.
# Crear una ventana que me permita navegar en el explorador de windows para reproducir la canción que yo quiera.



from playsound import playsound

playsound('Sleep Away.mp3')

# No me agarró el programa. Intenté desde carpetas distintas y no se pudo. Intenté moviendo la música y el programa a la misma carpeta y tampoco.

'''
playsound.PlaysoundException: 
    Error 261 for command:
        open "C:[...].mp3"
    El controlador no puede reconocer el comando especificado.
'''