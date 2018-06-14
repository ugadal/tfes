#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  inittables.py


import sqlite3

C = sqlite3.connect('db/impm.db')

c = C.cursor()

def CreateTable():
    c.execute('''CREATE TABLE patient
    (id INTEGER PRIMARY KEY,nom TEXT,prenom TEXT,sexe varchar(15),age integer(11),ville TEXT,quartier TEXT)''')

def AddEntry(nom,prenom,sexe,age,ville,quartier):
    c.execute('''insert into patient(nom,prenom,sexe,age,ville,quartier)
    VALUES (?,?,?,?,?,?)''',(nom,prenom,sexe,age,ville,quartier))

CreateTable()

AddEntry('Deudjui','martin','M',33,'Mouscron','Dottignies')
AddEntry('Deker','patrick','M',17,'Mons','Caregnon')
AddEntry('Ben','charlie','M',45,'Namur','Coin')
AddEntry('Van','charlotte','F',23,'Bruxelles','Molemberk')

C.commit()

c.execute('select * from patient')

for i in c:
    print "\n"
    for j in i:
        print j

c.close()
