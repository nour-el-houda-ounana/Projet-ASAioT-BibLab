import ecranLCD as LCD
import grovepi as gp
import serial
import time
import ListeLivre as LL
#import LR
import lecture as Lec
import CU

switchPin = 3
switchPin2 = 2
switchPinREAD = 4
hits = 0

switchState = 0
switchState2 = 0
switchStateREAD = 0

r = len(LL.affichage())


LCD.setRGB(100,0,0)
if hits == 0 :
	LCD.setText("choisissez un    livre")
	time.sleep(2)


hits = 1

while True :

	switchState = gp.digitalRead(switchPin)
	switchState2 = gp.digitalRead(switchPin2)
	switchStateREAD = gp.digitalRead(switchPinREAD)

	if switchState == 1 :
		hits = hits + 1

	if switchState2 == 1 :
		hits = hits - 1

	if hits > r :
		hits = 1

	nom = LL.affichage()
	cv = nom[hits - 1]
	LCD.setText_norefresh(cv)

	if switchStateREAD == 1 :
		son = LL.son()
		aud = son[hits-1]
		audio= './Leslivres/'+aud
		Lec.play(audio)
	CU.recupererDistance()
