# coding: utf-8
from ecranLCD import *
import time

setText("Bienvenue")
setRGB(0,128,64)
time.sleep(.02)

for c in range(0,200):
	setRGB(c,200-c,0)
	time.sleep(0.01)
setRGB(0,255,255)

time.sleep(0.5)


