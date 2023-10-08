import mysql.connector
mydb=mysql.connector(
    host="localhost",
    user="root",
    password="admin",
    database="db1"
)
cur=mydb.cursor()
s="SELECT * from Student_record"
cur.execute(s)
result=cur.fetchall()
#loop
for rec in result:
    print(rec)