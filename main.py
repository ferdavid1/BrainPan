import numpy as np 
from pydub import AudioSegment
from pydub.playback import play

def recognize_speech(audiofile):
	from vad import VoiceActivityDetector
	v = VoiceActivityDetector(audiofile)
	detected = v.detect_speech()
	return detected # returns array of window numbers and speech flags

def recognize_melody(audiofile):
	pass


# song = AudioSegment.from_mp3("song.mp3")
print(recognize_speech("song.mp3"))
# pan the sound 15% to the right
# panned_right = song.pan(+0.15)

# pan the sound 50% to the left
# panned_left = song.pan(-0.50)

# #Play panned left audio
# while True:
#     try:
#         play(panned_left)
#     except KeyboardInterrupt:
#         print "Stopping playing"
#         break