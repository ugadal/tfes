#!/usr/bin/env python
# -*- coding: utf-8 -*-



import cgi
import os

print "Content-type:text/html"
print
br="<br>"
hr="<hr>"

et="*"
Me=et*250

print hr


dataform=cgi.FieldStorage()
resultExamen=dataform.getvalue("examen")
username=dataform.getvalue("id")

print """<h1><font color="#BD8D46">LBH</font></h1>"""
print """ <h2 align="right"> Bonjour %s !</h2>"""%username
print resultExamen
