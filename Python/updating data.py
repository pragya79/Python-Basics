import mysql.connector
mydb=mysql.connector(
    host="localhost",
    user="root",
    password="admin",
    database="db1"
)
cur=mydb.cursor()
s="UPDATE Student_record SET CGPA=CGPA+1 WHERE CGPA<10"
cur.execute(s)
mydb.commit()