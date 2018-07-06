#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
from ft import *
f=cgi.FieldStorage()
idp=f.getvalue("idp")
print "Content-type:text/html"
print
#~ print "ok"
print """<html>
<body onload=fichpatient(%s)>
<script>
function fichpatient(id) {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      document.getElementById("fp").innerHTML =
      this.responseText;
    }
  };
	xhttp.open("POST", "getfich2.py", true);
	xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
	xhttp.send("idp="+id);
}


</script>"""%idp


print """
<div id=fp></div>
<div id=butdiv>
<input type=hidden idp=%s>
"""%(idp)
c.execute("select distinct cp from TA")
i=1
for c in c.fetchall():
	c=c[0]
	print """<input type="button" onclick="addexam_%s()" value="%s">"""%(i,c)
	#~ print """<input type=hidden name=exam value=%s> """%c
	#
	#
	# CA NE VA PAS CA
	# tu recrees une fonction addexam() et un hidden à chaque fois ! (car dans la boucle)
	# si tu as besoin d'une fonction tu dois l"inserer au niveau de la ligne 25
	#
	#~ deuxio:
		#~ qu'est ce que tu as mis dans la table TA ?
		#~ tu as mis des categories primaires et secondaire mais pas de mesure
		#~ le type d'input a été change en integer ? pourquoi ?
	
	print """<script>
	function addexam_%s() {
		var btn = document.querySelector('input');
		var exam=btn.value;
	  var xhttp = new XMLHttpRequest();
	  xhttp.onreadystatechange = function() {
		if (this.readyState == 4 && this.status == 200) {
		  document.getElementById("formdiv").innerHTML =
		  this.responseText;
		}
	  };
		xhttp.open("POST", "addexam.py", true);
		xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
		xhttp.send("exam="+"%s"+"&idp="+%s);
	}

	</script>
	"""%(i,c,idp)
	i+=1

print """
</div>
<div id=formdiv>
</div>
</body>
"""
print "<hr></html>"
