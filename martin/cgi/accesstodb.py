#!python2
import sqlite3
C=sqlite3.connect("db/example.db")
c=C.cursor()
c.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(c.fetchall())

c.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = c.fetchall()
for table_name in tables:
        table_name = table_name[0]
        print table_name
        c.execute("""select sql from sqlite_master where name='%s' """%table_name)
        print c.fetchall()
