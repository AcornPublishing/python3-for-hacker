
#!/usr/bin/env python3

import pymysql
import sys

#Open database connection
db = pymysql.connect("127.0.0.1", "root", "1234", "acorn_db")

if db:
	print("Welcome to the MySQL monitor.")
else:
	print("Access denied for user")
	sys.exit()

#prepare a cursor object using cursor() method
cursor = db.cursor()

#execute SQL query using execute() method.
cursor.execute("select version()")

#Fetch a single row using fetchone() method.
data = cursor.fetchone()

print("database version : {} ".format(data))

#disconnect from server
db.close()
