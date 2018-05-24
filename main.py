import numpy as np 
from pydub import AudioSegment
from pydub.playback import play
from scipy.io.wavfile import read, write

def recognize_speech(audiofile):
	from vad import VoiceActivityDetector
	v = VoiceActivityDetector(audiofile)
	detected = v.detect_speech()
	# detected2 = v.convert_windows_to_readible_labels(detected)
	return detected # returns array of window numbers and speech flags (1 - speech, 0 - nonspeech)

def recognize_melody(audiofile):
	pass

def main(audiofile):
	rate, signal = read(audiofile)
	recognized = recognize_speech(audiofile)
	inds = []
	for ind, x in enumerate(recognized[:-1]):
		for y in np.arange(int(x[0]), int(recognized[ind+1][0])):
			inds.append(y)
	print(len(inds))
	speech = np.array([signal[ind] for ind in inds])
	write('middleman.wav', 48100, speech)
	# middlerate, middlesignal = read('middleman.wav')

	song = AudioSegment.from_wav('middleman.wav')
	# print(len(speech), len(recognized)) # (1580, 27409)

	# pan the sound 15% to the right
	panned_right = song.pan(+0.15)

	# pan the sound 50% to the left
	# panned_left = song.pan(-0.50)

	# #Play panned left audio
	from pydub.playback import play
	# play(panned_left)

if __name__ == '__main__':
	main("song.wav")