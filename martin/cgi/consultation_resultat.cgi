#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
import cgi
import os

print "Content-type:text/html"
print


hr="<hr/>"
br="<br/>"

print '''<meta charset="UTF-8">'''
print """<h1><font color="#BD8D46">LBH</font></h1>"""
print """ <h2 align="right"> Bonjour!</h2>"""
print hr,hr


print '''<form action="base.cgi" enctype="multipart/form-data" required>
	
  <p><font color="blue">Veuillez selectionner un type d'examen svp :</font></p>
  
    <input type="radio" id="bac"
     name="exam" value="bacterio">
    <label for="bac">Bacteriologie</label><br/>

    <input type="radio" id="bio"
     name="exam" value="biochimie">
    <label for="bio">Biochimie</label><br/>

    <input type="radio" id="hema"
     name="exam" value="hemato">
    <label for="hema">Parasito/Hematologie</label><br/>
    
    <input type="radio" id="immuno"
     name="exam" value="immuno">
    <label for="immuno">Immuno_serologie</label><br/>
    
    
    <button type="submit">Suivant</button>
    
</form>'''
