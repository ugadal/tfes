#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Information du Patient Biochimie


import cgi
import os

print "Content-type:text/html"
print

dataform=cgi.FieldStorage()
username=dataform.getvalue("username")
type_examen=dataform.getvalue("examen")

et="*"
Me=et*200
hr="<hr/>"
br="<br/>"


print """<h1><font color="#BD8D46">LBH</font></h1>"""
print """ <h2 align="right"> Bonjour %s !</h2>"""%username

print hr
print """<center ><h1><font color='green'>Les examens medicaux de l'IMPM </font></h1></center>"""
print hr



#################################################################################################################
print """<h2><i><font color="blue">FICHE DE PAILLASE (BIOCHIMIE)</font></i></h2><br/>"""


biochimie="""
<meta charset="UTF-8">
<form  action="base_biochimie.cgi" enctype="multipart/form-data">

 <fieldset>
                <input  type="text"  id="patientnom" name="nom" placeholder="Nom du patient" value="" maxlength="32"  >
                <input  type="text"  id="patientprenom" name="prenom" placeholder="Prenom" aria-label="prenom" value="" maxlength="32" >
                 
                 <select type="select" name="sexe">
                 <option value="Sexe" selected disabled>Sexe du patient</option>
                 <option value="f">Feminin</option>
                 <option value="m">Masculin</option>
                 </select>
                 <input type="text" id="age" name="age" value="Age" placeholder="Age"><br/>
 </fieldset>
 
 <fieldset>
	<input type="text" name="ville" value="" placeholder="ville">	
	<input type="text" name="quartier" value="" placeholder="Quartier"><br/>
 </fieldset> 
 
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
 
 <input type="text" name="S_uree" value="" placeholder="S_uree">
 <input type="text" name="S_creat" value="" placeholder="S_creat">
 <input type="text" name="S_gluc" value="" placeholder="S_gluc">
 <input type="text" name="S_ac_ur" value="" placeholder="S_ac_ur">
 <input type="text" name="S_chol_t" value="" placeholder="S_chol_t">
 <input type="text" name="S_sdl" value="" placeholder="S_sdl">
 <input type="text" name="S_ldl" value="" placeholder="S_ldl">
 <input type="text" name="S_tg" value="" placeholder="S_tg">
 <input type="text" name="E_got" value="" placeholder="E_got">
 <input type="text" name="E_gpt" value="" placeholder="E_gpt">
 <input type="text" name="I_na" value="" placeholder="I_na">
 <input type="text" name="I_k" value="" placeholder="I_k">
 <input type="text" name="I_cl" value="" placeholder="I_cl">
 <input type="text" name="I_ca" value="" placeholder="I_ca">
 <input type="text" name="I_mg" value="" placeholder="I_mg">

</fieldset>


 <input type="text" name="email"  id="usernamereg-yid" placeholder="Adresse mail"
            aria-label="Adresse mail" value="" maxlength="32"   ><br/><br/>
       
       <button type="submit">Enregistrer</button>
    
    <input type="hidden" name="username" value="%s">     
    <input type="hidden" name="type_examen" value="%s">     

           
</form>
"""%(username, type_examen)



####################################################################################################################
print biochimie

