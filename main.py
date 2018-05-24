import numpy as np 
from pydub import AudioSegment
from pydub.playback import play

def recognize_speech(audiofile):
	pass

def recognize_melody(audiofile):
	pass


song = AudioSegment.from_mp3("song.mp3")
# pan the sound 15% to the right
panned_right = song.pan(+0.15)

# pan the sound 50% to the left
panned_left = song.pan(-0.50)

# #Play panned left audio
# while True:
#     try:
#         play(panned_left)
#     except KeyboardInterrupt:
#         print "Stopping playing"
#         break