#!/usr/bin/python
# -*- coding: utf-8 -*-
#FORMULAIRE 

import cgi
import os
import uuid
import shelve
###################################################################################################
err="""<form method="post" action="seq.cgi" enctype="multipart/form-data" >	
		<INPUT type="file" name="file"><br>
		
		<label for="seq">Entrez une sequence FASTA</label><br/>
		<textarea id="seq" class="reset" rows="5" cols="80" name="QUERY"></textarea><br/><br/>
		
		<INPUT type="submit" value="Envoyer"> <br/><!---pour recuperer un fichier---><br/>
		<input type="reset" value="Effacer tout">
	</form> """
###################################################################################################
nom=uuid.uuid1()
ftir="/tmp/%s.shelve"%nom  # Variable qui stock les shelves (Création d'un tiroir)
tir=shelve.open(ftir)      # Ouverture du tiroir
fn="/tmp/%s.seq"%nom
info="/dev/null"

print "Content-type:text/html"
print
print
print "<hr>"

et="*"
Me=et*200
br="<br>"
hr="<hr>"

# Recuperation des sequences
dataform=cgi.FieldStorage()
fl1=dataform.getvalue("file")
#~ print fl1,hr
fl2=dataform.getvalue("QUERY")
#~ print fl2,hr

seq=fl2
if fl1:seq=fl1
while not seq:
	#~ print '<a href="/seq.html">Veuillez introduir une sequence svp</a>'
	
	print '<FONT color="red">Veuillez introduir une sequence </FONT>',br,err
	exit()

# Introduction de la sequence dans le fichier	
fo=open(fn, "w")	
fo.write(seq)
fo.close()

#Recuperation du type et de la longueur de ma sequence
############################################################################
cmd="infoseq -noheading -only -type -length %s 2>%s"%(fn,info)
res=os.popen(cmd)
typeseq,longseq=res.readline().strip().split()
msg="Proteine"
msg2="acides amines"
if typeseq=="N":
	msg="ADN"
	msg2="nucleotides"
print "votre sequence de type %s, de longueur %s %s"%(msg,longseq,msg2),br
############################################################################

#Introduir les valeurs dans le tiroir
tir["fn"]=fn
tir["typeseq"]=typeseq
tir["longseq"]=longseq

from db import *


print """<h1>MON BLAST</h1>"""
debut='''Choisir le type de BLAST <br>
<form name=mm action=blast.cgi method=post enctype="multipart/form-data">	
<input type="hidden" name="id" value="%s">'''%nom


fin="""<input type=submit value="Envoyer"></form> """

print debut

#Recuperation des clés du dictionnaire DP et le stocké dans ap
ap=DP.keys() #allprogram
ap.sort()

for tp in ap:                    #type programme
	d,tq,tb=DP[tp]               #description,type query,type banque
	if tq==typeseq:
		print """<input type=radio name=type value="%s" required >%s : %s <br>"""%(tp,tp,d)

print fin



