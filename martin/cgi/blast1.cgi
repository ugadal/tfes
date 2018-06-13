#!/usr/bin/env python
# -*- coding: utf-8 -*-


import cgi
import os
import uuid


print "Content-type:text/html"
print
br="<br>"
hr="<hr>"
dataform=cgi.FieldStorage()
blast_type=dataform.getvalue("type")
nom=dataform.getvalue("id")

et="*"
Me=et*250


print """<h1>LES BANKS <h1/>"""

bla=["blastp","blastx","tblastn","blastn","tblastx"]
for i in range(len(bla)):
	if blast_type==bla[i]:
		bt=bla[i]
		print bt,br,hr
bt=bt
p='''
Choisir une BANK<br>
<form name=mm action=resultBlast.cgi method=post enctype="multipart/form-data">
<input type=checkbox name=bank value="swissprot" > La bank SWISSPROT <br>
<input type=checkbox name=bank value="yprot" > La bank YPROT<br>
<input type=checkbox name=bank value="nt" >La bank NT<br><br>
<input type="hidden" name="id" value="%s">
<input type="hidden" name="bt" value="%s">
<input type=submit value="Envoyer">
</form> '''%(nom,bt)

n='''Choisir une Bank <br>
<form name=mm action=resultBlast.cgi method=post enctype="multipart/form-data">
<input type=checkbox name=bank value="bct" > La bank BCT <br>
<input type=checkbox name=bank value="ydna" > La bank ydna<br>
<input type="hidden" name="id" value="%s">
<input type="hidden" name="bt" value="%s">
<input type=submit value="Envoyer">
</form> '''%(nom,bt)


if blast_type=="blastp" or blast_type=="blastx":
        print p
if blast_type=="tblastn" or blast_type=="blastn" or blast_type=="tblastx":
        print n
        


