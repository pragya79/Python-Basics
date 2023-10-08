'''How can we change a tuple?
----->firstly convert it into list then apply list methods then convert list into tuple'''

countries=("Spain","Italy","India","England","Germany")
print("Original list is= ",countries)
temp=list(countries)#conversion into list
print(type(temp))
temp.append("Russia")#new item added
temp.pop(3)#3rd index element i.e England is removed
print(temp)
temp[2]="Finland"
countries=tuple(temp)
print("Final list is= ",countries)

'''Merging tuples'''
name1=("Pragya","Sharma")
name2=("Raghav","Latawa")
name=name1+name2
print(name)
count=name.count("Pragya")
print("Count of 'Pragya' in name is ",count)
#Indexing and slicing
marks=(1,2,3,4,5,5,3,4,2,4,3)
index=marks.index(2,4,)#Syntax---> index(element,start,stop)
len=len(marks)
print("Index of 2 is ",index)
print(len)
