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

print "<table border=1 cellspacing=5 cellpadding=1>"
print "<tr>"
for k,v in zip(cn[2:],r[2:]):
    print "<th style='background-color:powderblue;'>",k,"</th>","<td style='background-color:#F8E6E0;'>",v,"</td>","</tr>"
    
print "</table><br/>"
print """<button onclick=deleteresult("%s","%s","%s")>supprimer ce resultat</button>"""%(idp,table,ida)

