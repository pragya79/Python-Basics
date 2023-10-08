import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='admin')
print(mydb.connection_id)
cur=mydb.cursor()
#creating table
cur.execute("CREATE DATABASE db1")
#here s is our query
s="CREATE TABLE Student_record(Name varchar(30),Roll_no interger(6),Branch varchar(20),CGPA float(4))"
cur.execute(s)
#inserting data into table 
s="INSERT INTO Student_record(Name,Roll_no,Branch,CGPA  VALUES(%s,%s,%s,%s))"
r1=('Pragya',228079,'IT',9.0)