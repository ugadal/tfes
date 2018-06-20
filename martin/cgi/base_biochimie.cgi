#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Base Biochimie

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

print '''<meta charset="UTF-8">'''
print """<h1><font color="#BD8D46">LBH</font></h1>"""
print """ <h2 align="right"> Bonjour !</h2>"""

print hr
print """<center style="background-color:#D0A9F5;><h1><font color='green'>Les examens medicaux de l'IMPM </font></h1></center>"""
print hr


print """<h2><i><font color="blue">FICHE DE PAILLASE (BIOCHIMIE)</font></i></h2><br/>"""




import sqlite3
C = sqlite3.connect('db/impm.db')
c=C.cursor()

c.execute("select count(date) from biochimie")
b=int(c.fetchall()[0][0])

c.execute("""INSERT INTO biochimie(ID_patient,date,type_examen,S_uree,S_creat,S_gluc,S_ac_ur,S_chol_t,S_sdl,S_ldl,S_tg,E_got,E_gpt,I_na,I_k,I_cl,I_ca,I_mg) 
VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);
""",(ID_patient,dat_jour,type_examen,S_uree,S_creat,S_gluc,S_ac_ur,S_chol_t,S_sdl,S_ldl,S_tg,E_got,E_gpt,I_na,I_k,I_cl,I_ca,I_mg))

C.commit() 

c.execute("select count(date) from biochimie")
R=int(c.fetchall()[0][0])
if R>b:
	print "Vos donnees ont ete bien enregistre<br/> Le Nombre de patient enregistre en biochimie est de: <b> %s </b>"%R
else:
	print """Vos donnees ne se sont pas enregistre, Veuillez recommencer"""

print br,br,br,hr,br

###################################
print """
	<p><b><font color="red"><br/>
	Cliquez sur le bouton pour effectuer une nouvelle analyse sur le meme patient</font></b></p>
	<form action="ancien_patient.cgi" enctype="multipart/form-data">
	<button type="submit">Nouvelle analyse</button>
	<input type="hidden" name="ID_patient" value="%s">
	</form>
"""%ID_patient,br,br


print """
	<p><b><font color="red">Vous avez terminé l'opération avec ce patient.<br/>
	Cliquez sur Accueil pour revenir au point de depart</font></b></p>
	<form action="../index.html" enctype="multipart/form-data">
	<button type="submit">Accueil</button>
	</form>
"""




