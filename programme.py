import ecranLCD as LCD
import grovepi as gp
import ListeLivre as LL
import LR
import CU
import time
from soundplayer import SoundPlayer
import test
#on initialise les ports D2 et D3 pour les boutons poussoirs,et on in
switchPin = 2
switchPin2 = 4
switchPinREAD = 3

#		Initialisation des variables
hits = 0
switchState = 0
switchState2 = 0
switchStateREAD = 0
r = len(LL.affichage())

# 		Demarrage
LR.eteindreLedRouge()

if hits == 0 :
	LCD.setText("Bienvenue sur   le BibLab")
	for c in range(0,255):
		LCD.setRGB(c-200,200-c,c)
		time.sleep(0.01)
	LCD.setText("Choisissez un   livre")
	time.sleep(2)

const = "play"
hits = 1
while True :

	switchState = gp.digitalRead(switchPin)
	switchState2 = gp.digitalRead(switchPin2)
	switchStateREAD = gp.digitalRead(switchPinREAD)

	if const=="play" or const=="break" or const=="resume":
		if switchState == 1 :
			hits = hits + 1

		if switchState2 == 1 :
			hits = hits - 1

		if hits > r :
			hits = 1

		nom = LL.affichage()
		cv = nom[hits - 1]
		LCD.setText_norefresh(cv)

		if switchStateREAD == 1 or const== "resume":
			son = LL.son()
			aud = son[hits-1]
			audio= './Leslivres/'+aud
			if const=="play" or const=="break":
				son = LL.son()
				aud = son[hits-1]
				audio= './Leslivres/'+aud
				p= SoundPlayer(audio)
				LR.allumerLedRouge()
				p.play()
				LCD.setText(cv+ " en lecture")
			if CU.recupererDistance() == True or (const== "resume" and CU.recupererDistance() == True) :
				LCD.setRGB(150,150,0)
				LR.eteindreLedRouge()
				p.pause()
				print ("pause")
				LCD.setText(cv +" en Pause")
				time.sleep(5)
				LCD.setText_norefresh("Reprendre la lecture?")
				while True:
					LCD.setRGB(0,255,100)
					if gp.digitalRead(switchPin2) ==1:
						const="resume"
						LCD.setText("Reprise de la   lecture")
						time.sleep(2)
						break
					else :
						if gp.digitalRead(switchPinREAD) == 1:
							const="play"
							LCD.setText("Debut du livre")
							time.sleep(2)
							break
						else :
							if gp.digitalRead(switchPin) == 1:
								const="break"
								break
								LCD.setText("Retour au menu")
							else : 
								print ("en attente")
				print (cv)
				print (const)
				print ("yes")
				if const == "resume":
					LCD.setText(cv+ " en lecture")
					p.resume()
					print("resume")
					LR.allumerLedRouge()

