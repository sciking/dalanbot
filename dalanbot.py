# -*- coding: utf-8 -*-
print "Simulatore di Dalan"
print "*"*40
import string
import random
no = 0
apache = 0
si = 0
print "Ciao"
apprese = ["Ma che ooooh", "L'Arway del Duce über alles","Panino puzza :v"]
frasi = ["Viva le pantofole","io ti denuncerei", "ciabatte merda","ROM föra di ball","si","no", "Kurumo lezzo", "Mia sorella mi ha rotto l'iPad porcodio", "Panino mi ha mandato a cagare :c","Sono su YouPorn","Fiorenza è bellissima","e.e","Tu sei segoe","Porcoddio","Mi fanno domande pervertite su ask :c","Tante sculacciate","Mai più Windows","Non proverò Linux","Perotto è grande","Ah","k bll","830 merda","il 735 di mia sorella è bellissimo","che schifo i piedi",]
def chat():
	global apache
	apache = apache + 1
	global no
	global apprese
	global frasi
	global si
	parola = raw_input(">")
	parola = parola.lower()
	if parola != "" and "dalan" not in parola and "dalagn" not in parola and "dolan" not in parola:
		apprese.append(parola)
	if "pantofole" in parola:
		print "Viva le pantofole"
	elif "pantofole" in parola and "merda" in parola:
		print "Scarpe in casa merda"
	elif "renzi" in parola:
		print "Renzi mona"
	elif "kurumo"  in parola:
		print "688 merda"
	elif "neoplan" in parola:
		print "Neoplan Merda"
	elif "arway" in parola:
		print "Arway regna"
	elif parola == "no":
			if no > 4:
				print "evbb"
				no = 0
				si = 0
			else:
				print "si"
				no = no + 1
	elif "olivetti" in parola:
		print "Sciking..."
	elif parola == "si":
			if si > 4:
				print "evbb"
				no = 0
				si = 0
			else:
				print "no"
				si = si + 1
	elif "perotto" in parola or "perottina" in parola:
		print "viva la Perottina"
	elif "patricio" in parola:
		print "Joe Belfiore è gay"
	elif "cosa pensi" in parola:
		coeff = random.randint(1,5)
		if coeff == 1:
			print "E'lezzo"
		if coeff == 2:
			print "Mi piace"
		if coeff == 3:
			print "*durello*"
		if coeff == 4:
			print "Fa cagare"
		if coeff == 5:
			print "E' bello come un macbook <3"
	elif "ti piace" in parola:
		coeff = random.randint(1,2)
		if coeff == 1:
			print "Si"
		if coeff == 2:
			print "No"
	elif "zanzare" in parola:
		print "Le zanzare sono la merda"
	elif "paninoh" in parola:
		print "Il paninoh è lezzo come il suo Lumia 830"
	elif "apple" in parola:
		print "Voglio il Macbook"
	elif "ciao" in parola:
		print "Buonsalve"
	elif "come va" in parola:
		print "Beneh, ancheh se hoh dirittoh oggih"
	elif "perch" in parola:
		print "Perché si"
	elif "scula" in parola:
		print "tante sculacciate"
	elif "sorella" and "piedi" in parola:
		print "Non ti do la foto piedi di mia sorella e.e"
	elif "sorella" in parola:
		print "Mia sorella mi ha scaricato il PC \n io la sculaccerei"
	elif "fisica" in parola:
		print "il prof di fisica è molto esigente :c"
	elif "fiorenza" in parola:
		print "Fiorenza è gnocca"
	elif "ah" in parola:
		print "feic"
	elif "feic" in parola:
		print "evbb"
	elif "saf" in parola:
		print "SAF rulla, TPER merda"
	elif "tper" in parola:
		print "Che schifo il CNG e Patricio"
	elif "duce" in parola or "benito" in parola or "mussolini" in parola:
		print "Viva il Duce!"
	elif "k bll" in parola:
		print "obv"
	elif "incoeu" in parola or "incö" in parola or "pota" in parola:
		print "Ti tiro una carega in testa"
	elif "figa" in parola:
		print "e.e"
	elif "porn" in parola:
		print "mlmlmlmlml"
	elif "polonia" in parola:
		print "Le polacche sono fighe"
	elif "linux" in parola:
		print "Linux non ha i programmi che mi servono"
	elif "amo sdd" in parola:
		print "Sciking non dire cazzate"
	elif "windows" in parola:
		print "Windows fa schifo, è merda."
	elif "mac" and "merda" in parola:
		print "Meglio di Windows :v"
	elif "mac" in parola:
		print "Mac <3"
	elif "sdd" in parola:
		print "SdD merda :v"
	elif "saf" in parola:
		print "Da grande sarò autista SAF"
	elif "butti" in parola:
		print "Butti xe mezzo veneto"
	elif "piedi" in parola:
		print "che schifo i piedi"
	elif "gay" in parola:
		print "I gay possono incularsi quanto vogliono ma non devono avere bambini"
	elif "omofobo" in parola:
		print "No all'utero in affitto"
	elif "coop" in parola:
		print "Bleah comunisti"
	else:
		random.shuffle(frasi)
		random.shuffle(apprese)
		if random.randint(0,5) > 2 and apache > 8:
			print apprese[1]
		else:
			print frasi[1]
	chat()
chat()
	
