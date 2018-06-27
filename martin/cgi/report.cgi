#!/usr/bin/python
import cgi
print "Content-type:text/html"
print
dataform=cgi.FieldStorage()
cgi.print_form(dataform)
print dataform
#~ exit()
sc=dataform.getvalue("blu")
print sc
for k in  dataform.keys():
	print "<br><hr><br>",k
	print dataform[k]
exit()
pc=dataform.getvalue("pref")
#~ print "<br>vous etes du type %s et vous aimez le %s"%(sc,pc)
br="<br>"
hr="<hr>"
print hr
if sc=="I":print "bonjour Machin",br
if sc=="M":print "bonjour Monsieur",br
if sc=="F":print "bonjour Madame",br

if pc=="sa":print "Une petite frite ?"
else:print "Combien de crepes ?"
