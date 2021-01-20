import ecranLCD as LCD
import grovepi as gp
import ListeLivre as LL
import LR
import CU
import time
from soundplayer import SoundPlayer
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
	for c in range(0,200):
		LCD.setRGB(c,200-c,c)
		time.sleep(0.02)
	LCD.setText("Choisissez un   livre")
	time.sleep(2)

const = "play"
hits = 1
while True :

#initialisation des boutons pour droite(avancer dns le liste) et  gauche (reculer) et le bouton du milieu qui selectionne un livre

	switchState = gp.digitalRead(switchPin)
	switchState2 = gp.digitalRead(switchPin2)
	switchStateREAD = gp.digitalRead(switchPinREAD)

#affichage de la liste de livre qu'on peut parcourir

	if const=="play" or const=="break" or const=="resume" or const=="plays":

		if switchState == 1 :
			hits = hits + 1

		if switchState2 == 1 :
			hits = hits - 1

		if hits > r :
			hits = 1

		nom = LL.affichage()
		cv ="Livre:"+ nom[hits - 1]
		LCD.setText_norefresh(cv)

#selection d'un livre et donc lecture ou si boucle deja parcouru recommencer un livre

		if switchStateREAD == 1 or const== "resume" or const=="plays":
			if const=="play" or const=="break"or const=="plays":
				son = LL.son()
				aud = son[hits-1]
				audio= './Leslivres/'+aud
				p= SoundPlayer(audio)
				LR.allumerLedRouge()
				p.play()
				cv =nom[hits - 1]
				LCD.setText(cv+ " en lecture")
#main sur capteur ultra son (voir fonction recupererDistance sur le script CU) qui met pause

			if CU.recupererDistance() == True or (const== "resume" and CU.recupererDistance() == True) :
				LCD.setRGB(150,150,0)
				LR.eteindreLedRouge()
				p.pause()
				print ("pause")
				LCD.setText(cv +" en Pause")
				time.sleep(5)
				LCD.setText_norefresh("Reprendre la lecture?")

#attente du choix de l'utilisateur (recommencer ou reprendre la lecture ou changer de livre)

				while True:
					LCD.setRGB(0,255,100)
					if gp.digitalRead(switchPin2) ==1:
						const="resume"
						LCD.setText("Reprise de la   lecture")
						time.sleep(2)
						break
					else :
						if gp.digitalRead(switchPinREAD) == 1:
							const="plays"
							LCD.setText("Debut du livre")
							p.stop()
							time.sleep(2)
							break
						else :
							if gp.digitalRead(switchPin) == 1:
								const="break"
								LCD.setText("Retour au menu")
								p.stop()
								time.sleep(2)
								break
							else : 
								print ("en attente")
#en cas de reprise de la lecture 
				if const == "resume":
					LCD.setText(cv+ " en lecture")
					p.resume()
					LR.allumerLedRouge()

