#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cgi
import os

print "Content-type:text/html"
print

dataform=cgi.FieldStorage()


mm=dataform.getvalue("mm")
dd=dataform.getvalue("dd")
yyyy=dataform.getvalue("yyyy")

type_examen=str(dataform.getvalue("type_examen"))
ID_patient=dataform.getvalue("ID_patient")
gs=str(dataform.getvalue("gs"))
rhesus=str(dataform.getvalue("rhesus"))
vs=dataform.getvalue("vs")
tp=dataform.getvalue("tp")
tca=dataform.getvalue("tca")
ts=dataform.getvalue("ts")
tx_reticul=dataform.getvalue("tx")
ge=dataform.getvalue("ge")
nb=dataform.getvalue("nb")
selle=dataform.getvalue("selle")
microfilaire=dataform.getvalue("microfilaire")
autre=str(dataform.getvalue("autre"))
mail=dataform.getvalue("mail")

dat="%s/%s/%s"%(yyyy,mm,dd)

et="*"
Me=et*200
hr="<hr/>"
br="<br/>"

print '''<meta charset="UTF-8">'''
print """<h1><font color="#BD8D46">LBH</font></h1>"""
print """ <h2 align="right"> Bonjour !</h2>"""

print hr
print """<center style="background-color:#D0A9F5;><h1><font color='green'>Les examens medicaux de l'IMPM </font></h1></center>"""
print hr


print """<h2><i><font color="blue">FICHE DE PAILLASE (PARASITOLOGIE / HEMATOLOGIE)</font></i></h2><br/>"""




import sqlite3
C = sqlite3.connect('db/impm.db')
c=C.cursor()

c.execute("select count(ID_patient) from hemato_parasitologie")
b=int(c.fetchall()[0][0])

c.execute("""INSERT INTO hemato_parasitologie(ID_patient,date,type_examen,gs,rhesus,vs,tp,tca,ts,tx_reticul,goutte_ep,autre) 
VALUES (?,?,?,?,?,?,?,?,?,?,?,?);
""",(ID_patient,dat,type_examen,gs,rhesus,vs,tp,tca,ts,tx_reticul,ge,autre))

C.commit() 


c.execute("select count(ID_patient) from hemato_parasitologie")
R=int(c.fetchall()[0][0])
if R>b:
	print "Vos donnees ont ete bien enregistre<br/> Le Nombre de patient enregistre est de: <b> %s </b>"%R
else:
	print """Vos donnees ne se sont pas enregistre, Veuillez recommencer"""

print br,br,br,hr,br

###################################
print """
	<p><b><font color="red">Vous avez terminé l'opération avec ce patient.<br/>
	Cliquez sur Accueil pour revenir au point de depart</font></b></p>
	<form action="../index.html" enctype="multipart/form-data">
	<button type="submit">Accueil</button>
	</form>
"""

