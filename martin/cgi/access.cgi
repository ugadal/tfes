#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import cgi
import os
from SOAPpy import *
import uuid

entseq=uuid.uuid1()


br="<br>"
hr="<hr>"



fn="/tmp/%s.seq"%entseq
serr="/dev/null"

conn=SOAPProxy("http://192.168.2.10:9080")

print "Content-type:text/html"
print

dataform=cgi.FieldStorage()
identif=dataform.getvalue("identifiant")
#~ lis_identifiant=list(identifiant)
nom="gb:%s"%identif

r=conn.getent("%s"%nom)

fo=open(fn, "w")	
fo.write(r)
fo.close()

GC="%"
#~ cmd="infoseq %s"%fn
#~ cmd="infoseq -noheading -only -USA -Database -Name -type -length -Organism -Desc %s 2>%s"%(fn,serr)
lis=["USA","Database","Name","type","length","Organism","Desc"]
sol=[]
for val in range(len(lis)):
	reponse=lis[val]
	cmd="infoseq -noheading -only -%s %s 2>%s"%(reponse,fn,serr)
	res=os.popen(cmd)
	#~ entTot=res.read()
	rinfo=res.readline().strip()
	sol.append(rinfo)
	#~ print """%s"""%rinfo,br,br
print

#~ print """%s"""%entTot,br,br,br,hr
print """<table border="1"><tr><td>USA</td><td>Database</td><td>Name</td><td>type</td><td>length</td><td>Organism</td><td>Desc</td></tr>
		 <tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>
         </table>
"""%(sol[0],sol[1],sol[2],sol[3],sol[4],sol[5],sol[6])

print hr

print """%s"""%r

