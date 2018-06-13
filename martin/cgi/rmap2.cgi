#!/usr/bin/env python
# -*- coding: utf-8 -*-
print "content-type:text/html"
print
br="<br>"
hr="<hr"
htmfh="""
select some enzymes<br>
<form name=step1 action=rmap.cgi method=post enctype="multipart/form-data">
"""
htmfe="""
<br><hr>
<input type=submit>
<input type=reset>
</form>

"""
f=open("keep")
AE=[]
for l in f:
	AE.append(l.split()[3])
AE=list(set(AE))
AE.sort()
#~ print ",".join(AE),br
import cgi
import os
form=cgi.FieldStorage()
if form.has_key("enz"):
	E=form.getvalue("enz")
	if not type(E)==type([]):E=[E]
else:E=[]	
print htmfh
cc=0
for e in AE:
	cc+=1
	checked=""
	if E.count(e):checked="checked"
	print """<input type=checkbox name=enz value=%s %s>%s"""%(e,checked,e)
	if cc%15==0:print br
print htmfe

cmd="/usr/local/bin/restrict -plasmid -fragments -enzymes %s -sitelen 6 -sequence %s -outfile stdout"
if form.has_key("enz"):
	es=",".join(E)
	print es,br
	for targ in ["fusa","ycp50"]:
		f=os.popen(cmd%(es,targ))
		AL=f.readlines()
		f.close()
		while not AL[0].startswith("# Fragment lengths:"):AL.pop(0)
		AL.pop(0)
		print "Fragments in %s :"%targ,br
		for l in AL :
			if not l.startswith("#--"):
				af=l.split()
				if len(af)>1:
					s=int(100*round(float(l.split()[1])/100))
					print s,br
			else:break
			
		
		
#~ else:
	#~ print "select some enzymes"
	


