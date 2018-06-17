#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  inittables.py


import sqlite3

C = sqlite3.connect('db/impm.db')

c = C.cursor()

def CreateTable():
	c.execute('''CREATE TABLE `bacteriologie` (
  `id` integer PRIMARY KEY,
  `ID_patient` int(15),
  `date` date,
  `type_examen` varchar(255),
  `macroscopie` text,
  `etat_frais` text,
  `comptage_cellules` int(15),
  `coloration_gram` text,
  `coloration_ziehl` text,
  `milieu_culture` text,
  `observation` text,
  `conclusion` text,
  `technicien` varchar(255));
 ''')

#~ def AddEntry(nom,prenom,sexe,age,ville,quartier,tel,email):
    #~ c.execute('''insert into patient(nom,prenom,sexe,age,ville,quartier,tel,email)
    #~ VALUES (?,?,?,?,?,?,?,?)''',(nom,prenom,sexe,age,ville,quartier,tel,email))

CreateTable()

#~ AddEntry('Deudjui','martin','M',33,'Mouscron','Dottignies',"0465513010","deudjuimartin@yahoo.fr")
#~ AddEntry('Deker','patrick','M',17,'Mons','Caregnon',"0410564567","exemple@yahoo.com")
#~ AddEntry('Ben','charlie','M',45,'Namur','Coin',"0410564567","exemple@yahoo.com")
#~ AddEntry('Van','charlotte','F',23,'Bruxelles','Molemberk', "0410564567","exemple@yahoo.com")
#~ AddEntry('Van','charlotte','F',23,'Bruxelles','Molemberk', "0410564567","exemple@yahoo.com")

C.commit()

c.execute('.schema immuno_serologie')

for i in c:
    print "\n"
    for j in i:
        print j






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


















