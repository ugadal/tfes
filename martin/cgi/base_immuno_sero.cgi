#!/usr/bin/env python
# -*- coding: utf-8 -*-

#  Base immu-serologie

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

dat_jour="%s/%s/%s"%(yyyy,mm,dd)
type_examen=str(dataform.getvalue("type_examen"))


ag_hbs=dataform.getvalue("ag_hbs")
ac_hcv=dataform.getvalue("ac_hcv")
aslo=dataform.getvalue("aslo")
crp=dataform.getvalue("crp")
hiv_det=dataform.getvalue("hiv_det")
hiv_im=dataform.getvalue("hiv_im")
chlamy=dataform.getvalue("chlamy")
tpha=dataform.getvalue("tpha")
vdrl=dataform.getvalue("vdrl")
widal=dataform.getvalue("widal")


email=str(dataform.getvalue("email"))


hr="<hr/>"
br="<br/>"



print """<h1><font color="#BD8D46">LBH</font></h1>"""
print """ <h2 align="right"> Bonjour %s !</h2>"""%username

print hr
print """<center><h1><font color='green'>Les examens medicaux de l'IMPM </font></h1></center>"""
print hr


print """<h2><i><font color="blue">FICHE DE PAILLASE (IMMUNO/SEROLOGIE)</font></i></h2><br/>"""





import pymysql
C=pymysql.connect("localhost","root","zz","immuno_serologie")
#reseau,nom d'utilisateur,mot de passe,nom de la base de donnee)
c=C.cursor()
c.execute("select count(nom) from patient")
b=int(c.fetchall()[0][0])

c.execute("INSERT INTO patient(nom,prenom,age,sexe,ville,quartier,dat_jour,type_examen,ag_hbs,ac_hcv,aslo,crp,hiv_det,hiv_im,chlamy,tpha,vdrl,widal,email,technicien) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);",(nom,prenom,age,sexe,ville,quartier,dat_jour,type_examen,ag_hbs,ac_hcv,aslo,crp,hiv_det,hiv_im,chlamy,tpha,vdrl,widal,email,username))

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

