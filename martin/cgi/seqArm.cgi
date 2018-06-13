#!/usr/bin/env python
# -*- coding: utf-8 -*-
#~ from db.py import *

#Importons les bibliothèques nécessaires
import shelve
import uuid
import os
import cgi

#Générons un identifiant aléatoire
ID=uuid.uuid1()

#Source des données de tous nos formulaires
from db import *

#mode html
print "Content-type:text/html"
print

#Récupération des données du formulaire
dataform=cgi.FieldStorage()
seqchamp=dataform.getvalue("seqchamp")
seqfile=dataform.getvalue("seqfile")

#initialisation du fichier de séquence
fn="/tmp/%s.seq"%ID

#Cmd pour trouver la taille et la nature de la séquence
cmd="infoseq -noheading -only -type %s 2>/dev/null" %fn
cmd1="infoseq -noheading -only -length %s 2>/dev/null" %fn

#Balise de début et de fin du formulaire
debutf="""<form method="post" nom="type d'analyse" action="prog.cgi">
<input type=hidden name=ID value=%s>"""%ID

finform="""<input type="submit" value="envoyer"/></form>"""

#Récupérons et trions la liste des clés du dictionnaire des programmes
ap=DP.keys()
ap.sort()

#Testons et choisissons la séquence entrée
laseq=seqchamp
if seqfile:laseq=seqfile
if not laseq:
	print "Attention une sequence !!!"
	print "veuillez au moins envoyer une sequence <a href=/seq.html> clicquez ici </a>"	
	exit()
	
#Ecrivons cette séquence dans le fichier fn
seq=open(fn,"w")
seq.write(laseq)
seq.close()

#Executons les commandes pour la taille et la nuture des commandes 
fc=os.popen(cmd)
ts=fc.readline().strip()
fc1=os.popen(cmd1)
ts1=fc1.readline().strip()

#Création d'un dictionnaire shelve pour la persistance des données
bk="/tmp/%s.db"%ID
backup=shelve.open(bk)
backup["type"]=ts
backup["longueur"]=ts1
backup["id"]=ID
backup.close()

#Affichage du premier message html
print "votre sequence est de type %s et de longueur %s!!!! <br>"%(ts,ts1) 

print "S'il vous plait les programmes de modelisation de sont pas encore operationnelles. Ne pas les choisir pour l'instant"

#Debut du nouveau formulaire
print debutf

#Contenu du formulaire
for tb in ap:
	d,tq,_=DP[tb]
	if tq==ts:print """<input type="radio" name="tblast" value=%s required>  %s  :  %s <br>"""%(tb,tb,d)

#fin du formulaire
print finform

