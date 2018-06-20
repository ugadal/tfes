#!/usr/bin/env python
# -*- coding: utf-8 -*-


#MES EXAMENS

import cgi
import os

print "Content-type:text/html"
print

dataform=cgi.FieldStorage()
exam=dataform.getvalue("exam")
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

print hr



bacte="""<b><font color="coral">Choisir un examen</font></b><br>
	<form name=mm action=bacteriologie.cgi method=post enctype="multipart/form-data">
	<input type=checkbox name=examen value="pcv_atb" > PCV + ATB <br>
	<input type=checkbox name=examen value="ecbu_atb" > ECBU + ATB <br>
	<input type=checkbox name=examen value="pu_atb" > PU +ATB <br>
	<input type=checkbox name=examen value="mycoplasme_atb" > Mycoplasme + ATB <br>
	<input type=checkbox name=examen value="coproculture_atb" > Coproculture + ATB <br>
	<button type="submit">Suivant</button>
	
	<input type="hidden" name="ID_patient" value="%s">

"""%ID_patient

bio="""<b><font color="coral">Choisir un examen</font></b><br>
	<form name=mm action=biochimie.cgi method=post enctype="multipart/form-data">
	<h2><i>Proteine</i></h2>
	<input type=checkbox name=examen value="hemoglobine" > Electrophorese hemoglobine <br>
	<h2><i>Subtrats</i></h2>
	<input type=checkbox name=examen value="uree" > Uree <br>
	<input type=checkbox name=examen value="creatinine" > Creatinine <br>
	<input type=checkbox name=examen value="au" > Acide urique <br>
	<input type=checkbox name=examen value="glycemie" > Glycemie a jeun <br>
	<input type=checkbox name=examen value="bandelette_urinaire" > Bandelette urinaire <br>
	<input type=checkbox name=examen value="cholesterol_t" > Cholesterol total <br>
	<input type=checkbox name=examen value="cholesterol_hdl" > Cholesterol HDL <br>
	<input type=checkbox name=examen value="triglycerides" > Triglycerides <br>
	<input type=checkbox name=examen value="hemoglobine" > Hemoglobine glycosylee (Hb A1c) <br>
	<h2><i>Enzyme</i></h2>
	<input type=checkbox name=examen value="gpt_alat" > GPT/ALAT <br>
	<input type=checkbox name=examen value="got_asat" > GOT/ASAT <br>
	<h2><i>Ions</i></h2>
	<input type=checkbox name=examen value="calcemie" > Calcemie <br>
	<input type=checkbox name=examen value="magnesemie" > Magnesemie <br>
	<button type="submit">Suivant</button>
	
	<input type="hidden" name="ID_patient" value="%s">

"""%ID_patient

parasito_hemato="""<b><font color="coral">Choisir un examen</font></b><br>
	<form name=mm action=hemato_parasitologie.cgi method=post enctype="multipart/form-data">
	<input type=checkbox name=examen value="gs" > Groupe sanguin/Rhesus <br>
	<input type=checkbox name=examen value="nfs" > NFS <br>
	<input type=checkbox name=examen value="vs" > Vitesse de sedimentation (VS) <br>
	<input type=checkbox name=examen value="pcv" > Goutte epaisse <br>
	<input type=checkbox name=examen value="ecbu" > Examen des selles (KOAP) <br>
	<button type="submit">Suivant</button>
	
	<input type="hidden" name="ID_patient" value="%s">

"""%ID_patient

