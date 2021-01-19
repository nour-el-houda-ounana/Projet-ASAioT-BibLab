import time
from grovepi import *

# Connect the Grove LED to digital port D6
led = 6

pinMode(led,"OUTPUT")
time.sleep(1)


def allumerLedRouge():
	digitalWrite(led,1)     # allume la led Rouge
	print ("LED ON!")
#print (allumerLedRouge())



def eteindreLedRouge():   #Eteint la led Rouge
	digitalWrite(led,0)
	print ("LED OFF") 
#print (eteindreLedRouge())

def pause(): #fait clignoter la led durant la pause
	while True:
		digitalWrite(led,1)     # allume la led Rouge
		print ("LED ON!")
		time.sleep(1)
		digitalWrite(led,0)
		time.sleep(1)
		print ("LED OFF") 
#print (pause())

