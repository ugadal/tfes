#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import cgi
import os

print "Content-type:text/html"
print

dataform=cgi.FieldStorage()
username=str(dataform.getvalue("username"))
nom=str(dataform.getvalue("nom"))
prenom=str(dataform.getvalue("prenom"))
sexe=str(dataform.getvalue("sexe"))
age=dataform.getvalue("age")
ville=str(dataform.getvalue("ville"))
quartier=str(dataform.getvalue("quartier"))
mm=dataform.getvalue("mm")
dd=dataform.getvalue("dd")
yyyy=dataform.getvalue("yyyy")

dat="%s/%s/%s"%(yyyy,mm,dd)
type_examen=str(dataform.getvalue("type_examen"))

macroscopie=str(dataform.getvalue("macroscopie"))
etat_frais=str(dataform.getvalue("etat_frais"))
comptage_cellules=dataform.getvalue("comptage_cellules")
coloration_gram=str(dataform.getvalue("coloration_gram"))
coloration_ziehl=str(dataform.getvalue("cloration_ziehl"))
milieu_culture=str(dataform.getvalue("milieu_culture"))
observation=str(dataform.getvalue("observation"))
conclusion=str(dataform.getvalue("conclusion"))
email=str(dataform.getvalue("email"))


hr="<hr/>"
br="<br/>"


print """<h1><font color="#BD8D46">LBH</font></h1>"""
print """ <h2 align="right"> Bonjour %s !</h2>"""%username

print hr
print """<center style="background-color:#D0A9F5;><h1><font color='green'>Les examens medicaux de l'IMPM </font></h1></center>"""
print hr


print """<h2><i><font color="blue">FICHE DE PAILLASE (BACTERIOLOGIE)</font></i></h2><br/>"""

print hr


import sqlite3;

C=sqlite3.connect("db/example.db")

#reseau,nom d'utilisateur,mot de passe,nom de la base de donnee)
c=C.cursor()
c.execute("select count(nom) from bacteriologie")
b=int(c.fetchall()[0][0])

c.execute("INSERT INTO bacteriologie(nom,prenom,age,sexe,dat_jour,type_examen,macroscopie,etat_frais,comptage_cellules,coloration_gram,coloration_ziehl,milieu_culture,observation,conclusion) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?);",(nom,prenom,age,sexe,dat,type_examen,macroscopie,etat_frais,comptage_cellules,coloration_gram,coloration_ziehl,milieu_culture,observation,conclusion))

c.execute("select count(nom) from bacteriologie")
R=int(c.fetchall()[0][0])
if R>b:
	print "Vos donnees ont ete bien enregistre<br/> Le Nombre de patient enregistre est de: <b> %s </b>"%R
else:
	print """Vos donnees ne se sont pas enre
	gistre, Veuillez recommencer"""

c.execute("select * from bacteriologie")
D=int(c.fetchall())
print D









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

