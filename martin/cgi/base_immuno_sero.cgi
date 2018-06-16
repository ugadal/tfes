#!/usr/bin/env python
# -*- coding: utf-8 -*-

#  Base immu-serologie

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


hr="<hr/>"
br="<br/>"


print '''<meta charset="UTF-8">'''
print """<h1><font color="#BD8D46">LBH</font></h1>"""
print """ <h2 align="right"> Bonjour !</h2>"""

print hr
print """<center><h1><font color='green'>Les examens medicaux de l'IMPM </font></h1></center>"""
print hr


print """<h2><i><font color="blue">FICHE DE PAILLASE (IMMUNO/SEROLOGIE)</font></i></h2><br/>"""



import sqlite3
C = sqlite3.connect('db/impm.db')
c=C.cursor()

c.execute("select count(ID_patient) from immuno_serologie")
b=int(c.fetchall()[0][0])

c.execute("""INSERT INTO immuno_serologie(ID_patient,date,type_examen,ag_hbs,ac_hcv,aslo,crp,hiv_det,hiv_im,chlamy,tpha,vdrl,widal) 
VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)
""",(ID_patient,dat_jour,type_examen,ag_hbs,ac_hcv,aslo,crp,hiv_det,hiv_im,chlamy,tpha,vdrl,widal))

C.commit() 
c.execute("select count(ID_patient) from immuno_serologie")
R=int(c.fetchall()[0][0])
if R>b:
	print "Vos donnees ont ete bien enregistre<br/> Le Nombre de patient enregistre en immuno_serologie est de: <b> %s </b>"%R
else:
	print """Vos donnees ne se sont pas enre
	gistre, Veuillez recommencer"""


print br,br,hr
################################################

print """
	<p><b><font color="red">Vous n'avez pas selectionne un examen. 
	Cliquez sur Ici pour revenir au point de depart</font></b></p>
	<form action="../index.html" enctype="multipart/form-data">
	<button type="submit">Ici</button>

"""

