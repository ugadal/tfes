#!/usr/bin/env python
# -*- coding: utf-8 -*-


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
print """ <h2 align="right"> Bonjour!</h2>"""

print hr
print """<center><h1><font color='green'>Les examens medicaux de l'IMPM </font></h1></center>"""
print hr

#################################################################################################################
print """<h2><i><font color="blue">FICHE DE PAILLASE (PARASITOLOGIE / HEMATOLOGIE)</font></i></h2><br/>"""


print """La valeur de l'ID_patient est de: %s """%ID_patient,br,br

pathema="""
<meta charset="UTF-8">
<form action="base_hemato_parasitologie.cgi" enctype="multipart/form-data">
 
 <fieldset>
	 <select name="mm" id="mois" required >
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
      <input type="tel" pattern="[0-9-() ]*" id="usernamereg-day" name="dd"   value=""  required  role="textbox" aria-multiline="false" placeholder="Jour" aria-label="Date"  minlength="1" maxlength="2">
      <input type="tel" pattern="[0-9-() ]*" id="usernamereg-year" name="yyyy" value=""  required  role="textbox" aria-multiline="false" placeholder="Annee" aria-label="Date"  minlength="1" maxlength="4">
     
      <select type="select" name="gs">
                 <option value="" selected disabled>Groupe sanguin</option>
                 <option value="a">A</option>
                 <option value="b">B</option>
                 <option value="ab">AB</option>
                 <option value="o">O</option>
      </select>
      
      <select type="select" name="rhesus">
                 <option value="" selected disabled>Rhesus</option>
                 <option value="positif">Positif</option>
                 <option value="negatif">Negatif</option>
      </select><br/>
      
      <input type="text" id="vs" name="vs" value="" placeholder="VS">
      <input type="text" id="tp" name="tp" value="" placeholder="Temps de Prothrombine">
      <input type="text" id="tca" name="tca" placeholder="TCA" value="">
      <input type="text" id="ts" name="ts" value="" placeholder="TS"><br/>
      <input type="text" id="tx" name="tx" value="" placeholder="Tx Reticul">
      
      <select type="select" name="ge">
                 <option value="">Goutte epaisse</option>
                 <option value="positif">Positif</option>
                 <option value="negatif">Negatif</option>
      </select>
      <input type="tel" id="nb" name="nb" value="" placeholder="Nombre / µl de sang"><br/>
      
      <textarea id="selle" class="reset" rows="3" cols="40" name="selle" value="" placeholder="Selles"></textarea>
      <textarea id="microfillet" class="reset" rows="3" cols="40" name="microfilaire" value="" placeholder="Recherche des microfilaire"></textarea>
      
		<textarea id="autre" class="reset" rows="2" cols="30" name="autre" value="" placeholder="Autre examen"></textarea><br/><br/>
      

          
 </fieldset>
<br/><br/>
       
       <button type="submit">Enregistrer</button>
    
    <input type="hidden" name="ID_patient" value="%s">     
    <input type="hidden" name="type_examen" value="%s">     

           
</form>
"""%(ID_patient,type_examen)
####################################################################################################################
print pathema
