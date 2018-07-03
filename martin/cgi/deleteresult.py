#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import cgi
import sqlite3 as sql
C=sql.connect("db/impm.db")
c=C.cursor()
f=cgi.FieldStorage()
ida=f.getvalue("ida")
table=f.getvalue("table")
print "Content-type:text/html"
print

print table
print "\n L'id est: ",ida
c.execute("""delete from ? where id=?""",(table,ida,))
C.commit()
