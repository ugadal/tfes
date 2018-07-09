#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

from ft import *
f=cgi.FieldStorage()
exam=f.getvalue("exam")
ID_patient=f.getvalue("idp")
print "Content-type:text/html"
print


print "<H2><i>Fiche de paillase de  </i>: <b>%s</b></H2><hr/>"%exam
print "<h3>Introduisez vos resultats d'analyse(s) ici:</h3>"
print """<form id="examform" onsubmit="return examform(%s);">  """%ID_patient
ete=[]
c.execute("pragma table_info(%s);"%exam)
i=0
j=0
for c in c.fetchall():
	ete.append(c[1])
	if i<2:
		print 
	else:
		if i==2:
			print """<b>Date:</b> <input type="date" name="%s" required value="2018-07-22" placeholder="%s"> <br/>"""%(c[1],c[1])
		else:
			print """ <input type="text" name="%s" value="" placeholder="%s">"""%(c[1],c[1])
	if j>3:
		print "<br/>"
		j=0
	i+=1

del ete[0]
print """<br><br><button>Enregistrer</button>   
<input type=hidden name="ID_patient" value=%s>     
<input type=hidden name="exam" value=%s>     
</form> """%(ID_patient,exam)
print "<br/>"


