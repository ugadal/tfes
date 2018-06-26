#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import cgi
import sqlite3 as sql
C=sql.connect("db/impm.db")
c=C.cursor()
f=cgi.FieldStorage()

print "Content-type:text/html"
print

print """<h2>Introduir un nouveau patient</h2>"""

print '''<meta charset="UTF-8">
<form action="registpatient.py" enctype="multipart/form-data"> 

 <fieldset>
                <input  type="text"  id="patientnom" name="nom" placeholder="Nom du patient" value="" maxlength="32" required >
                <input  type="text"  id="patientprenom" name="prenom" placeholder="Prenom" aria-label="prenom" value="" maxlength="32"  required>
                 
                 <select type="select" name="sexe" required>
                 <option value="Sexe" selected disabled>Sexe du patient</option>
                 <option value="F">Feminin</option>
                 <option value="M">Masculin</option>
                 </select>
                 <input type="tel" pattern="[0-9-() ]*" name="age"   value=""  required role="textbox" aria-multiline="false" placeholder="Age" aria-label="age"  minlength="1" maxlength="3">
                <br/>
 </fieldset>
 
 <fieldset>
	<input type="text" name="ville" value="" placeholder="ville" required>		
	<input type="text" name="quartier" value="" placeholder="Quartier" required>
	<input type="text" name="tel" value="" placeholder="Telephone"><br/>
 </fieldset> 
 <input type="hidden" name="exam" value="%s">
 '''

print """ <input type="text" name="email"  id="usernamereg-yid" placeholder="Adresse mail"
            aria-label="Adresse mail" value="" maxlength="32"   ><br/><br/>
       
       <button onclick="registpatient(id)">Enregistrer</button>   
        
</form>
"""
