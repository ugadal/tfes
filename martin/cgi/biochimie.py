#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import cgi
import sqlite3 as sql
C=sql.connect("db/impm.db")
c=C.cursor()
f=cgi.FieldStorage()
idp=f.getvalue("idp")

print "Content-type:text/html"
print



li1=[]
c.execute("pragma table_info(biochimie);")
D=c.fetchall()
for j in D:
	li1.append(j[1])

cmd="""select * from biochimie where ID_patient= %s"""%idp
c.execute(cmd)
b=c.fetchall()

for row in b:
	print "<caption>Resultat biochimie </caption>"
	print "<table cellspacing=5 cellpadding=2>"
	print "<tr>"
	for i in range(len(row)):
		print """<th style="background-color:powderblue;">""",li1[i],"</th>","""<td style="background-color:#00FF80;">""", row[i],"</td>","</tr>"
	
	print "</table>"	
	print "<br/><br/><br/><br/>"

print """</center></body>"""
