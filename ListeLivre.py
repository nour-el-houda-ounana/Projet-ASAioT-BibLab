import os

Liste = os.listdir("Leslivres")

#fonction qui va afficher le nom du livre et son auteur sans l'extension
def affichage() :
	names =[]
	for onePath in Liste:

		names.append(os.path.splitext(os.path.basename(onePath))[0])
	return names

print (affichage())
#focntion qui va mettre l'audio en fonction de  ce qui est affciher 
def son() :
	son = []
	for aud in Liste :
		son.append(aud)
	return son

print (son())
