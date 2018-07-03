#!/usr/bin/python
from ft import *
print "Content-type:text/html"
print
dataform=cgi.FieldStorage()
nom=str(dataform.getvalue("nom"))
prenom=str(dataform.getvalue("prenom"))
sexe=str(dataform.getvalue("sexe"))
dn=dataform.getvalue("dn")
ville=str(dataform.getvalue("ville"))
quartier=str(dataform.getvalue("quartier"))
tel=str(dataform.getvalue("tel"))
email=str(dataform.getvalue("email"))
c.execute ("""insert into patient (nom,prenom,sexe,dn,ville,quartier,tel,email) 
VALUES(?,?,?,?,?,?,?,?)""", (nom,prenom,sexe,dn,ville,quartier,tel,email))
C.commit()
thisid=c.lastrowid
print thisid
#~ print "inseerted ?"
print """<input type=hidden id=lastrowid value=%i>"""%thisid
