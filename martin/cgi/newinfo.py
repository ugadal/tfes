#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cgi
import sqlite3 as sql
C=sql.connect("db/impm.db")
c=C.cursor()
f=cgi.FieldStorage()
idp=f.getvalue("idp")
monselect=f.getvalue("monselect")
newval=f.getvalue("newval")
print "Content-type:text/html"
print


cmd=""" UPDATE patient SET %s = '%s' WHERE id=%s; """%(monselect,newval,idp)
c.execute(cmd)
C.commit()
print "Votre modification s'est effectue avec succes"
