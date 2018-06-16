#!/usr/bin/env python
# -*- coding: utf-8 -*-
#


import cgi
import os

print "Content-type:text/html"
print

dataform=cgi.FieldStorage()

ID_patient=str(dataform.getvalue("patient"))

type_examen=dataform.getvalue("exam")





