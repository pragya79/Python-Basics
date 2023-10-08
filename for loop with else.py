#LOOP WITH ELSE STATEMENT
for i in range(5):
    print(i)
else:
    print("sorry no i")

for k in []:#empty hence else statement will run
    print(k)
else:
    print("sorry no k")


for i in range(6):
    print(i)
    if(i==4):
        break
#Else statement only runs when loop successfully completes not when it gets break
#her loopgets break after i=4 hence else statement will not run
else:
    print("sorry no i")