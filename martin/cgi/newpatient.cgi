#!/usr/bin/env python
# -*- coding: utf-8 -*-
#


import cgi
import os

print "Content-type:text/html"
print

dataform=cgi.FieldStorage()

nom=str(dataform.getvalue("nom"))
prenom=str(dataform.getvalue("prenom"))
sexe=str(dataform.getvalue("sexe"))
age=dataform.getvalue("age")
ville=str(dataform.getvalue("ville"))
quartier=str(dataform.getvalue("quartier"))
tel=str(dataform.getvalue("tel"))
email=str(dataform.getvalue("email"))


#~ nom=dataform.getvalue("nom")
#~ prenom=dataform.getvalue("prenom")
#~ sexe=dataform.getvalue("sexe")
#~ age=dataform.getvalue("age")
#~ ville=dataform.getvalue("ville")
#~ quartier=dataform.getvalue("quartier")
#~ tel=dataform.getvalue("tel")
#~ email=dataform.getvalue("email")

exam=dataform.getvalue("exam")


hr="<hr/>"
br="<br/>"


print """<h1><font color="#BD8D46">LBH</font></h1>"""
print """ <h2 align="right"> Bonjour!</h2>"""
print hr
#~ print """<center style="background-color:#D0A9F5;><h1><font color='green'>Les examens medicaux de la LBH </font></h1></center>"""
print hr

###########################################################################################################################
import sqlite3
C = sqlite3.connect('db/impm.db')
c = C.cursor()
#~ c.execute ("""insert into patient(nom,prenom,sexe,age,ville,quartier,tel,email) VALUES(?,?,?,?,?,?,?,?)""",(nom,prenom,sexe,age,ville,quartier,tel,email))
c.execute ("""insert into patient(nom,prenom,sexe,age,ville,quartier,tel,email) 
VALUES(?,?,?,?,?,?,?,?);""",("Leoca","solange","F",33,"Mons","Jemappes","565556554","leoca@yahoo.fr"))


c.execute('select * from patient')

for i in c:
    print "\n"
    for j in i:
        print j


####################################################################################################################################
print "moi"





