#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

#MES EXAMENS

import cgi
import os

print "Content-type:text/html"
print

dataform=cgi.FieldStorage()
username=dataform.getvalue("username")
password=dataform.getvalue("password")

et="*"
Me=et*200
hr="<hr/>"
br="<br/>"


print """<h1><font color="#BD8D46">LBH</font></h1>"""
print """ <h2 align="right"> Bonjour %s !</h2>"""%username

print hr
print """<center ><h1><font color='green'>Les examens medicaux de l'IMPM </font></h1></center>"""
print hr


A= '''<form  action="fiche_paillasse.cgi" enctype="multipart/form-data">
			
		  <p><font color="blue">Veuillez selectionner un type d'examen svp :</font></p>
		  
			<input type="radio" id="bac"
			 name="exam" value="bacterio">
			<label for="bac">Bacteriologie</label><br/>

			<input type="radio" id="bio"
			 name="exam" value="biochimie">
			<label for="bio">Biochimie</label><br/>

			<input type="radio" id="hema"
			 name="exam" value="hemato">
			<label for="hema">Parasito /Hematologie</label><br/>
			
			<input type="radio" id="immuno"
			 name="exam" value="immuno">
			<label for="immuno">Immuno-serologie</label><br/>
			
		  
			
			<button type="submit">Suivant</button>
			
			<input type="hidden" name="username" value="%s">
		</form>'''%username



B=""" <html>
		 <head>
			<title>Analyses_medicales_IMPM</title>
			<meta charset="UTF-8">
			<link rel="stylesheet" href="style.css">
		 </head> 
	  
		<body>
		  
		<form method="post" action="../accueil.html" enctype="multipart/form-data" >	
			
			<INPUT type="submit" value="Ici"> <br/><!---pour se connecter --->
		</FORM>
		</body>
		</html>  """






import pymysql
C=pymysql.connect("localhost","root","zz","identification")
c=C.cursor()
c.execute("select pseudo, password from technicien;")
b=c.fetchall()

for row in b:
	ps,mp=row

	if ps==username and mp==password:
		print A
		exit()


print """<p><b><font color="red">Votre identification a echoue! Le pseudo ou le mot de passe est incorrecte</font></b></p> """
print "Cliquez sur Ici pour revenir a la page d'accueil. ",B		
		



  #~ <input type="radio" id="parosito"
     #~ name="exam" value="parasito">
    #~ <label for="para">Parasitologie</label><br/><br/>
