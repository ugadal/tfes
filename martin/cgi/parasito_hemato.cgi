#!/usr/bin/env python
# -*- coding: utf-8 -*-

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


print """<h1><font color="#BD8D46">LBH</font></h1>"""
print """ <h2 align="right"> Bonjour %s !</h2>"""%username

print hr
print """<center style="background-color:#D0A9F5;><h1><font color='green'>Les examens medicaux de l'IMPM </font></h1></center>"""
print hr


print """<h2><i><font color="blue">FICHE DE PAILLASE (PARASITOLOGIE / HEMATOLOGIE)</font></i></h2><br/>"""





import pymysql
C=pymysql.connect("localhost","root","zz","parasito_hemato")
#reseau,nom d'utilisateur,mot de passe,nom de la base de donnee)
c=C.cursor()
c.execute("select count(nom) from patient")
b=int(c.fetchall()[0][0])

c.execute("INSERT INTO patient(nom,prenom,age,sexe,ville,quartier,date,gs,rhesus,vs,tp,tca,ts,tx_reticul,goutte_ep,autre,nom_technicien) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);",(nom,prenom,age,sexe,ville,quartier,dat,gs,rhesus,vs,tp,tca,ts,tx_reticul,ge,autre,username))

c.execute("select count(nom) from patient")
R=int(c.fetchall()[0][0])
if R>b:
	print "Vos donnees ont ete bien enregistre<br/> Le Nombre de patient enregistre est de: <b> %s </b>"%R
else:
	print """Vos donnees ne se sont pas enre
	gistre, Veuillez recommencer"""

c.execute("select * from patient")
D=int(c.fetchall())
print D

