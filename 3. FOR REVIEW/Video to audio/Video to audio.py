# Anotaciones:

# Este código me puede servir para crear una app de audio y video.

import moviepy.editor as mp

video = input("Enter path of the video to convert: ")
audio = input("Enter path of the audio file + new name(without extention): ")

clip = mp.VideoFileClip(rf"{video}")
clip.audio.write_audiofile(rf"{audio}"+".wav")


# C:/Users/Public/Videos/Sample Videos/Wildlife.wmv
