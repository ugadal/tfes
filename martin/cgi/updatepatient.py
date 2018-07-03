#!/usr/bin/python
from ft import *
print "Content-type:text/html"
print

dataform=cgi.FieldStorage()
thisid=dataform.getvalue("idpatient")
nom=str(dataform.getvalue("nom"))
prenom=str(dataform.getvalue("prenom"))
sexe=str(dataform.getvalue("sexe"))
dn=dataform.getvalue("dn")
ville=str(dataform.getvalue("ville"))
quartier=str(dataform.getvalue("quartier"))
tel=str(dataform.getvalue("tel"))
email=str(dataform.getvalue("email"))
cmd="""update patient set dn="%s" , nom="%s" , prenom="%s", sexe="%s", ville="%s", quartier="%s", tel="%s", email="%s" where id=%s"""%(dn,nom,prenom,sexe,ville,quartier,tel,email,thisid)
print cmd
c.execute(cmd)
C.commit()
