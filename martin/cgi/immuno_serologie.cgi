#!/usr/bin/env python
# -*- coding: utf-8 -*-


#Information du Patient Biochimie


import cgi
import os

print "Content-type:text/html"
print

dataform=cgi.FieldStorage()
type_examen=dataform.getvalue("examen")
ID_patient=dataform.getvalue("ID_patient")

et="*"
Me=et*200
hr="<hr/>"
br="<br/>"


print """<h1><font color="#BD8D46">LBH</font></h1>"""
print """ <h2 align="right"> Bonjour !</h2>"""

print hr
print """<center ><h1><font color='green'>Les examens medicaux de l'IMPM </font></h1></center>"""
print hr


print ID_patient

#################################################################################################################
print """<h2><i><font color="blue">FICHE DE PAILLASE (IMMUNO-SEROLOGIE)</font></i></h2><br/>"""


immuno_sero="""
<meta charset="UTF-8">
<form action="base_immuno_sero.cgi" enctype="multipart/form-data">
 
 
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
      <input type="tel" pattern="[0-9-() ]*" id="usernamereg-year" name="yyyy" value=""  aria-required="true"  role="textbox" aria-multiline="false" placeholder="Annee" aria-label="Date"  minlength="1" maxlength="4"><br/><br/>
 
 <input type="text" name="ag_hbs" value="" placeholder="ag_hbs">
 <input type="text" name="ac_hcv" value="" placeholder="ac_hcv">
 <input type="text" name="aslo" value="" placeholder="aslo">
 <input type="text" name="crp" value="" placeholder="crp">
 <input type="text" name="hiv_det" value="" placeholder="hiv_det">
 <input type="text" name="hiv_im" value="" placeholder="hiv_im">
 <input type="text" name="chlamy" value="" placeholder="chlamy">
 <input type="text" name="tpha" value="" placeholder="tpha">
 <input type="text" name="vdrl" value="" placeholder="vdrl">
 <input type="text" name="widal" value="" placeholder="widal">

</fieldset>
<br/><br/>
       
       <button type="submit">Enregistrer</button>
    
    <input type="hidden" name="ID_patient" value="%s">     
    <input type="hidden" name="type_examen" value="%s">     

           
</form>
"""%(ID_patient,type_examen)

####################################################################################################################
print immuno_sero
