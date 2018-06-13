#!/usr/bin/env python2
# -*- coding: utf-8 -*-
print "content-type:text/html"
print
print """<style>
table, th, td {
    border: 1px solid black;
}
</style>"""
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
def hcell(s):return "<th>%s</th>"%s.center(10,"_")
def cell(s):return "<td>%s</td>"%s
def hrow(l):return "<tr>\r\n%s\r\n</tr>"%"\r\n".join([hcell(x) for x in l])
def row(l):return "<tr>\r\n%s\r\n</tr>"%"\r\n".join([cell(x) for x in l])
def table(lr):return "<table>\r\n%s\r\n</table>"%"\r\n".join(lr)
f=open("onecutters")
OC=[]
for l in f:OC.append(l.strip())
f.close()
OC.sort()
f=open("nocutters")
NC=[]
for l in f:NC.append(l.strip())
f.close()
NC.sort()
f=open("keep")
AE=[]
for l in f:
	AE.append(l.split()[3])
AE=list(set(AE)-set(NC)-set(OC))
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
print "Enzymes not cutting in plasmid",br,hr,br
for e in NC:
	cc+=1
	checked=""
	if E.count(e):checked="checked"
	print """<input type=checkbox name=enz value=%s %s onchange='submit()'>%s"""%(e,checked,e)
	if cc%15==0:print br
print hr,br
cc=0
print "Enzymes cutting once in plasmid",br,hr,br
for e in OC:
	cc+=1
	checked=""
	if E.count(e):checked="checked"
	print """<input type=checkbox name=enz value=%s %s onchange='submit()'>%s"""%(e,checked,e)
	if cc%15==0:print br
print hr,br
print "other enzymes",br,hr,br
cc=0
for e in AE:
	cc+=1
	checked=""
	if E.count(e):checked="checked"
	print """<input type=checkbox name=enz value=%s %s onchange='submit()'>%s """%(e,checked,e)
	if cc%15==0:print br
print htmfe

cmd="/usr/local/bin/restrict -plasmid -fragments -enzymes %s -sitelen 6 -sequence %s -outfile stdout 2>/dev/null"
if form.has_key("enz"):
	es=",".join(E)
	print es,br
	frags={}
	plas=["ycp50","fusa","fusb","fusc","fusd"]
	for targ in plas:
		frags[targ]=[]
		f=os.popen(cmd%(es,targ))
		AL=f.readlines()
		f.close()
		while not AL[0].startswith("# HitCount:"):AL.pop(0)
		hc=int(AL[0].split()[2])
		if hc==0:
			frags[targ]=["None"]
			continue
		while not AL[0].startswith("# Fragment lengths:"):AL.pop(0)
		AL.pop(0)
		for l in AL :
			if not l.startswith("#--"):
				af=l.split()
				if len(af)>1:
					s=int(100*round(float(l.split()[1])/100))
					frags[targ].append(str(s))
			else:break
		frags[targ]=br.join(frags[targ])
		if not frags[targ]:frags[targ].append("None")
		
Rows=[]
#~ Rows.append(hrow(E))
Rows.append(hrow(plas))
Rows.append(row([frags[x] for x in plas]))
print table(Rows)
#~ else:
	#~ print "select some enzymes"
	


