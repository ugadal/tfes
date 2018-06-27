#!/usr/bin/python2
# -*- coding: utf-8 -*-
import cgi
import sqlite3 as sql
C=sql.connect("db/impm.db")
c=C.cursor()
f=cgi.FieldStorage()
idp=f.getvalue("idp")
print "Content-type:text/html"
print
#~ print idp


li1=["id","nom","prenom","sexe","age","ville","quartier","tel","email"]
li1=["nom","prenom","sexe","age","ville","quartier","tel","email"]
c.execute("""SELECT * from patient where id=?""",(idp,))
b=c.fetchall()[0]

print "<caption>Information du patient </caption>"
print "<table cellspacing=5 cellpadding=2>"

for f,v in zip(li1,b[1:]):
	print """<tr>
			<th style="background-color:powderblue;">%s</th>
			<td style="background-color:#00FF80;">%s</td>
			</tr>"""%(f,v)
	
print "</table>"	


#####################
TA=["biochimie","bacteriologie","hemato_parasitologie","immuno_serologie"]

for ta in TA:
	cmd="""select id,date from %s where ID_patient= %s order by date desc"""%(ta,idp)
	c.execute(cmd)
	res=c.fetchall()
	if res:
		print "%i resultat(s) de %s :<br>"%(len(res),ta)
		for id,dateofanalysis in res:
			print """<button onmouseover=showresult("%s",%i)>%s</button>"""%(ta,id,dateofanalysis)
		print "<br>"
	#~ else:
		#~ print "pas de resultats de %s pour ce patient:<br>"%ta
#####################

print """<button onclick=resultpatient(%s)>Resultat</button>"""%idp
print """<button onclick=modifpatient(%s)>update</button>"""%idp
print """<button onclick=deletepatient(%s)>delete</button>"""%idp
