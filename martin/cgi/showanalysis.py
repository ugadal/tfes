#!/usr/bin/python2
# -*- coding: utf-8 -*-
import cgi
import sqlite3 as sql
def mab(row):
	#~ print """
	#~ <button onmouseover=fichpatient(%s) onmouseout=cleanfich()>select</button>%s %s (%s) <br>
	#~ """%row
	print """
	<table border=1 cellspacing=1 cellpadding=1><tr><td><button onmouseover=fichpatient(%s)>select</button></td><td>%s</td><td> %s</td><td> (%s)</td> </tr></table><br>
	"""%row
C=sql.connect("db/impm.db")
c=C.cursor()
f=cgi.FieldStorage()
table=f.getvalue("table")
ida=f.getvalue("idanalysis")
print "Content-type:text/html"
print
cmd="""select * from %s where id = %s"""%(table,ida)
#~ print cmd,table,ida
c.execute(cmd)
print c.fetchall()[0]
#~ for row in  c.fetchall():mab(row)
