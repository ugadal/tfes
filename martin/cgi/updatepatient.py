#!/usr/bin/python
import cgi
print "Content-type:text/html"
print

dataform=cgi.FieldStorage()
thisid=dataform.getvalue("idpatient")
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
cmd="""update patient set age="%s" , nom="%s" , prenom="%s", sexe="%s", ville="%s", quartier="%s", tel="%s", email="%s" where id=%s"""%(age,nom,prenom,sexe,ville,quartier,tel,email,thisid)
print cmd
c.execute(cmd)
C.commit()
exit()
