#!/usr/bin/env python
# -*- coding: utf-8 -*-
#


import cgi
import os

print "Content-type:text/html"
print

dataform=cgi.FieldStorage()

nom=str(dataform.getvalue("nom"))
prenom=str(dataform.getvalue("prenom"))
sexe=str(dataform.getvalue("sexe"))
age=dataform.getvalue("age")
ville=str(dataform.getvalue("ville"))
quartier=str(dataform.getvalue("quartier"))
tel=str(dataform.getvalue("tel"))
email=str(dataform.getvalue("email"))

exam=dataform.getvalue("exam")


hr="<hr/>"
br="<br/>"

print '''<meta charset="UTF-8">'''
print """<h1><font color="#BD8D46">LBH</font></h1>"""
print """ <h2 align="right"> Bonjour!</h2>"""
print hr
#~ print """<center style="background-color:#D0A9F5;><h1><font color='green'>Les examens medicaux de la LBH </font></h1></center>"""
print hr

###########################################################################################################################
import sqlite3
C = sqlite3.connect('db/impm.db')
c = C.cursor()
c.execute ("""insert into patient(nom,prenom,sexe,age,ville,quartier,tel,email) 
VALUES(?,?,?,?,?,?,?,?)""", (nom,prenom,sexe,age,ville,quartier,tel,email))

C.commit() 

#~ try:
	#~ c.execute ("""insert into patient(nom,prenom,sexe,age,ville,quartier,tel,email) 
	#~ VALUES(?,?,?,?,?,?,?,?)""",(nom,prenom,sexe,age,ville,quartier,tel,email))

#~ except sqlite3.OperationalError as e:
	#~ print """Une erreur produite dans la requete : """ + str(e)



c.execute("select id from patient where nom='%s' and prenom='%s' and sexe='%s' and age=%s and ville='%s' and quartier='%s' and tel='%s' and email='%s' "
%(nom,prenom,sexe,age,ville,quartier,tel,email))

for i in c:
    print "\n", br
    for j in i:
        ID_patient=j
	
####################################################################################################################################

Examen="""<b><font color="coral">Votre patient à bien été enregisté. Veuillez cliquer sur suivant pour continer</font></b><br/><br/>
	<form name=mm action=%s.cgi method=post enctype="multipart/form-data">
	<button type="submit">Suivant</button>
	
	<input type="hidden" name="ID_patient" value=%s>

"""%(exam,ID_patient)

print Examen




