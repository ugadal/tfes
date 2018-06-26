#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import cgi
import sqlite3 as sql
C=sql.connect("db/impm.db")
c=C.cursor()
f=cgi.FieldStorage()
idp=f.getvalue("idp")
print "Content-type:text/html"
print

print """<form>
<select id="monselect">
  <option value="nom">Nom</option> 
  <option value="prenom" selected>Prenom</option>
  <option value="sexe">Sexe</option>
  <option value="age">Age</option>
  <option value="ville">Ville</option>
  <option value="quartier">Quartier</option>
  <option value="tel">Tel</option>
  <option value="email">email</option>
</select>
</form>
"""
