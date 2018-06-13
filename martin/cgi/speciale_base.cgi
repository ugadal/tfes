#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

#Base speciale

import cgi
import os

print "Content-type:text/html"
print




dataform=cgi.FieldStorage()
ID=dataform.getvalue("id")
nom=dataform.getvalue("nom")
val=dataform.getvalue("val")
base=dataform.getvalue("type_examen")







#######################################################################################################
print """<h1><font color="#BD8D46"><img src="/root/BLOC3/vac/impm-logo.jpg">LBH</font></h1>"""
print """ <h2 align="right"> Bonjour !</h2>"""

print "<hr/>"
print """<center><h1><font color='green'>Les examens medicaux de l'IMPM </font></h1></center>"""
print "<hr/>"

#######################################################################################################




print """<h2><i><font color="blue">RESULTAT DES FICHES DE PAILLASE (BACTERIOLOGIE)</font></i></h2><br/>"""



print """<fieldset style="background-color:yellow;">
	<p><b><font color="green">cliquez sur EXAMENS pour revenir a la page de selection des examens</font></b></p>"""
	
print """
<form action="base_examen.cgi" enctype="multipart/form-data">
<button type="submit">EXAMENS</button>
<input type="hidden" name="username" value="%s"><br/><br/>
</fieldset>
"""



import pymysql


if val=="nom":
	C=pymysql.connect("localhost","root","zz",base)
	c=C.cursor()

	li1=[]
	c.execute("describe patient")
	D=c.fetchall()
	for j in D:
		li1.append(j[0])

	print "<br/>"
	print "<br/>"

	c.execute("""select * from patient where nom='%s' ORDER BY id DESC """%nom)
	b=c.fetchall()

	print """ <body style="background-color:#FBEFF2;"><center> """

	for row in b:
		print "<caption>Resultat </caption>"
		print "<table border=2 cellspacing=5 cellpadding=2>"
		print "<tr>"
		for i in range(len(row)):
			print """<th style="background-color:powderblue;">""",li1[i],"</th>","""<td style="background-color:#00FF80;">""", row[i],"</td>","</tr>"
		
		print "</table>"	
		print "<br/><br/><br/><br/>"

	print """</center></body>"""	
	
	
elif val=="ID":
	C=pymysql.connect("localhost","root","zz",base)
	c=C.cursor()

	li1=[]
	c.execute("describe patient")
	D=c.fetchall()
	for j in D:
		li1.append(j[0])

	print "<br/>"
	print "<br/>"

	c.execute("""select * from patient where id=%s """%ID)
	b=c.fetchall()

	print """ <body style="background-color:#FBEFF2;"><center> """

	for row in b:
		print "<caption>Resultat </caption>"
		print "<table border=2 cellspacing=5 cellpadding=2>"
		print "<tr>"
		for i in range(len(row)):
			print """<th style="background-color:powderblue;">""",li1[i],"</th>","""<td style="background-color:#00FF80;">""", row[i],"</td>","</tr>"
		
		print "</table>"	
		print "<br/><br/><br/><br/>"

	print """</center></body>"""

else:
	print """<p><b><font color="red">Vous n'avez pas fait de selection !</font></b></p>"""
