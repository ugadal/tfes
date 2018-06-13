#!/usr/bin/python

#FORMULAIRE 

import cgi
import os
import uuid
#~ import MySQLdb

nom=uuid.uuid1()
fn="/tmp/%s.seq"%nom
fo=open(fn, "w")
info="/dev/null"
#~ info="/tmp/info"

print "Content-type:text/html"
print
#~ print "<h1><i>Le Bioinformaticien</i></h1>"
print
print "<hr>"


#~ print "<h1><i>La connaissance fait vivre mais elle n'est pas la vie.</i></h1>"

et="*"
Me=et*200
br="<br>"
hr="<hr>"
dataform=cgi.FieldStorage()
#~ cgi.print_form(dataform)
#~ print dataform

#Recuprer mes valeurs
#~ sc=dataform.getvalue("tarif")
#~ pc=dataform.getvalue("choix")
fl1=dataform.getvalue("file")
print type(fl1)
fl2=dataform.getvalue("seq")
print type(fl2)
if fl2=="":
        fl2=fl1


fo.write(fl1)
fo.close()

#effectuer une commande sur mon fichier
cmd="infoseq -noheading -only -type %s 2>%s"%(fn,info)
res=os.popen(cmd)
typeseq=res.readline().strip()
#~ print "<p>%s</p>"%(a)

cmd="infoseq -noheading -only -length %s 2>%s"%(fn,info)
res=os.popen(cmd)
lonseq=res.readline().strip()

print """<h1>MON BLAST<h1>"""
#~ print "<br>votre preferance est le %s et vous aimez le %s"%(sc,pc)
nseq='''Choisir le type de BLAST <br>
<form name=mm action=blast.cgi method=post enctype="multipart/form-data">
<input type=radio name=type value="blastn" required > BLASTN :  Nuc ====> Nuc<br>
<input type=radio name=type value="blastx" required > BLASTX : Nuc ====> Prot<br>
<input type=radio name=type value="tblastx" required > TBLASTX : Nuc ==>prot ====>Prot <br>
<input type="hidden" name="id" value="%s">
<input type=submit value="Envoyer">
</form> '''%nom

pseq='''Choisir le type de BLAST <br>
<form name=mm action=blast.cgi method=post enctype="multipart/form-data">
<input type=radio name=type value="blastp" required > BLASTP : Prot ====> <br>
<input type=radio name=type value="tblastn" required > TBLASTN : Prot ====> Nuc <br>
<input type="hidden" name="id" value="%s">
<input type=submit value="Envoyer">
</form> '''%nom

if typeseq=="N":
        print "C'est une sequence de nucleodide",br
        print "Longueur : %s nucleotides"%lonseq,br,Me,Me,br
        print nseq
        
else:   
        print "C'est une sequence proteique",br
        print "longueur : %s acides amines"%lonseq,Me,Me,br
        print pseq




#Cours du 11/10/2017


