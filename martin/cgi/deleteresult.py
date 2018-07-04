#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
from ft import *
f=cgi.FieldStorage()
ida=f.getvalue("ida")
table=f.getvalue("table")
print "Content-type:text/html"
print

print table
print "\n L'id est: ",ida
cmd="""delete from %s where id=%s"""%(table,ida)
#~ c.execute("""delete from ? where id=?""",(table,ida,))
c.execute(cmd)
C.commit()
