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

print "L'id du patient est %s"%idp



TA=["biochimie","bacteriologie","hemato_parasitologie","immuno_serologie"]

for ta in TA:
	print "resultats de %s :<br>"%ta
	#~ cmd="""select * from %s where ID_patient= %s"""%(ta,idp)
	#~ c.execute(cmd)
	#~ res=c.fetchall()
	#~ if res:print res
