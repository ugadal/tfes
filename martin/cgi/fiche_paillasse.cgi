#!/usr/bin/env python
# -*- coding: utf-8 -*-


import cgi
import os

print "Content-type:text/html"
print


dataform=cgi.FieldStorage()
exam=dataform.getvalue("exam")
username=dataform.getvalue("username")

et="*"
Me=et*200
hr="<hr/>"
br="<br/>"


print """<h1><font color="#BD8D46">LBH</font></h1>"""
print """ <h2 align="right"> Bonjour %s !</h2>"""%username

print hr
print """<center ><h1><font color='green'>Les examens medicaux de l'IMPM </font></h1></center>"""
print hr


bacte="""<b><font color="coral">Choisir un examen</font></b><br>
	<form name=mm action=bacteriologie.cgi method=post enctype="multipart/form-data">
	<input type=checkbox name=examen value="pcv_atb" > PCV + ATB <br>
	<input type=checkbox name=examen value="ecbu_atb" > ECBU + ATB <br>
	<input type=checkbox name=examen value="pu_atb" > PU +ATB <br>
	<input type=checkbox name=examen value="mycoplasme_atb" > Mycoplasme + ATB <br>
	<input type=checkbox name=examen value="coproculture_atb" > Coproculture + ATB <br>
	<button type="submit">Suivant</button>
	
	<input type="hidden" name="username" value="%s">

"""%username

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
	
	<input type="hidden" name="username" value="%s">

"""%username

parasito_hemato="""<b><font color="coral">Choisir un examen</font></b><br>
	<form name=mm action=hematologie.cgi method=post enctype="multipart/form-data">
	<input type=checkbox name=examen value="gs" > Groupe sanguin/Rhesus <br>
	<input type=checkbox name=examen value="nfs" > NFS <br>
	<input type=checkbox name=examen value="vs" > Vitesse de sedimentation (VS) <br>
	<input type=checkbox name=examen value="pcv" > Goutte epaisse <br>
	<input type=checkbox name=examen value="ecbu" > Examen des selles (KOAP) <br>
	<button type="submit">Suivant</button>
	
	<input type="hidden" name="username" value="%s">

"""%username

immuno_sero="""<b><font color="coral">Choisir un examen</font></b><br>
	<form name=mm action=immuno_sero.cgi method=post enctype="multipart/form-data">
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
	
	<input type="hidden" name="username" value="%s">

"""%username

para="""<b><font color="coral">Choisir un examen</font></b><br>
	<form name=mm action=fiche_labo.cgi method=post enctype="multipart/form-data">
	

	<button type="submit">Suivant</button>
	
	<input type="hidden" name="username" value="%s">

"""%username


if exam=="bacterio":
	print """<h2><i><font color="blue">Examens de bacteriologie</font></i></h2><br/>"""
	print bacte
elif exam=="biochimie":
	print """<h2><i><font color="blue">Examens de biochimie</font></i></h2><br/>"""
	print bio
elif exam=="hemato":
	print """<h2><i><font color="blue">Examens d'hemato/Parasitologie</font></i></h2><br/>"""
	print parasito_hemato
#~ elif exam=="parasito":
	#~ print """<h2><i><font color="blue">Examens de parasitologie</font></i></h2><br/>"""
	#~ print para
elif exam=="immuno":
	print """<h2><i><font color="blue">Examens d'immuno-serologie</font></i></h2><br/>"""
	print immuno_sero
else:
	print """
	<p><b><font color="red">Vous n'avez pas selectionne un examen. 
	Cliquez sur Ici pour choisir un examen</font></b></p>"""
	
	print """
	<form action="examens.cgi" enctype="multipart/form-data">
	<button type="submit">Ici</button>
	<input type="hidden" name="username" value="%s">

"""%username
