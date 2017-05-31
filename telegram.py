#!/usr/bin/ python-
# -*- coding: utf-8 -*-
import telepot
import sys
import os
import time
import pprint
import unicodedata
import subprocess
import string
import random

TOKEN = 'TOKEN'
bot = telepot.Bot(TOKEN)

def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type == 'text':
        name = msg["from"]["first_name"]
        txt = msg['text']
        helab = str.lower(unicodedata.normalize('NFKD', txt).encode('ascii','ignore'))
    no = 0
    apache = 0
    si = 0
    apprese = ["Ma che ooooh", "L'Arway del Duce über alles","Panino puzza :v"]
    frasi = ["Viva le pantofole","io ti denuncerei", "ciabatte merda","ROM föra di ball","si","no", "Kurumo lezzo", "Mia sorella mi ha rotto l'iPad porcodio", "Panino mi ha mandato a cagare :c","Sono su YouPorn","Fiorenza è bellissima","e.e","Tu sei segoe","Porcoddio","Mi fanno domande pervertite su ask :c","Tante sculacciate","Mai più Windows","Non proverò Linux","Perotto è grande","Ah","k bll","830 merda","il 735 di mia sorella è bellissimo","che schifo i piedi",]
    global apache
    apache = apache + 1
    global no
    global apprese
    global frasi
    global si
    if helab != "" and "dalan" not in helab and "dalagn" not in helab and "dolan" not in helab:
            apprese.append(helab)
    if "pantofole" in helab:
        bot.sendMessage(chat_id, "Viva le pantofole")
    elif "pantofole" in helab and "merda" in helab:
        bot.sendMessage(chat_id, "Scarpe in casa merda")
    elif "renzi" in helab:
        bot.sendMessage(chat_id, "Renzi mona")
    elif "kurumo"  in helab:
        bot.sendMessage(chat_id, "688 merda")
    elif "neoplan" in helab:
        bot.sendMessage(chat_id, "Neoplan Merda")
    elif "arway" in helab:
        bot.sendMessage(chat_id, "Arway regna")
    elif helab == "no":
    	if no > 4:
    	    bot.sendMessage(chat_id, "evbb")
            no = 0
            si = 0
        else:
            bot.sendMessage(chat_id, "sì")
            no = no + 1  
    elif "olivetti" in helab:
        bot.sendMessage(chat_id, "Sciking...")
    elif helab == "si":
        if si > 4:
            bot.sendMessage(chat_id, "evbb")
            no = 0
            si = 0
        else:
            bot.sendMessage(chat_id, "no")
            si = si + 1
    elif "perotto" in helab or "perottina" in helab:
        bot.sendMessage(chat_id, "viva la Perottina")
    elif "patricio" in helab:
        bot.sendMessage(chat_id, "Joe Belfiore è gay")
    elif "cosa pensi" in helab:
            coeff = random.randint(1,5)
            if coeff == 1:
                bot.sendMessage(chat_id, "È lezzo")
            if coeff == 2:
                bot.sendMessage(chat_id, "Mi piace")
            if coeff == 3:
                bot.sendMessage(chat_id, "*durello*")
            if coeff == 4:
                bot.sendMessage(chat_id, "Fa cagare")
            if coeff == 5:
                bot.sendMessage(chat_id, "E' bello come un macbook <3")
    elif "ti piace" in helab:
            coeff = random.randint(1,2)
            if coeff == 1:
                bot.sendMessage(chat_id, "Si")
            if coeff == 2:
                bot.sendMessage(chat_id, "No")
    elif "zanzare" in helab:
        bot.sendMessage(chat_id, "Le zanzare sono la merda")
    elif "paninoh" in helab:
        bot.sendMessage(chat_id, "Il paninoh è lezzo come il suo Lumia 830")
    elif "apple" in helab:
        bot.sendMessage(chat_id, "Voglio il Macbook")
    elif "ciao" in helab:
        bot.sendMessage(chat_id, "Buonsalve")
    elif "come va" in helab:
        bot.sendMessage(chat_id, "Beneh, ancheh se hoh dirittoh oggih")
    elif "perch" in helab:
        bot.sendMessage(chat_id, "Perché si")
    elif "scula" in helab:
        bot.sendMessage(chat_id, "tante sculacciate")
    elif "sorella" and "piedi" in helab:
        bot.sendMessage(chat_id, "Non ti do la foto piedi di mia sorella e.e")
    elif "sorella" in helab:
        bot.sendMessage(chat_id, "Mia sorella mi ha scaricato il PC \n io la sculaccerei")
    elif "fisica" in helab:
        bot.sendMessage(chat_id, "il prof di fisica è molto esigente :c")
    elif "fiorenza" in helab:
        bot.sendMessage(chat_id, "Fiorenza è gnocca")
    elif "ah" in helab:
        bot.sendMessage(chat_id, "feic")
    elif "feic" in helab:
        bot.sendMessage(chat_id, "evbb")
    elif "saf" in helab:
        bot.sendMessage(chat_id, "SAF rulla, TPER merda")
    elif "tper" in helab:
        bot.sendMessage(chat_id, "Che schifo il CNG e Patricio")
    elif "duce" in helab or "benito" in helab or "mussolini" in helab:
        bot.sendMessage(chat_id, "Viva il Duce!")
    elif "k bll" in helab:
        bot.sendMessage(chat_id, "obv")
    elif "incoeu" in helab or "incö" in helab or "pota" in helab:
        bot.sendMessage(chat_id, "Ti tiro una carega in testa")
    elif "figa" in helab:
        bot.sendMessage(chat_id, "e.e")
    elif "porn" in helab:
        bot.sendMessage(chat_id, "mlmlmlmlml")
    elif "polonia" in helab:
        bot.sendMessage(chat_id, "Le polacche sono fighe")
    elif "linux" in helab:
        bot.sendMessage(chat_id, "Linux non ha i programmi che mi servono")
    elif "amo sdd" in helab:
        bot.sendMessage(chat_id, "Sciking non dire cazzate")
    elif "windows" in helab:
        bot.sendMessage(chat_id, "Windows fa schifo, è merda.")
    elif "mac" and "merda" in helab:
        bot.sendMessage(chat_id, "Meglio di Windows :v")
    elif "mac" in helab:
        bot.sendMessage(chat_id, "Mac <3")
    elif "sdd" in helab:
        bot.sendMessage(chat_id, "SdD merda :v")
    elif "saf" in helab:
        bot.sendMessage(chat_id, "Da grande sarò autista SAF")
    elif "butti" in helab:
        bot.sendMessage(chat_id, "Butti xe mezzo veneto")
    elif "piedi" in helab:
        bot.sendMessage(chat_id, "che schifo i piedi")
    elif "gay" in helab:
        bot.sendMessage(chat_id, "I gay possono incularsi quanto vogliono ma non devono avere bambini")
    elif "omofobo" in helab:
        bot.sendMessage(chat_id, "No all'utero in affitto")
    elif "coop" in helab:
        bot.sendMessage(chat_id, "Bleah comunisti")
    elif "m8" in helab:
        bot.sendMessage(chat_id, "Patricio...")
    elif "mdd" in helab:
        bot.sendMessage(chat_id, "Ho riacceso il Wi-Fi")
    elif "hamer" in helab:
        bot.sendMessage(chat_id, "Hamer è un ciarlatano di merda, lo ammazzerei con le mie mani")
    elif "eri hameriano" in helab:
        bot.sendMessage(chat_id, "Ero ingenuo :(")
    elif "alex" in helab:
        bot.sendMessage(chat_id, "Che schifo il bisex")
    elif "jorji" in helab:
        bot.sendMessage(chat_id, "Gloria ad Arstotzka")
    else:
        random.shuffle(frasi)
        random.shuffle(apprese)
        if random.randint(0,5) > 2 and apache > 8:
            bot.sendMessage(chat_id, apprese[1])
        else:
            bot.sendMessage(chat_id, frasi[1])
bot.message_loop(on_chat_message)
while 1:
    time.sleep(5)
