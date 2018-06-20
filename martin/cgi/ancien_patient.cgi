#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import cgi
import os

print "Content-type:text/html"
print

dataform=cgi.FieldStorage()

ID_patient=dataform.getvalue("ID_patient")

hr="<hr/>"
br="<br/>"

print '''<meta charset="UTF-8">'''
print """<h1><font color="#BD8D46">LBH</font></h1>"""
print """ <h2 align="right"> Bonjour!</h2>"""
print hr,hr

print """L'ID du patient est: %s"""%ID_patient,br,br,hr


print '''<form  action="infopatient.cgi" enctype="multipart/form-data" required>
			
		  <p><font color="blue">Veuillez selectionner un type d'examen svp :</font></p>
		  
			<input type="radio" id="bac"
			 name="exam" value="bacteriologie">
			<label for="bac">Bacteriologie</label><br/>

			<input type="radio" id="bio"
			 name="exam" value="biochimie">
			<label for="bio">Biochimie</label><br/>

			<input type="radio" id="hema"
			 name="exam" value="hemato_parasitologie">
			<label for="hema">Parasito /Hematologie</label><br/>
			
			<input type="radio" id="immuno"
			 name="exam" value="immuno_serologie">
			<label for="immuno">Immuno-serologie</label><br/>
			
		  
			
			<button type="submit">Suivant</button>
			<input type="hidden" name="ID_patient" value="%s">
		</form>'''%ID_patient
