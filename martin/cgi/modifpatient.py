#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import cgi
import sqlite3 as sql
C=sql.connect("db/impm.db")
c=C.cursor()
f=cgi.FieldStorage()
idp=f.getvalue("idp")
cmd="""select * from patient where id=%s"""%idp
c.execute(cmd)
d=c.fetchall()[0]
d=list(d)
d.append(idp)
d=tuple(d)
print "Content-type:text/html"
print
#~ print d
print """
<form id="patientform" onsubmit="return formaccess2(%i);">

<fieldset>
<input  type="text"  id="patientnom" name="nom" placeholder="Nom du patient" value="%s" maxlength="32" required >
<input  type="text"  id="patientprenom" name="prenom" placeholder="Prenom" aria-label="prenom" value="%s" maxlength="32"  required>
"""%d[:3]
sexp=d[3]
#~ print "sexp",sexp
if sexp=="F":
	checkF=" checked "
	checkM=""
else:
	checkM=" checked "
	checkF=""
	
print """
<input type=radio 
	name=sexe
	value=F
	%s
>femme
<input type=radio 
	name=sexe
	value=M
	%s
>homme<br>"""%(checkF,checkM)
print """
<input type="tel" pattern="[0-9-() ]*" name="age"   value="%s"  required role="textbox" aria-multiline="false" placeholder="Age" aria-label="age"  minlength="1" maxlength="3">
                <br/>
 </fieldset>
 
 <fieldset>
	<input type="text" name="ville" value="%s" placeholder="ville" required>		
	<input type="text" name="quartier" value="%s" placeholder="Quartier" required>
	<input type="text" name="tel" value="%s" placeholder="Telephone"><br/>
 </fieldset> 


<input type="text" name="email"  id="usernamereg-yid" placeholder="Adresse mail"
            aria-label="Adresse mail" value="%s" maxlength="32"   ><br/><br/>
       
       <button>Enregistrer</button>   
<input type=hidden name=idpatient value=%s>     
</form>
"""%d[4:]
