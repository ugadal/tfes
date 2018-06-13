#!/usr/bin/python
# -*- coding: utf-8 -*-
import cgi
import os
import time

print "Content-type:text/html"
print
print """<img src=/pds.jpg width=50%><img src=/pds2.jpe with=50%>
<hr>
"""
br="<br>\n"
hr="<hr>\n"
form=cgi.FieldStorage()
plat=form.getvalue("plat")
time.sleep(3)
#cl="""/data/pds/be/blastn -query /data/pds/%s.sample -db /data/pds/FG -outfmt '6 sseqid'| sed -e "s/_.*//" | sort | uniq -c | sort -nr"""%plat
cl="""cat /data/pds/%s.blastout"""%plat
r=os.popen(cl).readlines()
print """
<html>
<head>
<!--Load the AJAX API-->
<script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
<script type="text/javascript">
google.charts.load('current', {'packages':['corechart']});
google.charts.setOnLoadCallback(drawChart);
function drawChart() {
var data = new google.visualization.DataTable();
data.addColumn('string', 'Organisme');
data.addColumn('number', "fragment d'ADN identifies");
data.addRows([
"""
for l in r:
    a,b=l.split()
    print """['%s',%s],"""%(b,a)
print """
]);
var options = {'title':'Analyse du plat %s',
'width':600,
'height':450,
'is3D':true};
var chart = new google.visualization.PieChart(document.getElementById('chart_div'));
chart.draw(data, options);
}
</script>
</head>

<body>
<!--Div that will hold the pie chart-->
<div id="chart_div"></div>
</body>
<a href=/cgi-bin/pds.cgi> Une autre analyse SVP </a><br><br>      =;B^)
</html>
"""%plat

