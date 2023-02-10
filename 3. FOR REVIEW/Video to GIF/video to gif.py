# Anotaciones:

# Este código puede servirme para mi app de audio y video.

from moviepy.editor import *

video = input("Enter path of the video to convert: ")
gif = input("Enter path of the converted gif + new name(without extension): ")

clip = (VideoFileClip(rf"{video}").subclip(0.3))
clip.write_gif(f"{gif}"+".gif")

print("FINISHED!")