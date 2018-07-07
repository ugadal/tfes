#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

from ft import *
f=cgi.FieldStorage()
exam=f.getvalue("exam")
idp=f.getvalue("idp")
print "Content-type:text/html"
print

print idp
print "L'examen est: %s"%exam
