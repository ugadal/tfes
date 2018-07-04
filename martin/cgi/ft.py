#!/usr/bin/python2
# -*- coding: utf-8 -*-
import cgi
import sqlite3 as sql
C=sql.connect("db/impm.db")
c=C.cursor()
mpa={}
mpa["vs"]="vitesse de sedimentation (min)"
mpa["tp"]="temps de peutetre que jai oublie"

