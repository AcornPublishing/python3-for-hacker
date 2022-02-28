
#!/usr/bin/env python
#-*-coding:utf-8 -*-

import MySQLdb

#Open database connection
db = MySQLdb.connect("127.0.0.1", "root", "1234", "acorn_db")

#prepare a cursor object using cursor() method
cursor = db.cursor()

#execute SQL query using execute() method.
cursor.execute("select version()")

#Fetch a single row using fetchone() method.
data = cursor.fetchone()

print "database version : %s " % data

#disconnect from server
db.close()
