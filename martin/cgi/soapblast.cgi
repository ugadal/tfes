#!/usr/bin/python
import cgi
import os
import shelve
from SOAPpy import *
conn=SOAPProxy("http://localhost:3564")
br="<br>" 
hr="<hr>"
print "Content-type:text/html"
print
dataform=cgi.FieldStorage()
key=dataform.getvalue("ID")
banque=dataform.getvalue("banque")

tiroir=shelve.open("/tmp/%s.shelf"%key)
typblast=tiroir["typblast"]
filtre=tiroir["filtre"]
f=open("/tmp/%s.seq"%key)
seq=f.read()

retry="""Vous n'avez pas selectionner de banque veuillez submit et selectionner des banques <br>
<form name=mm action=blast.cgi method=post enctype="multipart/form-data">
<input type="hidden" name=ID value="%s">
<input type="hidden" name=type value="%s">
<input type=submit>
</form> """%(key,typblast)
if banque==None:
	print retry,br
	exit()
if type(banque) is str:banque=[banque]


r=conn.blast(filtre,typblast,seq,banque)
print r
