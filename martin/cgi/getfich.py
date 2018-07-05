#!/usr/bin/python2
# -*- coding: utf-8 -*-
from ft import *
f=cgi.FieldStorage()
idp=f.getvalue("idp")
print "Content-type:text/html"
print
#~ print idp


#~ <<<<<<< HEAD
#~ li1=["id","nom","prenom","sexe","age","ville","quartier","tel","email"]
li1=["nom","prenom","sexe","age","ville","quartier","tel","email"]
#~ =======
li1=["id","nom","prenom","sexe","dn","ville","quartier","tel","email"]
li1=["nom","prenom","sexe","dn","ville","quartier","tel","email"]
#~ >>>>>>> 221c34a8a4c2ba4d72537bb16e4825971fdf0f64
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
	cmd="""select id,date,type_examen from %s where ID_patient= %s order by date desc"""%(ta,idp)
	c.execute(cmd)
	res=c.fetchall()
	print "<table border=1 cellspacing=1 cellpadding=1><tr>"
	if res:
		#~ print "%i resultat(s) de %s :<br>"%(len(res),ta)
		print "<td>%i resultat(s) de %s </td>"%(len(res),ta)
		for id,dateofanalysis,te in res:
			print """<td><button onmouseover=showresult("%s","%s",%i)>%s(%s)</button></td>"""%(idp,ta,id,dateofanalysis,te)
	print "</tr></table>"
print "<br>"
	#~ else:
		#~ print "pas de resultats de %s pour ce patient:<br>"%ta
#####################

print """<form name=inputanalysis action=cgi/inputanalysis.py>
<input type=hidden name=idp value=%s>
<input type=submit value="introduire des resultats d'analyse pour ce patient">
</form><hr/>"""%idp
print """<button onclick=modifpatient(%s)>modifier la fiche patient</button>"""%idp
print """<button onclick=deletepatient(%s)>supprimer ce patient</button><br/>"""%idp
