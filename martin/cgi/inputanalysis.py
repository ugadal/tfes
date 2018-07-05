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
for c in c.fetchall():
	print """<input type="button" onclick="addexam()" value="%s">"""%c
	print """<input type=hidden name=exam value=%s> """%c

	print """<script>
	function addexam() {
		var btn = document.querySelector('input');
		var exam=btn.value
		alert("%s");
	  var xhttp = new XMLHttpRequest();
	  xhttp.onreadystatechange = function() {
		if (this.readyState == 4 && this.status == 200) {
		  document.getElementById("formdiv").innerHTML =
		  this.responseText;
		  alert(this.responseText);
		}
	  };
		xhttp.open("POST", "addexam.py", true);
		xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
		xhttp.send("exam="+exam);
	}

	</script>
	"""%c

print """
</div>
<div id=formdiv>
</div>
</body>
"""
print "<hr></html>"
