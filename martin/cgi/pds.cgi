#!/bin/bash
echo """Content-type:text/html

<img src=/pds.jpg width=50%><img src=/pds2.jpe with=50%>
<hr>
<form name=blast action=/cgi-bin/runblast.cgi method=post enctype="multipart/form-data">
"""
for f in $(ls /data/pds/*.plat | grep -v Xxx)
do
bn=$(basename $f)
bn=${bn%.plat}
echo """<input type=radio name=plat value=$bn required>$bn<br>"""
done
echo """<br><hr>"""
for f in /data/pds/Xxx*.plat
do
bn=$(basename $f)
bn=${bn%.plat}
echo """<input type=radio name=plat value=$bn required>$bn<br>"""
done

echo """
<br><hr>
<input type=submit value=analyse>
</form>
"""

