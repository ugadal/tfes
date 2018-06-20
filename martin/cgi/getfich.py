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
print """<button onclick=deletepatient(%s)>delete this patient</button>"""%idp
