#!/usr/bin/env python
# -*- coding: utf-8 -*-

#On importe les modules nécessaires
import shelve
import os
import cgi

#Format HTML
print "Content-type:text/html"
print

#Pour utiliser des données sur les banques
from db import *

#Récupération des variables du formulaire précédent
dataform=cgi.FieldStorage()
tbank=dataform.getvalue("tbank")
ID=dataform.getvalue("ID")

#Oubligeons le choix d'au moins une banque
if not tbank: 
	print " Vous de devez faire un choix !!! <a href=/prog.cgi> cliquez ici </a> "
	exit()
	
#Création des noms de fichiers nécessaires
resultat="/tmp/%s.res"%ID
fn="/tmp/%s.seq"%ID
bk="/tmp/%s.db"%ID
res="/tmp/%s.html"%ID

#Ouverture du fichier shelve pour récuperer le type de programme
backup=shelve.open(bk)
backup["tbank"]=tbank
tblast=backup["tblast"]
tbvpb=backup["tbvpb"]
backup.close()

#Nom du fichier allias
tpnal1=DP[tblast][2].lower()
tpnal=DP[tblast][2].lower()[1]
bal="/tmp/%s.%sal"%(ID,tpnal)   #bank alias file


#On teste les banques choisies
if type(tbank)==str: tbank=[tbank]
#conditions sur la nature des banques
cmd1="%s %s %s"%(tblast,fn,DB[tbank[0]][1])	
if tbvpb[0]=="F":
	res=os.popen(cmd1)
	resu=res.read()
	print resu
	exit()

#Première ligne de notre fichier allias
seq=open(bal,"w")
bl=", ".join(tbank)
seq.write("TITLE: fichier temporaire contenant les banques suivantes: %s\n"%bl)

#Deuxième ligne de notre banque allias
bl=" ".join([DB[x][1] for x in tbank])
seq.write("DBLIST %s\n"%bl)

#~ seq.write("\n")
seq.close()	
		
#Execution du blast	et des autres programmes		
cmd2="blastall -p %s -i %s -d /tmp/%s -a 4 -T T "%(tblast,fn,str(ID))
print cmd2
print "<hr>"
print bal
print "<hr>"

#Exécution du blast et affichage des résultats 
execblast=os.popen(cmd2)
resu=execblast.read()
print resu









