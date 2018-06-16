#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

#Information du Patient


import cgi
import os

print "Content-type:text/html"
print

dataform=cgi.FieldStorage()
ID_patient=dataform.getvalue("ID_patient")
type_examen=dataform.getvalue("examen")

et="*"
Me=et*200
hr="<hr/>"
br="<br/>"


print """<h1><font color="#BD8D46">LBH</font></h1>"""
print """ <h2 align="right"> Bonjour !</h2>"""

print hr
print """<center ><h1><font color='green'>Les examens medicaux de l'IMPM </font></h1></center>"""
print hr



#################################################################################################################
print """<h2><i><font color="blue">FICHE DE PAILLASE (BACTERIOLOGIE)</font></i></h2><br/>"""

patbacte="""
<meta charset="UTF-8">
<form action="base_bacterio.cgi" enctype="multipart/form-data">

 <fieldset>
	 <select name="mm" id="mois"  >
            <option value="" selected disabled>mois</option>
            <option value="1">Janvier</option>
            <option value="2">Fevrier</option>
            <option value="3">Mars</option>
            <option value="4">Avril</option>
            <option value="5">Mai</option>
            <option value="6">Juin</option>
            <option value="7">Juillet</option>
            <option value="8">Aout</option>
            <option value="9">Septembre</option>
            <option value="10">Octobre</option>
            <option value="11">Novembre</option>
            <option value="12">Decembre</option>
      </select>
      <input type="tel" pattern="[0-9-() ]*" id="usernamereg-day" name="dd"   value=""  aria-required="true"  role="textbox" aria-multiline="false" placeholder="Jour" aria-label="Date"  minlength="1" maxlength="2">
      <input type="tel" pattern="[0-9-() ]*" id="usernamereg-year" name="yyyy" value=""  aria-required="true"  role="textbox" aria-multiline="false" placeholder="Annee" aria-label="Date"  minlength="1" maxlength="4"><br/>
 
 <input type="text" name="macroscopie" value="" placeholder="Macroscopie">
 <input type="text" name="etat_frais" value="" placeholder="Etat frais">
 <input type="text" name="comptage_cellules" value="" placeholder="Comptage cellues"><br/>
 <input type="text" name="coloration_gram" value="" placeholder=" coloration_gram">
 <input type="text" name="coloration_ziehl" value="" placeholder=" Coloration_ziehl">
 <input type="text" name="milieu_culture" value="" placeholder="Milieu de culture"><br/>
 <input type="text" name="observation" value="" placeholder="observation">
 <input type="text" name="conclusion" value="" placeholder="conclusion"><br/>

 </fieldset>
<br/><br/>
       
       <button type="submit">Enregistrer</button>
    
    <input type="hidden" name="username" value="%s">     
    <input type="hidden" name="type_examen" value="%s">     

           
</form>
"""%(ID_patient,type_examen)
 

####################################################################################################################
print patbacte
