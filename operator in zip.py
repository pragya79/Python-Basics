l1=[1,2,3]
l2=[4,5,6]
#method 1
print(list(zip(l1,l2)))
#to create l=[(1,4),(2,5),(3,6)]
#method 2
l=[(1,4),(2,5),(3,6)]
zip(*l)#unpacks the list
print(list(zip(*l)))#it will give a list having 2 tuples
#unpacking the tuples
l1,l2=list(zip(*l))
print(l1)
print(l2)
print(list(zip(l1,l2)))
#exercise
l1=[1,2,3]
l2=[4,5,6]
new_list=[]
#to create a new list having values max of each pair
for pair in zip(l1,l2):
    new_list.append(max(pair))
print(new_list)