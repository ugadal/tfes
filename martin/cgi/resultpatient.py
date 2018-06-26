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

print "<b>Les différentes analyses:</b><br/><br/>"



TA=["biochimie","bacteriologie","hemato_parasitologie","immuno_serologie"]

for ta in TA:
	print "<button onclick=%s(%s)>resultats de %s </button><br><br/>"%(ta,idp,ta)
	#~ cmd="""select * from %s where ID_patient= %s"""%(ta,idp)
	#~ c.execute(cmd)
	#~ res=c.fetchall()
	#~ if res:print res
