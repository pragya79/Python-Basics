def even(a):
    return a%2==0
numbers=[2,32,5,7,9,1,2,5]
#now we have to filter out even numbers from list and append them in another list
evens=[]
evens=tuple(filter(even,numbers))
print(evens)
for i in evens:
    print(i)