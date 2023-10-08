f=open("myfile.txt","r")
i=0
while True:
    i=i+1
    line=f.readline()
    if not line:
        break
    name=line.split(",")[0]
    age=line.split(",")[1]
    rollno=line.split(",")[1]
    print(f"Name of student {i} is: {name} ")
    print(f"Age of student {i} is: {age} ")
    print(f"Roll No of student {i} is: {rollno} ")
    print(line)
    