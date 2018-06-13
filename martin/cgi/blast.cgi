#!/usr/bin/env python
# -*- coding: utf-8 -*-


import cgi
import os
import shelve

print "Content-type:text/html"
print
br="<br>"
hr="<hr>"
###########################################################################################
dataform=cgi.FieldStorage()
blast_type=dataform.getvalue("type")
nom=dataform.getvalue("id")
ftir="/tmp/%s.shelve"%nom          # Variable qui stock les shelves (Creation d'un tiroir)
tir=shelve.open(ftir)              # Ouverture du tiroir
tir["blast_type"]=blast_type
###########################################################################################
et="*"
Me=et*250


print """<h1>LES BANQUES </h1>"""

from db import *

debut='''Choisir une BANQUE<br>
	<form name=mm action=resultBlast.cgi method=post enctype="multipart/form-data">
	<input type="hidden" name="id" value="%s">'''%nom
	
fin='''<input type=submit value="Envoyer"></form>'''

print debut,br

#Quelles banques pour le blast choisi ??
k,tq,tb=DP[blast_type]
ab=DB.keys()  #liste des cles de banques
ab.sort()     #Triage par ordre alphabetique
for unebanque in ab:
	name,typb,chemin=DB[unebanque]
	if typb==tb:
		print """<input type=checkbox name=bank value="%s" > %s <br>"""%(unebanque,name),br

print fin
        


