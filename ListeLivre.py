import os

Liste = os.listdir("Leslivres")

def affichage() :
	names =[]
	for onePath in Liste:

		names.append("Livre :" + os.path.splitext(os.path.basename(onePath))[0])
	return names

print (affichage())

def son() :
	son = []
	for aud in Liste :
		son.append(aud)
	return son

print (son())
