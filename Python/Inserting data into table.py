import mysql.connector
mydb=mysql.connector(
    host="localhost",
    user="root",
    password="admin",
    database="db1"
)
cur=mydb.cursor()
#here s is our query
s="CREATE TABLE Student_record(Name varchar(30),Roll_no interger(6),Branch varchar(20),CGPA float(4))"
cur.execute(s)
#inserting data into table 
s="INSERT INTO Student_record(Name,Roll_no,Branch,CGPA  VALUES(%s,%s,%s,%s))"
# r1=('Pragya',228079,'IT',9.0)#r1 is a tuple object
# cur.execute(s,r1)
#student is a list of tuples
students=[('Pallavi',228077,'IT',9.0),
         ('Akshat',218011,'CSE',10.0),
         ('Shivangi',228091,'IT',9.0),
         ('Nancy',228072,'IT',9.0)]
cur.executemany(s,students)#for list of tuples

mydb.commit()#saves the changes we made