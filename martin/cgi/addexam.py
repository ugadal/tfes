#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

from ft import *
f=cgi.FieldStorage()
exam=f.getvalue("exam")
ID_patient=f.getvalue("idp")
print "Content-type:text/html"
print


print """<H2><font color="#610B0B"><i>Fiche de paillase de : </i></font> <b>%s</b></H2><hr/>"""%exam
print """<h3><font color="#B40404">Introduisez vos resultats d'analyse(s) ici:</font></h3>"""
print """<form id="examform" onsubmit="return examform(%s);">  """%ID_patient
print """<b>Date:</b> <input type="date" name="date" required value="" placeholder="2018-07-22"> <br/>"""


c.execute('''select * from table_analyse where nom1="%s";'''%exam)
z=0
for i in c:
	if i[3]=="radio":
		z+=1
		if z==1:
			print """<hr/><p><i><b>%s</b></i></p> """%i[6]
			print """ <input type="radio" name="%s" id="%s" value="%s">"""%(i[2],i[2],i[5])
			print """<label for="%s"> %s</label><br/>"""%(i[2],i[5])
			z+=1
		else:
			print """ <input type="radio" name="%s" id="%s" value="%s">"""%(i[2],i[2],i[5])
			print """<label for="%s"> %s</label><br/>"""%(i[2],i[5])
			if z>i[4]:
				z=0
			else:
				z=z
	else:
		print """ <input type="text" name="%s" value="" placeholder="%s">"""%(i[2],i[2])
		z=0

print """<br><br><button>Enregistrer</button>   
<input type=hidden name="ID_patient" value=%s>     
<input type=hidden name="exam" value=%s>     
</form> """%(ID_patient,exam)
print "<br/>"

###################################################################################################

#~ ete=[]
#~ c.execute("pragma table_info(%s);"%exam)
#~ i=0
#~ j=0
#~ for c in c.fetchall():
	#~ ete.append(c[1])
	#~ if i<2:
		#~ print 
	#~ else:
		#~ if i==2:
			#~ print """<b>Date:</b> <input type="date" name="%s" required value="" placeholder="2018-07-22"> <br/>"""%(c[1])
		#~ else:
			#~ print """ <input type="text" name="%s" value="" placeholder="%s">"""%(c[1],c[1])
	#~ if j>3:
		#~ print "<br/>"
		#~ j=0
	#~ i+=1

#~ del ete[0]
#~ print """<br><br><button>Enregistrer</button>   
#~ <input type=hidden name="ID_patient" value=%s>     
#~ <input type=hidden name="exam" value=%s>     
#~ </form> """%(ID_patient,exam)
#~ print "<br/>"
