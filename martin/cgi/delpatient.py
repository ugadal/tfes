#!/usr/bin/python2
# -*- coding: utf-8 -*-
import cgi
import sqlite3 as sql
C=sql.connect("db/impm.db")
c=C.cursor()
f=cgi.FieldStorage()
idp=f.getvalue("idp")
print "Content-type:text/html"
print
print idp

TA=["biochimie","bacteriologie","hemato_parasitologie","immuno_serologie"]
for ta in TA:
	cmd="""delete from %s where ID_patient= %s"""%(ta,idp)
	c.execute(cmd)
	print "resultats de %s supprimé:<br>"%ta


c.execute("""delete from patient where id=?""",(idp,))
C.commit()
