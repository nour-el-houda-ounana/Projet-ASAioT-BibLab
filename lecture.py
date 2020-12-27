import numpy as np
from scipy.io import wavfile
import pyaudio
import time
from pynput import keyboard

def sound(array, fs=8000):
	p = pyaudio.PyAudio()
	stream = p.open(format=pyaudio.paInt16, channels=len(array.shape), rate=fs, output=True)
	stream.write(array.tobytes())
	stream.stop_stream()
	stream.close()
	p.terminate()

file = 'Leslivres/test.wav'

def play(file) :
	fs,data = wavfile.read(file)
	return sound(data, fs)


def on_press(key):
	global paused
	print (key)
	if key == keyboard.Key.space:
		if stream.is_stopped():     # time to play audio
			print ('play pressed')
			stream.start_stream()
			paused = False
			return False
		elif stream.is_active():   # time to pause audio
			print ('pause pressed')
			stream.stop_stream()
			paused = True
			return False
		return False









#def pause(file) :
#	return file.stop_stream()

#print (pause(file))





def pause():
    programPause = input("Press")



#print (play(file))

#time.sleep(10)
#stream.stop_stream('test.wav')
