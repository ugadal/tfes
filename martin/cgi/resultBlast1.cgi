#!/usr/bin/env python
# -*- coding: utf-8 -*-


import cgi
import os
import uuid


print "Content-type:text/html"
print
br="<br>"
hr="<hr>"

et="*"
Me=et*250

print hr
print hr
dataform=cgi.FieldStorage()
resultBlast=dataform.getvalue("bank")
nom=dataform.getvalue("id")
rbt=dataform.getvalue("bt")
print rbt

print "<h1>Le resultat de mon BLAST</h1>",br,Me
#~ if resultBlast=="bct":
cmd="/opt/blast-2.2.26/bin/blastall -p %s -i /tmp/%s.seq -d %s -T T"%(rbt,nom)
res=os.popen(cmd)
rblast=res.read()
print rblast
#~ if resultBlast=="ydna":
	#~ cmd="/opt/blast-2.2.26/bin/blastall -p blastn -i /tmp/%s.seq -d /data/dbs/ydna/ydna -T T"%nom
	#~ res=os.popen(cmd)
	#~ rblast=res.read()
	#~ print rblast
#~ if resultBlast=="swissprot":
	#~ cmd="/opt/blast-2.2.26/bin/blastall -p blastp -i /tmp/%s.seq -d /data/dbs/swissprot -T T"%nom
	#~ res=os.popen(cmd)
	#~ rblast=res.read()
	#~ print rblast
#~ if resultBlast=="yprot":
	#~ cmd="/opt/blast-2.2.26/bin/blastall -p blastp -i /tmp/%s.seq -d /data/dbs/yprot/yprot -T T"%nom
	#~ res=os.popen(cmd)
	#~ rblast=res.read()
	#~ print rblast
#~ if resultBlast=="nt":
	#~ cmd="/opt/blast-2.2.26/bin/blastall -p blastp -i /tmp/%s.seq -d /data/dbs/pdb/nt -T T"%nom
	#~ res=os.popen(cmd)
	#~ rblast=res.read()
	#~ print rblast
