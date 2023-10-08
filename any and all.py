l1=[2,4,6,8,10]
l2=[1,2,3,4,5]
even=[]
for num in l1:
    if num%2==0:
        even.append(True)
print(even)
#using all function
print(all([num%2==0 for num in l1]))#---->output=true if all the numbers are even
print(any([num%2==0 for num in l1]))#---->output=true if any number is even