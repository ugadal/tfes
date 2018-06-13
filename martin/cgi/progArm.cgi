#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Importons des bibliothèques nécessaires
import shelve
import cgi

#mode html
print "Content-type:text/html"
print

from db import *
#Récupération des données du formulaire
dataform=cgi.FieldStorage()
tblast=dataform.getvalue("tblast")
tbvpb=DP[tblast][2] #type banque voulues par le blast selectionne
ID=dataform.getvalue("ID")

#Ouverture du dictionnaire shelve pour la persistance des données
bk="/tmp/%s.db"%ID
backup=shelve.open(bk)
backup["tbvpb"]=tbvpb
backup["tblast"]=tblast
backup.close()

#Debut et fin du formulaire

debutf="""<form method="post" nom="type d'analyse" action="blast.cgi">
		  <input type=hidden name=ID value=%s>"""%ID
finform="""<input type="submit" value="envoyer"/></form>"""

#liste des banques triées
ab=DB.keys()
ab.sort()

#Affichage du nouveau formulaire
print """<h2> Liste des banques pour pour les sequences de type %s <h2>"""%tbvpb
print debutf
for tb in ab:
	d,bl,x=DB[tb]
	if x==tbvpb:
		print """<input type="checkbox" name="tbank" id="tbank" value=%s>  %s  :  %s <br>"""%(tb,tb,d)
print finform

