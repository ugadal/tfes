#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import cgi
import os

print "Content-type:text/html"
print

dataform=cgi.FieldStorage()
exam=str(dataform.getvalue("exam"))



hr="<hr/>"
br="<br/>"

####################################################################################################################################
print """<h1><font color="#BD8D46">LBH</font></h1>"""
print """ <h2 align="right"> Bonjour!</h2>"""

print hr
#~ print """<center style="background-color:#D0A9F5;><h1><font color='green'>Les examens medicaux de la LBH </font></h1></center>"""
print hr
#####################################################################################################################################

#~ print """%s"""%exam
print br


import sqlite3

C = sqlite3.connect('db/impm.db')
c = C.cursor()

c.execute('select id,nom,prenom from patient order by nom ASC')


# Selectionner un patient existant
######################################################################################################
print '''<meta charset="UTF-8">
<form action="infopatient.cgi" enctype="multipart/form-data"> '''

print """<h2>Selectionner un patient existant</h2>"""
print """<select name="patient" id="mesPatients" multiple> """
for i in c:
	ID=i[0]
	NomPrenom=i[1]+" "+i[2]
	print """
	<option value="%s">%s</option> 
	"""%(ID,NomPrenom),br
print """</select> """
print br,br
print """ <input type="hidden" name="exam" value="%s">
       <button type="submit">Suivant</button>   
        
</form>
"""%exam
c.close()
######################################################################################################
print hr
print br
print br

#Pour introduir un nouveau patient dans la base de donnees patient
#######################################################################################################################################
print """<h2>Introduir un nouveau patient</h2>"""

print '''<meta charset="UTF-8">
<form action="newpatient.cgi" enctype="multipart/form-data"> 

 <fieldset>
                <input  type="text"  id="patientnom" name="nom" placeholder="Nom du patient" value="" maxlength="32"  >
                <input  type="text"  id="patientprenom" name="prenom" placeholder="Prenom" aria-label="prenom" value="" maxlength="32" >
                 
                 <select type="select" name="sexe">
                 <option value="Sexe" selected disabled>Sexe du patient</option>
                 <option value="F">Feminin</option>
                 <option value="M">Masculin</option>
                 </select>
                 <input type="tel" pattern="[0-9-() ]*" name="age"   value=""  aria-required="true"  role="textbox" aria-multiline="false" placeholder="Age" aria-label="age"  minlength="1" maxlength="3">
                <br/>
 </fieldset>
 
 <fieldset>
	<input type="text" name="ville" value="" placeholder="ville">		
	<input type="text" name="quartier" value="" placeholder="Quartier">
	<input type="text" name="tel" value="" placeholder="Telephone"><br/>
 </fieldset> 
 <input type="hidden" name="exam" value="%s">
 '''%exam

print """ <input type="text" name="email"  id="usernamereg-yid" placeholder="Adresse mail"
            aria-label="Adresse mail" value="" maxlength="32"   ><br/><br/>
       
       <button type="submit">Enregistrer</button>   
        
</form>
"""
#########################################################################################################################

