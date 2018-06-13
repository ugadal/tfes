#!/usr/bin/env python
# -*- coding: utf-8 -*-
from SOAPpy import *
from DBS import *
import os
import uuid
def blast(filtre,typblast,seq,banque):
	key=uuid.uuid1()
	print type(typblast),typblast
	print type(seq)
	print type(banque),banque
	print "working in progress", key
	if filtre not in list("FT"):
		return "remplacer le filtre"
	if typblast not in TBB.keys():
		return "bad blast option"
	d,c,tb,typ=TBB[typblast]		
	#~ if typblast=="blastn" :
		#~ p="blastn"
		#~ typ="n"
	#~ elif typblast=="tblastn" :
		#~ p="tblastn"
		#~ typ="n"
	#~ elif typblast=="blastp" :
		#~ p="blastp"
		#~ typ="p"
	#~ elif typblast=="blastx" :
		#~ p="blastx"
		#~ typ="p"
	#~ if typblast=="tblastx" :
		#~ p="tblastx"
		#~ typ="n"	
	#~ else: 
		#~ return "you miss type try again"
	if type(seq) is not str:
		return "no string found"

	f=open("/tmp/%s.seq"%key,"w")
	f.write(seq)
	f.close
	
	valide=[]
	
	if typ=="n":
		for b in banque:
			if DB[b][2]=="n":
				print DB[b][1]
				valide.append(DB[b][1])
	if typ=="p":
		for b in banque:
			if DB[b][2]=="p":
				print DB[b][1]
				valide.append(DB[b][1])			
	sorted(set(valide)) #on vire double

	f=open("/tmp/%s.%sal"%(key,typ),"w")
	al="TITLE %s\nDBLIST "%key+" ".join(valide)
	f.write(al+"\n")
	f.close()
	


	cmd=TBB[typblast][1]%(key,key,filtre) #on go find command in DBS
	desc=os.popen(cmd)
	page=desc.read()
	return page

server= SOAPServer( ( '0.0.0.0', 3564) ) #le port et les adresse ip autorisée
server.registerFunction ( blast )
server.serve_forever()
