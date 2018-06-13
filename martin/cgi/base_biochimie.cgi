#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Base Biochimie

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

S_uree=dataform.getvalue("S_uree")
S_creat=dataform.getvalue("S_creat")
S_gluc=dataform.getvalue("S_gluc")
S_ac_ur=dataform.getvalue("S_ac_ur")
S_chol_t=dataform.getvalue("S_chol_t")
S_sdl=dataform.getvalue("S_sdl")
S_ldl=dataform.getvalue("S_ldl")
S_tg=dataform.getvalue("S_tg")
E_got=dataform.getvalue("E_got")
E_gpt=dataform.getvalue("E_gpt")
I_na=dataform.getvalue("I_na")
I_k=dataform.getvalue("I_k")
I_cl=dataform.getvalue("I_cl")
I_ca=dataform.getvalue("I_ca")
I_mg=dataform.getvalue("I_mg")

email=str(dataform.getvalue("email"))




hr="<hr/>"
br="<br/>"


print """<h1><font color="#BD8D46">LBH</font></h1>"""
print """ <h2 align="right"> Bonjour %s !</h2>"""%username

print hr
print """<center style="background-color:#D0A9F5;><h1><font color='green'>Les examens medicaux de l'IMPM </font></h1></center>"""
print hr


print """<h2><i><font color="blue">FICHE DE PAILLASE (BIOCHIMIE)</font></i></h2><br/>"""





import pymysql
C=pymysql.connect("localhost","root","zz","biochimie")
#reseau,nom d'utilisateur,mot de passe,nom de la base de donnee)
c=C.cursor()
c.execute("select count(nom) from patient")
b=int(c.fetchall()[0][0])

c.execute("INSERT INTO patient(nom,prenom,age,sexe,ville,quartier,dat_jour,type_examen,S_uree,S_creat,S_gluc,S_ac_ur,S_chol_t,S_sdl,S_ldl,S_tg,E_got,E_gpt,I_na,I_k,I_cl,I_ca,I_mg,email,technicien) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);",(nom,prenom,age,sexe,ville,quartier,dat_jour,type_examen,S_uree,S_creat,S_gluc,S_ac_ur,S_chol_t,S_sdl,S_ldl,S_tg,E_got,E_gpt,I_na,I_k,I_cl,I_ca,I_mg,email,username))

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


