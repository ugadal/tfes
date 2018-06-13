#!/usr/bin/python
# -*- coding: utf-8 -*-
import uuid
import cgi
import shelve
print "content-type:text/html"
print
br="<br>\n"
hr="<hr>\n"
form=cgi.FieldStorage()
typemenu=["regulier","vegetarien"]
menuviande=["classic","beef cheese","beef onions"]
menuveggie=["soja burger","tofu burger","onions burger"]
BE="coca,fanta,sprite".split(",")
BA="biere,johnny walker,red bull".split(",")

htmf="""
<form name=step1 action=aiof.cgi method=post enctype="multipart/form-data">
%s
<input type=submit>
<input type=reset>
</form>

"""
als=[]
def inphid(n,v):
	return """<input type=hidden name="%s" value="%s">"""%(n,v)
def inprad(n,v,t=""):
	if not t:t=v
	return """<input type=radio name="%s" value="%s" required>%s"""%(n,v,t)
def inpchx(n,v,t=""):
	if not t:t=v
	return """<input type=checkbox name="%s" value="%s">%s"""%(n,v,t)
def envoi():
	als.append(inphid("id",id))
	print htmf%br.join(als)
	print hr,tir,hr
	exit(0)

if not form.has_key("id"):
	id=uuid.uuid1()
	tir=shelve.open("/tmp/%s.data"%id)
	als.append(inprad("age","adulte","Menu adulte"))
	als.append(inprad("age","enfant","Menu enfant"))
	envoi()
	
	
id=form.getvalue("id")
tir=shelve.open("/tmp/%s.data"%id)

if not tir.has_key("age"):
	age=form.getvalue("age")
	tir["age"]=age
	for v in typemenu:als.append(inprad("typemenu",v))
	envoi()

if not tir.has_key("typemenu"):
	typemenu=form.getvalue("type")
	tir["typemenu"]=typemenu
	if tir["age"]=="adulte":BP=BA+BE
	else:BP=BE
	for b in BP:als.append(inprad("boisson",b))
	envoi()

	
	
