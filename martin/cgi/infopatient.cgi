#!/usr/bin/env python
# -*- coding: utf-8 -*-
#


import cgi
import os

print "Content-type:text/html"
print

dataform=cgi.FieldStorage()

ID_patient=str(dataform.getvalue("patient"))

type_examen=dataform.getvalue("exam")




c.execute('''insert into patient(nom,prenom,sexe,age,ville,quartier,tel,email)
VALUES (?,?,?,?,?,?,?,?)''',(nom,prenom,sexe,age,ville,quartier,tel,email)
