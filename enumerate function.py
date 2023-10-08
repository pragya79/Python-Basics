marks=(1,2,3,4,5)
print(type(marks))
index=0
for marks in marks:
    print(marks)
    if(index==4):
        print("very good")
    index=index+1
#ALTERNATE METHOD
marks=[10,30,20,49,50]
for index, marks in enumerate(marks,start=2 ):
    print(marks)
    if(index==4):
        print("Well done!!")