#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
from ft import *
f=cgi.FieldStorage()
idp=f.getvalue("idp")
print "Content-type:text/html"
print
print """<html>
<body onload=fichpatient(%s)>
<script>
function cleandiv(namediv) {
	document.getElementById(namediv).innerHTML =""
}

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
<input type=hidden idp=%s>
"""%(idp)

print "<h2>Selectionnez un type d'examen</h2>"
c.execute("select distinct cp from TA")
i=1
for c in c.fetchall():
	c=c[0]
	print """<input type="button" onclick="addexam_%s()" value="%s" id="examens">"""%(i,c)	
	print """<script>
	function addexam_%s() {
		var btn = document.querySelector('input');
		var exam=btn.value;
	  var xhttp = new XMLHttpRequest();
	  xhttp.onreadystatechange = function() {
		if (this.readyState == 4 && this.status == 200) {
		  document.getElementById("analyse").innerHTML =
		  this.responseText;
		  cleandiv("formdiv");
		}
	  };
		xhttp.open("POST", "addexam.py", true);
		xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
		xhttp.send("exam="+"%s"+"&idp="+%s);
	}

	</script>
	"""%(i,c,idp)
	i+=1
	
print """<script>
function examform() {
	form=document.getElementById("examform");
	var z="";
	for (i=0;i<form.length;i++) {
		te=form.elements[i];
		w=te.name;
		v=te.value;
		if (te.type!="radio" || te.checked ) {z+="&"+w+"="+v;}
	}
	var xhttp = new XMLHttpRequest();
	xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
		//~ alert(this.responseText);
      document.getElementById("formdiv").innerHTML=this.responseText;
      loadpatients();
      forcefichpat();
    }
  };
	xhttp.open("POST", "examform.py");
	xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
	xhttp.send(z);
	return false;
}

</script>
"""

#############################################################################################################
print """	
	<style type="text/css">
div{position: absolute; padding: 1em; border: 1px solid #000}
#examens{background: #FF0040; top: 0; left: 0; right: 60%; border: 5px solid; bottom: 75%;overflow:auto}
#fp{background: #F7BE81; top: 25%; left: 0%; right: 63%; bottom: 0;}
#analyse{background: #A9D0F5; top: 0; left: 37%; right: 0; bottom: 35%;overflow:auto}
#formdiv{background: #F4FA58; top: 65%; left: 37%; right: 0;overflow:auto}
</style>	
"""



print """
</div>
<div id="analyse">
</div>
<div id="formdiv">
</div>
</body>
"""
print "<hr></html>"
