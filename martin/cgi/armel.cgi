#!/usr/bin/env python
# -*- coding: utf-8 -*-
import uuid
import os
import sys
import cgi
import string
ID=uuid.uuid1()
formulaire1="""<form method="post" nom="type d'analyse" action="prog.cgi">
        <input type=hidden name=ID value=%s>
        blastn<input type="radio" name="bn" value="blastn" checked/> qui compare une sequence nucleique a une/des banques nucleiques<br/>
        blastx<input type="radio" name="bn" value="tblastn"/><br/>qui traduit une query nuc en proteine avant de la comparer aux banques prorteiques
        <input type="submit" value="envoyer"/>
        </form>"""%ID
formulaire2="""<form method="post" nom="type d'analyse" action="prog.cgi">
        <input type=hidden name=ID value=%s>
        blastP<input type="radio" name="bp" value="blastt" checked/>protein contre proteine<br/>
        tblastn<input type="radio" name="bp" value="tblastx"/>proteine contre banq nuc traduite en 6 phases proteiques<br/>
        <input type="submit" value="envoyer"/>
        </form>"""%ID
print "Content-type:text/html"
print
dataform=cgi.FieldStorage()
sequence1=dataform.getvalue("seq")
fichier=dataform.getvalue("sequence")
#~ cgi.print_form(dataform)
fn="/tmp/%s.seq"%ID
if fichier:
        seq=open(fn,"w")
        seq.write(fichier)
        seq.close()
if sequence1:
        seq=open(fn,"w")
        seq.write(sequence1)
        seq.close()
else:
        print "Attention une sequence !!!"
        print "veuillez au moins envoyer une sequence <a href=/seq.html> clicquez ici </a>"     
        exit()
#~ seq=open("/tmp/bla","r")
#~ for line in seq: print line.strip()
cmd="infoseq -noheading -only -type %s 2>/dev/null" %fn
#~ cmd="infoseq %s 2>/dev/null" %fn
fc=os.popen(cmd)
print "<pre>"
ts=fc.readline().strip()
print "votre sequence est de type %s !!!!"%ts
if ts=="N":
        print formulaire1
else:
        print formulaire2       
#~ seq.close()
#~ print fichier
#~ print "<br> Bonjour Monsieur %s %s  et merci d'avoir envoye le fichier %s </br>" %(nom,prenom,fichier)
