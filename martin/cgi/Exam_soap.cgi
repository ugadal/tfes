#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

from SOAPpy import *
conn=SOAPProxy("http://192.168.2.10:3564")
r=conn.tran("Soap made all so simple")
print r
