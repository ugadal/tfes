#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

from ft import *
print "Content-type:text/html"
print
dataform=cgi.FieldStorage()
ID_patient=dataform.getvalue("ID_patient")
exam=dataform.getvalue("exam")
date=dataform.getvalue("date")
type_examen=str(dataform.getvalue("type_examen"))
technicien=dataform.getvalue("technicien")

if exam=="biochimie":
	S_uree=dataform.getvalue("S_uree")
	S_creat=dataform.getvalue("S_creat")
	S_gluc=dataform.getvalue("S_gluc")
	S_ac_ur=dataform.getvalue("S_ac_ur")
	S_chol_t=dataform.getvalue("S_chol_t")
	S_sdl=dataform.getvalue("S_sdl")
	S_ldl=dataform.getvalue("S_ldl")
	S_tg=dataform.getvalue("S_tg")
	E_got=dataform.getvalue("E_got")
	E_gpt=dataform.getvalue("E_gpt")
	I_na=dataform.getvalue("I_na")
	I_k=dataform.getvalue("I_k")
	I_cl=dataform.getvalue("I_cl")
	I_ca=dataform.getvalue("I_ca")
	I_mg=dataform.getvalue("I_mg")
	
	print "<br>"
	
	cmd="""INSERT INTO biochimie(ID_patient,date,type_examen,S_uree,S_creat,S_gluc,S_ac_ur,S_chol_t,S_sdl,S_ldl,S_tg,E_got,E_gpt,I_na,I_k,I_cl,I_ca,I_mg,technicien) 
	VALUES ("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s");
	"""%(ID_patient,date,type_examen,S_uree,S_creat,S_gluc,S_ac_ur,S_chol_t,S_sdl,S_ldl,S_tg,E_got,E_gpt,I_na,I_k,I_cl,I_ca,I_mg,technicien)
	c.execute(cmd)
	C.commit()
	thisid=c.lastrowid
	print "<h3>Vos donnees ont bien ete enregistre!</h3>"
	
	cmd="""select * from %s where id = %s"""%(exam,thisid)
	c.execute(cmd)
	cn=zip(*c.description)[0] #nom des colonnes
	r=c.fetchone()
	lign1=[]
	lign2=[]
	ligntot=[lign1,lign2]
	for k,v in zip(cn[2:],r[2:]):
		if mpa.has_key(k):k=mpa[k]
		lign1.append(k)
		lign2.append(v)
	print "<table border=1 cellspacing=2 cellpadding=5>"
	for i in range(len(ligntot)):
		print "<tr>"
		for j in range(len(lign1)):
			if i==0:
				print "<th style='background-color:powderblue;'>"
				print ligntot[i][j]
				print "</th>"
			else:
				print "<td style='background-color:#F8E6E0;'>"
				print ligntot[i][j]
				print "</td>"
				
		print "</tr>"
	print "</table><br/>" 
		
elif exam=="bacteriologie":
	macroscopie=str(dataform.getvalue("macroscopie"))
	etat_frais=str(dataform.getvalue("etat_frais"))
	comptage_cellules=dataform.getvalue("comptage_cellules")
	coloration_gram=str(dataform.getvalue("coloration_gram"))
	coloration_ziehl=str(dataform.getvalue("coloration_ziehl"))
	milieu_culture=str(dataform.getvalue("milieu_culture"))
	observation=str(dataform.getvalue("observation"))
	conclusion=str(dataform.getvalue("conclusion"))
	
	cmd="""INSERT INTO bacteriologie(ID_patient,date,type_examen,macroscopie,etat_frais,comptage_cellules,coloration_gram,coloration_ziehl,milieu_culture,observation,conclusion,technicien) 
	VALUES ("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s");
	"""%(ID_patient,date,type_examen,macroscopie,etat_frais,comptage_cellules,coloration_gram,coloration_ziehl,milieu_culture,observation,conclusion,technicien)
	c.execute(cmd)
	C.commit()
	thisid=c.lastrowid
	print "<h3>Vos donnees ont bien ete enregistre!</h3>"
	cmd="""select * from %s where id = %s"""%(exam,thisid)
	c.execute(cmd)
	cn=zip(*c.description)[0] #nom des colonnes
	r=c.fetchone()
	lign1=[]
	lign2=[]
	ligntot=[lign1,lign2]
	for k,v in zip(cn[2:],r[2:]):
		if mpa.has_key(k):k=mpa[k]
		lign1.append(k)
		lign2.append(v)
	print "<table border=1 cellspacing=2 cellpadding=5>"
	for i in range(len(ligntot)):
		print "<tr>"
		for j in range(len(lign1)):
			if i==0:
				print "<th style='background-color:powderblue;'>"
				print ligntot[i][j]
				print "</th>"
			else:
				print "<td style='background-color:#F8E6E0;'>"
				print ligntot[i][j]
				print "</td>"
				
		print "</tr>"
	print "</table><br/>" 
