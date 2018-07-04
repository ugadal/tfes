#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
from ft import *
f=cgi.FieldStorage()
idp=f.getvalue("idp")
print "Content-type:text/html"
print
#~ print "ok"
print """
<body onload=fichpatient(%s)>
<script>
function fichpatient(id) {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      document.getElementById("fp").innerHTML =
      this.responseText;
      cleandiv("se");
    }
  };
	xhttp.open("POST", "getfich2.py", true);
	xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
	xhttp.send("idp="+id);
}
</script>
"""%idp
print """
<div id=fp></div>
<div id=butdiv>
<input type=hidden idp=%s>
"""%(idp)
c.execute("select distinct cp from TA")
for c in c.fetchall():
	print """<input type=button onclick="auboulot()" value=%s>"""%c
print 
"""
</div>
<div id=formdiv>
</div>
</body>
"""%idp
