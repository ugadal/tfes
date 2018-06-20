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
c.execute("""delete from patient where id=?""",(idp,))
C.commit()
