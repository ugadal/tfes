#!/usr/bin/python
import cgi
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
import sqlite3
C = sqlite3.connect('db/impm.db')
c = C.cursor()
c.execute ("""insert into patient (nom,prenom,sexe,age,ville,quartier,tel,email) 
VALUES(?,?,?,?,?,?,?,?)""", (nom,prenom,sexe,age,ville,quartier,tel,email))
C.commit()
thisid=c.lastrowid
print thisid
print "inseerted ?"
print """<input type=hidden id=lastrowid value=%i>"""%thisid
