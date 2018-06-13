#!/usr/bin/python
# -*- coding: utf-8 -*-
#RECUPERER CE QU'IL Y A DANS LE FORMULAIRE

#importer le modul cgi
import cgi
#demander au module cgi d'aller recuperer les éléments du formulaire
print "content-type:text/html"
print

#Recuperer tout ce ki se trouv dans le "cgi" avec "FieldStorage" et le stosk dans la variable "dataform"
dataform=cgi.FieldStorage()

#imprimer le formulaire
cgi.print_form(dataform)
print dataform

#Je demand a dataform d'aller chercher la valeur de "sex"
sc=dataform.getvalue("sex")
pc=dataform.getvalue("pref")
print "<br>vous etes du type %s et vous aimez le %s"%(sc,pc)
br="<br>"
hr="<hr>"

if sc=="I" :print "Bonjour Man", br
if sc=="M" :print "Bonjour Monsieur", br
if sc=="F" :print "Bonjour Madame", br

if pc=="SA" :print "Une petite frite?"
else :print "Combien de crepes?"
