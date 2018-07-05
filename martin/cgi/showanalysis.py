#!/usr/bin/python2
# -*- coding: utf-8 -*-
from ft import *
def mab(row):
	#~ print """
	#~ <button onmouseover=fichpatient(%s) onmouseout=cleanfich()>select</button>%s %s (%s) <br>
	#~ """%row
	print """
	<table border=1 cellspacing=1 cellpadding=1><tr><td><button onmouseover=fichpatient(%s)>select</button></td><td>%s</td><td> %s</td><td> (%s)</td> </tr></table><br>
	"""%row
f=cgi.FieldStorage()
table=f.getvalue("table")
ida=f.getvalue("idanalysis")
idp=f.getvalue("idp")
print "Content-type:text/html"
print
cmd="""select * from %s where id = %s"""%(table,ida)
c.execute(cmd)
cn=zip(*c.description)[0] #nom des colonnes
r=c.fetchone()

#~ print "<table border=1 cellspacing=5 cellpadding=1>"
#~ print "<tr>"
#~ for k,v in zip(cn[2:],r[2:]):
    #~ if mpa.has_key(k):k=mpa[k]
    #~ print "<th style='background-color:powderblue;'>",k,"</th>","<td style='background-color:#F8E6E0;'>",v,"</td>","</tr>"
    
#~ print "</table><br/>"
#~ print """<button onclick=deleteresult("%s","%s","%s")>supprimer ce resultat</button>"""%(idp,table,ida)


lign1=[]
lign2=[]
ligntot=[lign1,lign2]
for k,v in zip(cn[2:],r[2:]):
    if mpa.has_key(k):k=mpa[k]
    lign1.append(k)
    lign2.append(v)
print "<table border=1 cellspacing=2 cellpadding=5>"
for i in range(len(ligntot)):
	print "<tr>"
	for j in range(len(lign1)):
		if i==0:
			print "<th style='background-color:powderblue;'>"
			print ligntot[i][j]
			print "</th>"
		else:
			print "<td style='background-color:#F8E6E0;'>"
			print ligntot[i][j]
			print "</td>"
			
	print "</tr>"
print "</table><br/>"    
print """<button onclick=deleteresult("%s","%s","%s")>supprimer ce resultat</button>"""%(idp,table,ida)

