#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import cgi
import os

print "Content-type:text/html"
print




dataform=cgi.FieldStorage()
exam=dataform.getvalue("exam")
username=dataform.getvalue("username")



#######################################################################################################
print """<h1><font color="#BD8D46"><img src="/root/BLOC3/vac/impm-logo.jpg">LBH</font></h1>"""
print """ <h2 align="right"> Bonjour !</h2>"""

print "<hr/>"
print """<center style="background-color:#D0A9F5;"><h1><font color='green'>Les examens medicaux de l'IMPM </font></h1></center>"""
print "<hr/>"



#######################################################################################################









import pymysql

if exam=="bacterio":
	print """<h2><i><font color="blue">RESULTAT DES FICHES DE PAILLASE (BACTERIOLOGIE)</font></i></h2><br/>"""
	
	C=pymysql.connect("localhost","root","zz","bacterio")
	c=C.cursor()
	
	base="bacterio"

	li1=[]
	c.execute("describe patient")
	D=c.fetchall()
	for j in D:
		li1.append(j[0])

	print "<br/>"
	print "<br/>"

	c.execute("select * from patient ORDER BY id DESC")
	b=c.fetchall()
	
	print """<meta charset="UTF-8">
	<p>Afficher le resultat en fonction de l'ID ou du Nom</p>
	<form action="speciale_base.cgi" enctype="multipart/form-data">
	<fieldset>
	
	<input type="radio" id="bac"
     name="val" value="ID">
    <label for="bac">ID</label><br/>

    <input type="radio" id="bio"
     name="val" value="nom">
    <label for="bio">nom</label><br/>
	
	<input type="number" name="id" placeholder="id">	
	<input type="text" name="nom" value="" placeholder="Nom"><br/>
	<button type="submit">Rechercher</button>
	<input type="hidden" name="type_examen" value="%s">
	</fieldset> <br/>
	
	"""%base


elif exam=="biochimie":
	print """<h2><i><font color="blue">RESULTAT DES FICHES DE PAILLASE (BIOCHIMIE)</font></i></h2><br/>"""
	
	C=pymysql.connect("localhost","root","zz","biochimie")
	c=C.cursor()

	li1=[]
	c.execute("describe patient")
	D=c.fetchall()
	for j in D:
		li1.append(j[0])

	print "<br/>"
	print "<br/>"

	c.execute("select * from patient ORDER BY id DESC")
	b=c.fetchall()
	
	
	base="biochimie"
	print """<meta charset="UTF-8">
	<p>Afficher le resultat en fonction de l'ID ou du nom</p>
	<form action="speciale_base.cgi" enctype="multipart/form-data">
	<fieldset>
	
	<input type="radio" id="bac"
     name="val" value="ID">
    <label for="bac">ID</label><br/>

    <input type="radio" id="bio"
     name="val" value="nom">
    <label for="bio">nom</label><br/>
	
	<input type="number" name="id" placeholder="id">	
	<input type="text" name="nom" value="" placeholder="Nom"><br/>
	<button type="submit">Rechercher</button>
	<input type="hidden" name="type_examen" value="%s">
	</fieldset> <br/>
	
	"""%base


elif exam=="hemato":
	print """<h2><i><font color="blue">RESULTAT DES FICHES DE PAILLASE (PARASITOLOGIE / HEMATOLOGIE)</font></i></h2><br/>"""
	C=pymysql.connect("localhost","root","zz","parasito_hemato")
	c=C.cursor()

	li1=[]
	c.execute("describe patient")
	D=c.fetchall()
	for j in D:
		li1.append(j[0])
		#~ print j[0], "  || "

	print "<br/>"
	print "<br/>"

	c.execute("select * from patient ORDER BY id DESC")
	b=c.fetchall()
	
	base="parasito_hemato"
	print """<meta charset="UTF-8">
	<p>Afficher le resultat en fonction de l'ID ou du nom</p>
	<form action="speciale_base.cgi" enctype="multipart/form-data">
	<fieldset>
	
	<input type="radio" id="bac"
     name="val" value="ID">
    <label for="bac">ID</label><br/>

    <input type="radio" id="bio"
     name="val" value="nom">
    <label for="bio">nom</label><br/>
	
	<input type="number" name="id" placeholder="id">	
	<input type="text" name="nom" value="" placeholder="Nom"><br/>
	<button type="submit">Rechercher</button>
	<input type="hidden" name="type_examen" value="%s">
	</fieldset> <br/>
	
	"""%base
	


