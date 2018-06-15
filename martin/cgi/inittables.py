#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  inittables.py


import sqlite3

C = sqlite3.connect('db/impm.db')

c = C.cursor()

def CreateTable():
    c.execute('''CREATE TABLE patient
    (id INTEGER PRIMARY KEY,nom TEXT,prenom TEXT,sexe varchar(15),age integer(11),ville TEXT,quartier TEXT,tel text,email text)''')

def AddEntry(nom,prenom,sexe,age,ville,quartier,tel,email):
    c.execute('''insert into patient(nom,prenom,sexe,age,ville,quartier,tel,email)
    VALUES (?,?,?,?,?,?,?,?)''',(nom,prenom,sexe,age,ville,quartier,tel,email))

CreateTable()

AddEntry('Deudjui','martin','M',33,'Mouscron','Dottignies',"0465513010","deudjuimartin@yahoo.fr")
AddEntry('Deker','patrick','M',17,'Mons','Caregnon',"0410564567","exemple@yahoo.com")
AddEntry('Ben','charlie','M',45,'Namur','Coin',"0410564567","exemple@yahoo.com")
AddEntry('Van','charlotte','F',23,'Bruxelles','Molemberk', "0410564567","exemple@yahoo.com")
AddEntry('Albert','charle','F',23,'Bruxelles','Molemberk', "0410564567","exemple@yahoo.com")

C.commit()

c.execute('select * from patient')

for i in c:
    print "\n"
    for j in i:
        print j


