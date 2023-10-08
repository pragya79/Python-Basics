#!/usr/bin/python

import MySQLdb

database = "CODINGGROUND"
username = 'root'
password = 'root'

# Open database connection
db = MySQLdb.connect(host='localhost', user=username, passwd=password, db=database )

# prepare a cursor object using cursor() method
cursor = db.cursor()

sql = "select * from users"

try:
   cursor.execute(sql)
   results = cursor.fetchall()
   for row in results:
      id   = row[0]
      name = row[1]
      age  = row[2]
      sex  = row[3]
      print "%d, %s, %d, %s"%  (id, name, age, sex)

   print "\n"
except:
   print "Error: unable to fecth data"

db.close()