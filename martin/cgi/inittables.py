#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  inittables.py


import sqlite3

C = sqlite3.connect('db/impm.db')

c = C.cursor()

def CreateTable():
	c.execute('''CREATE TABLE `table_analyse` (
  `id` integer PRIMARY KEY,
  `nom1` varchar(255),
  `nom2` varchar(255),
  `input_type` varchar(255),
  `nb_val` int(15),
  `val` varchar(255),
  `inst` varchar(255));
  
 ''')

def AddEntry(nom1,nom2,input_type,nb_val,val,inst):
    c.execute('''insert into table_analyse(nom1,nom2,input_type,nb_val,val,inst)
    VALUES (?,?,?,?,?,?)''',(nom1,nom2,input_type,nb_val,val,inst))

CreateTable()

AddEntry("bacteriologie","macroscopie","text",1,"","")
AddEntry("bacteriologie","etat_frais","text",1,"","")
AddEntry("bacteriologie","comptage_cellules","text",1,"","")
AddEntry("bacteriologie","coloration_gram","radio",2,"positif","Coloration Gram")
AddEntry("bacteriologie","coloration_gram","radio",2,"negatif","Coloration gram")
AddEntry("bacteriologie","coloration_ziehl","text",1,"","")
AddEntry("bacteriologie","milieu_culture","text",1,"","")
AddEntry("bacteriologie","observation","text",1,"","")
AddEntry("bacteriologie","conclusion","text",1,"","")
AddEntry("bacteriologie","technicien","text",1,"","")

AddEntry("biochimie","S_uree","text",1,"","")
AddEntry("biochimie","S_creat","text",1,"","")
AddEntry("biochimie","S_gluc","text",1,"","")
AddEntry("biochimie","S_ac_ur","text",1,"","")
AddEntry("biochimie","S_chol_t","text",1,"","")
AddEntry("biochimie","S_sdl","text",1,"","")
AddEntry("biochimie","S_ldl","text",1,"","")
AddEntry("biochimie","S_tg","text",1,"","")
AddEntry("biochimie","E_got","text",1,"","")
AddEntry("biochimie","E_gpt","text",1,"","")
AddEntry("biochimie","I_na","text",1,"","")
AddEntry("biochimie","I_k","text",1,"","")
AddEntry("biochimie","I_cl","text",1,"","")
AddEntry("biochimie","I_ca","text",1,"","")
AddEntry("biochimie","I_mg","text",1,"","")
AddEntry("biochimie","technicien","text",1,"","")

AddEntry("hemato_parasitologie","gs","radio",4,"A","Groupe sanguin")
AddEntry("hemato_parasitologie","gs","radio",4,"B","Groupe sanguin")
AddEntry("hemato_parasitologie","gs","radio",4,"AB","Groupe sanguin")
AddEntry("hemato_parasitologie","gs","radio",4,"O","Groupe sanguin")
AddEntry("hemato_parasitologie","rhesus","radio",2,"positif","Facteur rhesus ")
AddEntry("hemato_parasitologie","rhesus","radio",2,"negatif","facteur rhesus")
AddEntry("hemato_parasitologie","vs","text",1,"","")
AddEntry("hemato_parasitologie","tp","text",1,"","")
AddEntry("hemato_parasitologie","tca","text",1,"","")
AddEntry("hemato_parasitologie","ts","text",1,"","")
AddEntry("hemato_parasitologie","tx_reticul","text",1,"","")
AddEntry("hemato_parasitologie","goutte_ep","radio",2,"positif","Goutte epaisse")
AddEntry("hemato_parasitologie","goutte_ep","radio",2,"negatif","Goutte epaisse")
AddEntry("hemato_parasitologie","autre","text",1,"","")
AddEntry("hemato_parasitologie","technicien","text",1,"","")

AddEntry("immuno_serologie","ag_hbs","text",1,"","")
AddEntry("immuno_serologie","ac_hcv","text",1,"","")
AddEntry("immuno_serologie","aslo","text",1,"","")
AddEntry("immuno_serologie","crp","text",1,"","")
AddEntry("immuno_serologie","hiv_det","text",1,"","")
AddEntry("immuno_serologie","hiv_im","text",1,"","")
AddEntry("immuno_serologie","chlamy","text",1,"","")
AddEntry("immuno_serologie","tpha","text",1,"","")
AddEntry("immuno_serologie","vdrl","text",1,"","")
AddEntry("immuno_serologie","widal","text",1,"","")
AddEntry("immuno_serologie","technicien","text",1,"","")




C.commit()

c.execute('select * from table_analyse;')

for i in c:
    print "\n"
    for j in i:
        print j





#~ CreateTable():
	#~ c.execute('''CREATE TABLE `bacteriologie` (
  #~ `id` integer PRIMARY KEY,
  #~ `ID_patient` int(15),
  #~ `date` date,
  #~ `type_examen` varchar(255),
  #~ `macroscopie` text,
  #~ `etat_frais` text,
  #~ `comptage_cellules` int(15),
  #~ `coloration_gram` text,
  #~ `coloration_ziehl` text,
  #~ `milieu_culture` text,
  #~ `observation` text,
  #~ `conclusion` text,
  #~ `technicien` varchar(255));
 #~ ''')


#~ CREATE TABLE `biochimie` (
  #~ `id` integer PRIMARY KEY,
  #~ `ID_patient` int(11),
  #~ `date` date ,
  #~ `type_examen` text,
  #~ `S_uree` double,
  #~ `S_creat` double,
  #~ `S_gluc` double,
  #~ `S_ac_ur` double,
  #~ `S_chol_t` double,
  #~ `S_sdl` double,
  #~ `S_ldl` double,
  #~ `S_tg` double,
  #~ `E_got` double,
  #~ `E_gpt` double,
  #~ `I_na` double,
  #~ `I_k` double,
  #~ `I_cl` double,
  #~ `I_ca` double,
  #~ `I_mg` double,
  #~ `technicien` text 
#~ );


#~ CREATE TABLE `hemato_parasitologie` (
  #~ `id` integer PRIMARY KEY,
  #~ `ID_patient` int(11),
  #~ `date` date ,
  #~ `type_examen` text,
  #~ `gs` text,
  #~ `rhesus` text,
  #~ `vs` int(11),
  #~ `tp` int(11),
  #~ `tca` int(11),
  #~ `ts` int(11),
  #~ `tx_reticul` int(11),
  #~ `goutte_ep` text,
  #~ `autre` text,
  #~ `technicien` text
#~ );




#~ CREATE TABLE `immuno_serologie` (
  #~ `id` integer PRIMARY KEY,
  #~ `ID_patient` int(15),
  #~ `date` date,
  #~ `type_examen` text,
  #~ `ag_hbs` text,
  #~ `ac_hcv` text,
  #~ `aslo` text,
  #~ `crp` text,
  #~ `hiv_det` text,
  #~ `hiv_im` text,
  #~ `chlamy` text,
  #~ `tpha` text,
  #~ `vdrl` text,
  #~ `widal` text,
  #~ `technicien` text
#~ );


















