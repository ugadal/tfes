#!/usr/bin/python2
# -*- coding: utf-8 -*-
import cgi
import sqlite3 as sql
def mab(row):
	print """
	<button onclick=fichpatient(%s)>select</button>%s %s (%s) <br>
	"""%row
C=sql.connect("db/impm.db")
c=C.cursor()
f=cgi.FieldStorage()
nib=f.getvalue("nib")
if nib==None:nib=""
print "Content-type:text/html"
print
se='%'+nib+'%'
c.execute("""SELECT id,nom,prenom,email FROM patient WHERE nom like ? or prenom like ? limit 25""",(se,se,))
for row in  c.fetchall():mab(row)
