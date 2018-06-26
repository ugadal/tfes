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
#~ print idp
c.execute("""SELECT * from patient where id=?""",(idp,))
IPatient=c.fetchall()
print "<table border=6 cellspacing=2 cellpadding=1>"
print "<tr>"
for i in range(len(IPatient)):
	p=IPatient[i]
	for j in range(len(p)):
		print "<td>",p[j],"</td>"
	print "</tr>"

print "</table>"
print "<br/><br/>"


print "<br><hr>"




#####################
TA=["biochimie","bacteriologie","hemato_parasitologie","immuno_serologie"]

for ta in TA:
	print "resultats de %s :<br>"%ta
	cmd="""select * from %s where ID_patient= %s"""%(ta,idp)
	c.execute(cmd)
	res=c.fetchall()
	if res:print res
#####################

print """<button onclick=deletepatient(%s)>delete this patient</button>"""%idp
print """<button onclick=modifpatient(%s)>modification du patient</button>"""%idp