#~ elif exam=="parasito":
	#~ C=pymysql.connect("localhost","root","zz","parasitologie")
	#~ c=C.cursor()

	#~ li1=[]
	#~ c.execute("describe patient")
	#~ D=c.fetchall()
	#~ for j in D:
		#~ li1.append(j[0])

	#~ print "<br/>"
	#~ print "<br/>"

	#~ c.execute("select * from patient ORDER BY id DESC")
	#~ b=c.fetchall()


elif exam=="immuno":
	print """<h2><i><font color="blue">RESULTAT DES FICHES DE PAILLASE (IMMUNO/SEROLOGIE)</font></i></h2><br/>"""
	C=pymysql.connect("localhost","root","zz","immuno_serologie")
	c=C.cursor()

	li1=[]
	c.execute("describe patient")
	D=c.fetchall()
	for j in D:
		li1.append(j[0])
		#~ print j[0], "  || "

	print "<br/>"
	print "<br/>"

	c.execute("select * from patient ORDER BY id DESC")
	b=c.fetchall()
	
	base="immuno_serologie"
	print """<meta charset="UTF-8">
	<p>Afficher le resultat en fonction de l'ID ou du nom</p>
	<form action="speciale_base.cgi" enctype="multipart/form-data">
	<fieldset>
	
	<input type="radio" id="bac"
     name="val" value="ID">
    <label for="bac">ID</label><br/>

    <input type="radio" id="bio"
     name="val" value="nom">
    <label for="bio">nom</label><br/>
	
	<input type="number" name="id" placeholder="id">	
	<input type="text" name="nom" value="" placeholder="Nom"><br/>
	<button type="submit">Rechercher</button>
	<input type="hidden" name="type_examen" value="%s">
	</fieldset> <br/>
	
	"""%base
	
	
else:
	print """
	<p><b><font color="red">Vous n'avez pas selectionne un examen. 
	Cliquez sur Ici pour choisir un examen</font></b></p>"""
	
	print """
	<form action="base_examen.cgi" enctype="multipart/form-data">
	<button type="submit">Ici</button>
	<input type="hidden" name="username" value="%s">

	"""%username




#~ for row in b:
	#~ for i in range(len(row)):
		#~ print li1[i],"=", row[i], "<br/>"
		
	#~ print "<br/><br/><br/><br/>"


print """ <body style="background-color:#FBEFF2;"><center> """

for row in b:
	print "<caption>Resultat %s </caption>"%exam
	print "<table border=2 cellspacing=5 cellpadding=2>"
	print "<tr>"
	for i in range(len(row)):
		print """<th style="background-color:powderblue;">""",li1[i],"</th>","""<td style="background-color:#00FF80;">""", row[i],"</td>","</tr>"
	
	print "</table>"	
	print "<br/><br/><br/><br/>"

print """</center></body>"""	


#~ for row in b:
	#~ print "<caption>Resultat %s </caption>"%exam
	#~ print "<table border=2 cellspacing=5 cellpadding=2>"
	
	#~ for i in range(len(row)):
		
		#~ print "<tr>"
		#~ for j in range(len(li1)):
			#~ print """<th style="background-color:powderblue;">""",li1[j],"</th>"
		#~ print "</tr>"
	
	#~ for z in range(len(row)):
		#~ print "<tr>"
			
		#~ print """<td style="background-color:#00FF80;">""", row[z],"</td>"
	#~ print "</tr>"
	
	#~ print "</table>"	
	#~ print "<br/><br/><br/><br/>"

#~ print """</center></body>"""	

	