elif exam=="hemato_parasitologie":
	gs=str(dataform.getvalue("gs"))
	rhesus=str(dataform.getvalue("rhesus"))
	vs=dataform.getvalue("vs")
	tp=dataform.getvalue("tp")
	tca=dataform.getvalue("tca")
	ts=dataform.getvalue("ts")
	tx_reticul=dataform.getvalue("tx")
	ge=dataform.getvalue("ge")
	nb=dataform.getvalue("nb")
	selle=dataform.getvalue("selle")
	microfilaire=dataform.getvalue("microfilaire")
	autre=str(dataform.getvalue("autre"))
	cmd="""INSERT INTO hemato_parasitologie(ID_patient,type_examen,date,gs,rhesus,vs,tp,tca,ts,tx_reticul,goutte_ep,autre,technicien) 
	VALUES ("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s");
	"""%(ID_patient,type_examen,date,gs,rhesus,vs,tp,tca,ts,tx_reticul,ge,autre,technicien)
	c.execute(cmd)
	C.commit()
	thisid=c.lastrowid
	print "<h3>Vos donnees ont bien ete enregistre!</h3>"
	cmd="""select * from %s where id = %s"""%(exam,thisid)
	c.execute(cmd)
	cn=zip(*c.description)[0] #nom des colonnes
	r=c.fetchone()
	lign1=[]
	lign2=[]
	ligntot=[lign1,lign2]
	for k,v in zip(cn[2:],r[2:]):
		if mpa.has_key(k):k=mpa[k]
		lign1.append(k)
		lign2.append(v)
	print "<table border=1 cellspacing=2 cellpadding=5>"
	for i in range(len(ligntot)):
		print "<tr>"
		for j in range(len(lign1)):
			if i==0:
				print "<th style='background-color:powderblue;'>"
				print ligntot[i][j]
				print "</th>"
			else:
				print "<td style='background-color:#F8E6E0;'>"
				print ligntot[i][j]
				print "</td>"
				
		print "</tr>"
	print "</table><br/>"   
elif exam=="immuno_serologie":
	ag_hbs=dataform.getvalue("ag_hbs")
	ac_hcv=dataform.getvalue("ac_hcv")
	aslo=dataform.getvalue("aslo")
	crp=dataform.getvalue("crp")
	hiv_det=dataform.getvalue("hiv_det")
	hiv_im=dataform.getvalue("hiv_im")
	chlamy=dataform.getvalue("chlamy")
	tpha=dataform.getvalue("tpha")
	vdrl=dataform.getvalue("vdrl")
	widal=dataform.getvalue("widal")
	
	cmd="""INSERT INTO immuno_serologie(ID_patient,date,type_examen,ag_hbs,ac_hcv,aslo,crp,hiv_det,hiv_im,chlamy,tpha,vdrl,widal,technicien) 
	VALUES ("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s");
	"""%(ID_patient,date,type_examen,ag_hbs,ac_hcv,aslo,crp,hiv_det,hiv_im,chlamy,tpha,vdrl,widal,technicien)
	c.execute(cmd)
	C.commit()
	thisid=c.lastrowid
	print "<h3>Vos donnees ont bien ete enregistre!</h3>"
	cmd="""select * from %s where id = %s"""%(exam,thisid)
	c.execute(cmd)
	cn=zip(*c.description)[0] #nom des colonnes
	r=c.fetchone()
	lign1=[]
	lign2=[]
	ligntot=[lign1,lign2]
	for k,v in zip(cn[2:],r[2:]):
		if mpa.has_key(k):k=mpa[k]
		lign1.append(k)
		lign2.append(v)
	print "<table border=1 cellspacing=2 cellpadding=5>"
	for i in range(len(ligntot)):
		print "<tr>"
		for j in range(len(lign1)):
			if i==0:
				print "<th style='background-color:powderblue;'>"
				print ligntot[i][j]
				print "</th>"
			else:
				print "<td style='background-color:#F8E6E0;'>"
				print ligntot[i][j]
				print "</td>"
				
		print "</tr>"
	print "</table><br/>" 
else:
	print "<h3>Vous n'avez pas selectionne une analyse!</h3>"
