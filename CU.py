# GrovePi + Grove Ultrasonic Ranger
#import lecture as lec
from grovepi import *
#from time import *
# Connect the Grove Ultrasonic Ranger to digital port D5

ultrasonic_ranger = 7

def recupererDistance() :

	while True :
		pause = False 
		if ultrasonicRead(ultrasonic_ranger) == 0 :
			pause = True 
			return pause

#print (recupererDistance())
