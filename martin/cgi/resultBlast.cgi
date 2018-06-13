#!/usr/bin/env python
# -*- coding: utf-8 -*-


import cgi
import os
import shelve
from db import *

print "Content-type:text/html"
print
br="<br>"
hr="<hr>"

et="*"
Me=et*250

print hr
print hr
dataform=cgi.FieldStorage()
resultBlast=dataform.getvalue("bank")
nom=dataform.getvalue("id")
ftir="/tmp/%s.shelve"%nom                           # Variable qui stock les shelves (Creation d'un tiroir)
tir=shelve.open(ftir)                               # Ouverture du tiroir
if type(resultBlast)!=type([]):resultBlast=[resultBlast]
tir["bank"]=resultBlast
blast_type=tir["blast_type"] # essentiel !!

typebank=DP[blast_type][2]
#~ typeseq=tir["typeseq"]	
fn=tir["fn"]

dblisfn="/tmp/%s.%sal"%(nom,typebank.lower())

print "<h1>Le resultat de mon BLAST</h1>",br,Me

fo=open(dblisfn,"w") #file out
titledblist="TITLE "
if len(resultBlast)>1:titledblist+="temporary collection of "+" + ".join(resultBlast)
else:titledblist+=resultBlast[0]
fo.write(titledblist)
fo.write("\n")


listepath=[DB[x][2] for x in resultBlast]
bl=" ".join(listepath) #bank list
fo.write("DBLIST "+bl+"\n")
fo.close()
cmd="blastall -p %s -d /tmp/%s -i /tmp/%s.seq -a 4 -T T"%(blast_type,nom,nom)
fc=os.popen(cmd)
fd=fc.read()
print fd






