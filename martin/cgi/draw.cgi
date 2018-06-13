#!/usr/bin/python
import os
os.environ['PYTHON_EGG_CACHE'] = '/var/www/localhost/eggcache'
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as p 
import cStringIO
buf=cStringIO.StringIO()
print "Content-type: image/png\n"
p.plot(range(10))
p.savefig(buf,format="png")
buf.seek(0)
print buf.read()
