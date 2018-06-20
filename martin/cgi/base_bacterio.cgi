#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import cgi
import os

print "Content-type:text/html"
print

dataform=cgi.FieldStorage()

ID_patient=dataform.getvalue("ID_patient")
mm=dataform.getvalue("mm")
dd=dataform.getvalue("dd")
yyyy=dataform.getvalue("yyyy")

dat_jour="%s/%s/%s"%(yyyy,mm,dd)
type_examen=str(dataform.getvalue("type_examen"))

macroscopie=str(dataform.getvalue("macroscopie"))
etat_frais=str(dataform.getvalue("etat_frais"))
comptage_cellules=dataform.getvalue("comptage_cellules")
coloration_gram=str(dataform.getvalue("coloration_gram"))
coloration_ziehl=str(dataform.getvalue("coloration_ziehl"))
milieu_culture=str(dataform.getvalue("milieu_culture"))
observation=str(dataform.getvalue("observation"))
conclusion=str(dataform.getvalue("conclusion"))


hr="<hr/>"
br="<br/>"




print '''<meta charset="UTF-8">'''
print """<h1><font color="#BD8D46">LBH</font></h1>"""
print """ <h2 align="right"> Bonjour!</h2>"""

print hr
print """<center style="background-color:#D0A9F5;><h1><font color='green'>Les examens medicaux de l'IMPM </font></h1></center>"""
print hr


print """<h2><i><font color="blue">FICHE DE PAILLASE (BACTERIOLOGIE)</font></i></h2><br/>"""

print hr

print ID_patient


import sqlite3
C=sqlite3.connect("db/impm.db")
c=C.cursor()


c.execute("select count(id) from bacteriologie")
b=int(c.fetchall()[0][0])

c.execute("""INSERT INTO bacteriologie(ID_patient,date,type_examen,macroscopie,etat_frais,comptage_cellules,coloration_gram,coloration_ziehl,milieu_culture,observation,conclusion) 
VALUES (?,?,?,?,?,?,?,?,?,?,?);
""",(ID_patient,dat_jour,type_examen,macroscopie,etat_frais,comptage_cellules,coloration_gram,coloration_ziehl,milieu_culture,observation,conclusion))

C.commit() 


c.execute("select count(id) from bacteriologie")
R=int(c.fetchall()[0][0])
if R>b:
	print "Vos donnees ont ete bien enregistre<br/> Le Nombre de patient enregistre en bactériologie est de: <b> %s </b>"%R
else:
	print """Vos donnees ne se sont pas enregistre, Veuillez recommencer"""


print br,br,br,hr,hr,br

###################################
print """
	<p><b><font color="green"><br/>
	Cliquez sur le bouton pour effectuer une nouvelle analyse sur le meme patient</font></b></p>
	<form action="ancien_patient.cgi" enctype="multipart/form-data">
	<input type="hidden" name="ID_patient" value="%s">
	<button type="submit">Nouvelle analyse</button>
	</form>
	"""%ID_patient

print br,br


print """
	<p><b><font color="red">Vous avez terminé l'opération avec ce patient.<br/>
	Cliquez sur Accueil pour revenir au point de depart</font></b></p>
	<form action="../index.html" enctype="multipart/form-data">
	<button type="submit">Accueil</button>
	</form>
	"""







#~ import pymysql
#~ C=pymysql.connect("localhost","root","zz","bacterio")
#~ #reseau,nom d'utilisateur,mot de passe,nom de la base de donnee)
#~ c=C.cursor()
#~ c.execute("select count(nom) from patient")
#~ b=int(c.fetchall()[0][0])

#~ c.execute("INSERT INTO patient(nom,prenom,age,sexe,ville,quartier,dat_jour,type_examen,macroscopie,etat_frais,comptage_cellules,coloration_gram,cloration_ziehl,milieu_culture,observation,conclusion,email,technicien) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);",(nom,prenom,age,sexe,ville,quartier,dat,type_examen,macroscopie,etat_frais,comptage_cellules,coloration_gram,cloration_ziehl,milieu_culture,observation,conclusion,email,username))

#~ c.execute("select count(nom) from patient")
#~ R=int(c.fetchall()[0][0])
#~ if R>b:
	#~ print "Vos donnees ont ete bien enregistre<br/> Le Nombre de patient enregistre est de: <b> %s </b>"%R
#~ else:
	#~ print """Vos donnees ne se sont pas enre
	#~ gistre, Veuillez recommencer"""

#~ c.execute("select * from patient")
#~ D=int(c.fetchall())
#~ print D

