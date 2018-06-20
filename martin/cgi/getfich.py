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
c.execute("""SELECT * from patient where id=?""",(idp,))

print c.fetchall()
print "<br><hr>"
TA=["biochimie","bacteriologie","hemato_parasitologie","immuno_serologie"]
for ta in TA:
	print "resultats de %s :<br>"%ta
	cmd="""select * from %s where ID_patient= %s"""%(ta,idp)
	c.execute(cmd)
	#~ c.execute("""select * from ? where ID_patient = ?""",(ta,idp,))
	print c.fetchall()
	print "<hr>"
print """<button onclick=deletepatient(%s)>delete this patient</button>"""%idp