immuno_sero="""<b><font color="coral">Choisir un examen</font></b><br>
	<form name=mm action=immuno_serologie.cgi method=post enctype="multipart/form-data">
	<input type=checkbox name=examen value="hiv" > HIV <br>
	<input type=checkbox name=examen value="aslo" > ASLO <br>
	<input type=checkbox name=examen value="pu" > PU +ATB <br>
	<input type=checkbox name=examen value="aghbs" > AgHbs <br>
	<input type=checkbox name=examen value="achcv" > Ac HCV <br>
	<input type=checkbox name=examen value="crp" > CRP <br>
	<input type=checkbox name=examen value="tpha" > TPHA/VDRL <br>
	<input type=checkbox name=examen value="chlamydia" > Chlamydia <br>
	<input type=checkbox name=examen value="toxoplasmose_g" > Toxoplasmose IgG <br>
	<input type=checkbox name=examen value="toxoplasmose_m" > Toxoplasmose IgM <br>
	<input type=checkbox name=examen value="rubeole_g" > Rubeole IgG <br>
	<input type=checkbox name=examen value="rubeole_m" > Rubeole IgM <br>
	<input type=checkbox name=examen value="widal" > Serodiagnostic de WIDAL <br>
	<input type=checkbox name=examen value="palu" > Serologie paludisme <br>
	<button type="submit">Suivant</button>
	
	<input type="hidden" name="ID_patient" value="%s">

"""%ID_patient


if exam=="bacteriologie":
	print """<h2><i><font color="blue">Examens de bacteriologie</font></i></h2><br/>"""
	print bacte
elif exam=="biochimie":
	print """<h2><i><font color="blue">Examens de biochimie</font></i></h2><br/>"""
	print bio
elif exam=="hemato_parasitologie":
	print """<h2><i><font color="blue">Examens d'hemato/Parasitologie</font></i></h2><br/>"""
	print parasito_hemato
elif exam=="immuno_serologie":
	print """<h2><i><font color="blue">Examens d'immuno-serologie</font></i></h2><br/>"""
	print immuno_sero
else:
	print """
	<p><b><font color="red">Vous n'avez pas selectionne un examen. 
	Cliquez sur Ici pour faire un choix</font></b></p>"""
	
	print """
	<form action="ancien_patient.cgi" enctype="multipart/form-data">
	<button type="submit">Ici</button>
	<input type="hidden" name="ID_patient" value="%s">

	"""%ID_patient







######################################################################################################################
# A permet l'insertion des donnees
#~ A= '''<form  action="patient.cgi" enctype="multipart/form-data">
			
		  #~ <p><font color="blue">Veuillez selectionner un type d'examen svp :</font></p>
		  
			#~ <input type="radio" id="bac"
			 #~ name="exam" value="bacteriologie">
			#~ <label for="bac">Bacteriologie</label><br/>

			#~ <input type="radio" id="bio"
			 #~ name="exam" value="biochimie">
			#~ <label for="bio">Biochimie</label><br/>

			#~ <input type="radio" id="hema"
			 #~ name="exam" value="hemato_parasitologie">
			#~ <label for="hema">Parasito /Hematologie</label><br/>
			
			#~ <input type="radio" id="immuno"
			 #~ name="exam" value="immuno_serologie">
			#~ <label for="immuno">Immuno-serologie</label><br/>
			
		  
			
			#~ <button type="submit">Suivant</button>
			
		#~ </form>'''
		
# B Permet la consultation des donnees		
#~ B='''<form action="base.cgi" enctype="multipart/form-data">
	
  #~ <p><font color="blue">Veuillez selectionner un type d'examen svp :</font></p>
  
    #~ <input type="radio" id="bac"
     #~ name="exam" value="bacterio">
    #~ <label for="bac">Bacteriologie</label><br/>

    #~ <input type="radio" id="bio"
     #~ name="exam" value="biochimie">
    #~ <label for="bio">Biochimie</label><br/>

    #~ <input type="radio" id="hema"
     #~ name="exam" value="hemato">
    #~ <label for="hema">Parasito/Hematologie</label><br/>
    
    #~ <input type="radio" id="immuno"
     #~ name="exam" value="immuno">
    #~ <label for="immuno">Immuno_serologie</label><br/>
    
    
    #~ <button type="submit">Envoyer</button>
    
#~ </form>'''



#~ if choix=="insertion":
	#~ print A

#~ elif choix=="consultation":
	#~ print B
	
#~ else:
	#~ print """
	#~ <p><b><font color="red">Vous n'avez pas fais de selection.<br/>
	#~ Cliquez sur Accueil pour revenir au point de depart</font></b></p>
	#~ <form action="../index.html" enctype="multipart/form-data">
	#~ <button type="submit">Accueil</button>
	#~ </form>
	#~ """
